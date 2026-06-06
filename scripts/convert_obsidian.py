#!/usr/bin/env python3
"""Convert Obsidian KB notes to VitePress-compatible markdown."""

import os
import re
import shutil
import yaml
from pathlib import Path

# Paths
OBSIDIAN_ROOT = Path("/mnt/d/scRNA/code/omics_applications/obsidian_kb")
VITEPRESS_ZH = Path("/mnt/d/scRNA/code/omics-kb/docs/zh")

# Folder name mapping: Obsidian → VitePress (kebab-case)
FOLDER_MAP = {
    "Single_Cell_RNA_seq": "single-cell-rna-seq",
    "Multi_omics": "multi-omics",
    "Spatial_Omics": "spatial-omics",
    "Perturbation": "perturbation",
}

# MOC file mapping
MOC_MAP = {
    "README.md": "guide/index.md",
    "Analysis_Modules.md": "guide/analysis-modules.md",
    "Visualization_Methods.md": "guide/visualization.md",
}


def convert_wikilinks(content: str) -> str:
    """Convert Obsidian [[folder/note|display]] or [[note]] to standard markdown links."""

    def _replace_wikilink(match: re.Match) -> str:
        inner = match.group(1)
        if "|" in inner:
            target, display = inner.split("|", 1)
        else:
            target = display = inner

        # Clean display name from markdown backticks or path styling
        display = display.strip()

        # Convert folder path to kebab-case
        parts = target.split("/")
        if len(parts) == 2:
            folder, note = parts
            vp_folder = FOLDER_MAP.get(folder, folder.lower().replace("_", "-"))
            return f"[{display}](../{vp_folder}/{note.lower()}.md)"
        elif len(parts) == 1:
            # Check if this maps to a folder prefix or is a general note
            # If target exists in FOLDER_MAP or is known, otherwise treat it as relative in same directory
            # For index/MOC links:
            if target == "Analysis_Modules":
                return f"[{display}](../guide/analysis-modules.md)"
            elif target == "Visualization_Methods":
                return f"[{display}](../guide/visualization.md)"
            elif target == "README":
                return f"[{display}](../guide/index.md)"
            return f"[{display}](./{parts[0].lower()}.md)"
        else:
            return f"[{display}](.{target})"

    return re.sub(r"\[\[([^\]]+)\]\]", _replace_wikilink, content)


def convert_file_urls(content: str, github_url: str) -> str:
    """Replace file:///D:/... URLs with GitHub blob/tree URLs or fallback description."""
    def _get_clean_fallback(match: re.Match) -> str:
        file_path = match.group(1)
        normalized_path = file_path.replace("\\", "/")
        parts = normalized_path.split("/")
        # Find where 'omics_applications' is, and keep the path starting from the repo folder name
        try:
            idx = parts.index("omics_applications")
            # Return relative path within the omics_applications dir
            clean_path = "/".join(parts[idx + 1:])
            # Capitalize directory steps for cleaner view, e.g. "Single_Cell_RNA_seq / admultiregion_analysis"
            return f"`[Local Code] {clean_path}`"
        except ValueError:
            # If omics_applications is not in path, just return the last 2 components
            if len(parts) >= 2:
                return f"`[Local Code] {parts[-2]}/{parts[-1]}`"
            return f"`[Local Code] {parts[-1]}`"

    if not github_url:
        return re.sub(r"file:///([^\s\)]+)", _get_clean_fallback, content)

    # Clean github url
    github_url = github_url.strip().rstrip("/")
    if github_url.endswith(".git"):
        github_url = github_url[:-4]

    def _replace_file_url(match: re.Match) -> str:
        file_path = match.group(1)
        normalized_path = file_path.replace("\\", "/")
        repo_name = github_url.split("/")[-1]
        parts = normalized_path.split("/")
        try:
            idx = parts.index(repo_name)
            relative = "/".join(parts[idx + 1:])
            return f"{github_url}/blob/main/{relative}"
        except ValueError:
            try:
                idx = parts.index("omics_applications")
                relative = "/".join(parts[idx + 3:])
                return f"{github_url}/blob/main/{relative}"
            except ValueError:
                return github_url

    return re.sub(r"file:///([^\s\)]+)", _replace_file_url, content)


def sanitize_html_and_brackets(text: str) -> str:
    """Escape all angle brackets to entity equivalents to secure Vue/VitePress compilation."""
    # Simple and robust escaping of < and > to bypass Vue template compile failures
    # This prevents any bare or malformed HTML tags from breaking the build
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    return text


def convert_note(src_path: Path, dest_dir: Path, folder_key: str) -> None:
    """Convert a single Obsidian note to VitePress format."""
    content = src_path.read_text(encoding="utf-8")

    # Parse frontmatter to get github_url
    github_url = ""
    fm_raw = ""
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_raw = parts[1]
            body = parts[2]
            
            # Pre-clean source_path line with regex because invalid backslashes break yaml.safe_load
            fm_raw = re.sub(r"source_path:[^\n]+", "", fm_raw)
            
            try:
                fm = yaml.safe_load(fm_raw)
                if isinstance(fm, dict):
                    github_url = fm.get("github_url", "")
                    
                    # Clean up local path from frontmatter to prevent exposing Windows paths on GitHub site
                    if "source_path" in fm:
                        del fm["source_path"]
                    
                    # Double check other keys and sanitize backslashes to forward slashes to prevent yaml escape issues
                    for k, v in list(fm.items()):
                        if isinstance(v, str) and "\\" in v:
                            fm[k] = v.replace("\\", "/")
                            
                    # Convert back to yaml
                    fm_raw = yaml.dump(fm, allow_unicode=True, default_flow_style=False).strip()
            except yaml.YAMLError as e:
                print(f"  ⚠️ YAML Parse Error in {src_path.name}: {e}")
                # Fallback: regex delete source_path from raw string directly
                fm_raw = re.sub(r"\nsource_path:[^\n]+", "", fm_raw)

    # Convert links and URLs in the body
    body = convert_wikilinks(body)
    body = convert_file_urls(body, github_url)
    body = sanitize_html_and_brackets(body)

    # Normalize some Markdown issues (e.g. double colons from Obsidian Dataview notation `Key:: Value`)
    body = re.sub(r"^- \*\*([^*]+)\*\*::", r"- **\1**:", body)
    body = re.sub(r"^- ([a-zA-Z0-9_\s\u4e00-\u9fa5]+)::", r"- **\1**:", body)

    # Destination filename in kebab-case/lowercase
    dest_name = src_path.stem.lower() + ".md"
    dest_path = dest_dir / dest_name
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Reassemble with frontmatter and div v-pre wrapper to completely bypass Vue compilation errors on arbitrary body content
    output = f"---\n{fm_raw.strip()}\n---\n\n<div v-pre>\n\n{body.strip()}\n\n</div>\n"
    dest_path.write_text(output, encoding="utf-8")


def convert_moc(src_path: Path, dest_rel: str) -> None:
    """Convert MOC index pages."""
    content = src_path.read_text(encoding="utf-8")
    content = convert_wikilinks(content)
    
    # Remove double colons Dataview notation from MOC pages if any
    content = re.sub(r"::", r":", content)

    dest_path = VITEPRESS_ZH / dest_rel
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    # Also wrap MOC pages with v-pre
    output = f"<div v-pre>\n\n{content.strip()}\n\n</div>\n"
    dest_path.write_text(output, encoding="utf-8")


def main():
    print("🔄 Converting Obsidian KB → VitePress zh/ ...")

    # Clear target dir except index.md
    if VITEPRESS_ZH.exists():
        for item in VITEPRESS_ZH.iterdir():
            if item.name != "index.md":
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()

    # 1. Convert tool notes
    for obs_folder, vp_folder in FOLDER_MAP.items():
        src_dir = OBSIDIAN_ROOT / obs_folder
        dest_dir = VITEPRESS_ZH / vp_folder
        dest_dir.mkdir(parents=True, exist_ok=True)

        if not src_dir.exists():
            print(f"  ⚠️ Skipping {obs_folder}: not found")
            continue

        print(f"📂 Processing {obs_folder} ...")
        notes = []
        for md_file in sorted(src_dir.glob("*.md")):
            convert_note(md_file, dest_dir, obs_folder)
            
            # Record for index page
            notes.append(md_file.stem)
            
        # Generate category portal index.md
        cat_title = obs_folder.replace("_", " ")
        cat_emojis = {
            "Single_Cell_RNA_seq": "💻",
            "Multi_omics": "🧬",
            "Spatial_Omics": "🗺️",
            "Perturbation": "⚡"
        }
        emoji = cat_emojis.get(obs_folder, "📂")
        
        index_content = f"# {emoji} {cat_title}\n\n"
        index_content += f"本分类下收录了 {len(notes)} 个工具与高影响力代码分析流程：\n\n"
        index_content += "<div v-pre>\n\n"
        for note in notes:
            index_content += f"- [{note}](./{note.lower()}.md)\n"
        index_content += "\n</div>\n"
        
        (dest_dir / "index.md").write_text(index_content, encoding="utf-8")
        print(f"  ✨ Generated category portal: {vp_folder}/index.md")

    # 2. Convert MOC pages
    print("📑 Processing MOC pages...")
    for src_name, dest_rel in MOC_MAP.items():
        src_path = OBSIDIAN_ROOT / src_name
        if src_path.exists():
            convert_moc(src_path, dest_rel)

    print(f"✅ Conversion complete! Files generated in {VITEPRESS_ZH}")


if __name__ == "__main__":
    main()

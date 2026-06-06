#!/usr/bin/env python3
"""Generate VitePress sidebar config from docs directory structure."""

import json
import yaml
from pathlib import Path

DOCS_ROOT = Path("/mnt/d/scRNA/code/omics-kb/docs")

CATEGORIES = {
    "single-cell-rna-seq": {"zh": "💻 单细胞 RNA-seq", "en": "💻 scRNA-seq"},
    "multi-omics": {"zh": "🧬 多组学整合", "en": "🧬 Multi-omics"},
    "spatial-omics": {"zh": "🗺️ 空间组学", "en": "🗺️ Spatial Omics"},
    "perturbation": {"zh": "⚡ 扰动分析", "en": "⚡ Perturbation"},
}


def build_sidebar(lang: str) -> dict:
    """Build sidebar config for a given language."""
    lang_root = DOCS_ROOT / lang
    sidebar = {}

    # 1. Generate sidebars for main categories
    for folder, labels in CATEGORIES.items():
        folder_path = lang_root / folder
        if not folder_path.exists():
            continue

        items = []
        # Gather all markdown files in category
        for md_file in sorted(folder_path.glob("*.md")):
            if md_file.name == "index.md":
                continue
            
            # Read name from YAML frontmatter, fallback to capitalized filename
            name = md_file.stem.upper()
            content = md_file.read_text(encoding="utf-8")
            if content.startswith("---"):
                try:
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        fm = yaml.safe_load(parts[1])
                        if isinstance(fm, dict) and "name" in fm:
                            name = fm["name"]
                except yaml.YAMLError:
                    pass

            items.append({
                "text": name,
                "link": f"/{lang}/{folder}/{md_file.stem}",
            })

        # Add sidebar mapping for this sub-path
        sidebar[f"/{lang}/{folder}/"] = [
            {
                "text": labels[lang],
                "collapsed": False,
                "items": items,
            }
        ]

    # 2. Add sidebar for MOC guide section
    guide_items = []
    guide_path = lang_root / "guide"
    if guide_path.exists():
        # Order MOC files logically: modules -> visualization
        moc_files = ["analysis-modules.md", "visualization.md"]
        for filename in moc_files:
            file_path = guide_path / filename
            if file_path.exists():
                text = "Analysis Modules" if filename == "analysis-modules.md" else "Visualization"
                if lang == "zh":
                    text = "⚙️ 分析模块检索" if filename == "analysis-modules.md" else "🎨 可视化方法"
                guide_items.append({
                    "text": text,
                    "link": f"/{lang}/guide/{file_path.stem}"
                })
        
        # Add MOC guide sidebar mapping
        sidebar[f"/{lang}/guide/"] = [
            {
                "text": "📑 指南" if lang == "zh" else "📑 Guide",
                "items": guide_items
            }
        ]

    return sidebar


def main():
    zh_sidebar = build_sidebar("zh")
    en_sidebar = build_sidebar("en")

    output = {
        "zh": zh_sidebar,
        "en": en_sidebar,
    }

    out_path = DOCS_ROOT / ".vitepress" / "sidebar.json"
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Sidebar configuration generated at {out_path}")
    print(f"   zh: {len(zh_sidebar)} categories mapped")
    print(f"   en: {len(en_sidebar)} categories mapped")


if __name__ == "__main__":
    main()

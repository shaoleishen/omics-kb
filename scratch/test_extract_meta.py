import re
import yaml
from pathlib import Path

OBSIDIAN_ROOT = Path("/mnt/d/scRNA/code/omics_applications/obsidian_kb")

def extract_meta_from_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    
    # 1. Parse Frontmatter
    fm = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
            except:
                pass
    
    # 2. Extract Intro/Overview First Paragraph
    intro = ""
    # Look for ## 📝 简介 or ## 📝 Overview
    m = re.search(r"## 📝 (?:简介|Overview)\n(.*?)(?=\n##|\n---|$)", content, re.DOTALL)
    if m:
        para = m.group(1).strip()
        # Remove markdown quotes, images or links from the description preview
        para = re.sub(r"<[^>]+>", "", para) # Remove html tags
        para = re.sub(r"!\[.*?\]\(.*?\)", "", para) # Remove markdown images
        para = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", para) # Keep text from markdown links
        para = para.replace(">", "").strip()
        
        # Split by sentences (dot followed by space, or Chinese period)
        sentences = re.split(r"(?<=[.。])\s*", para)
        # Grab first 2 sentences
        intro = " ".join(sentences[:2]).strip()
        if len(intro) > 200:
            intro = intro[:197] + "..."
            
    # 3. Assemble Analysis Pipeline (e.g. R: Seurat + ggplot2)
    lang = fm.get("language", [])
    pkgs = fm.get("packages", [])
    viz = fm.get("visualizations", [])
    
    pipelines = []
    if "R" in lang:
        r_pkgs = [p for p in pkgs if p in ["Seurat", "SingleCellExperiment", "scran"]]
        r_viz = [v for v in viz if v in ["ggplot2", "ggpubr"]]
        pkg_str = " + ".join(r_pkgs) if r_pkgs else "Base R"
        viz_str = f" + {r_viz[0]}" if r_viz else ""
        pipelines.append(f"R: {pkg_str}{viz_str}")
        
    if "Python" in lang:
        py_pkgs = [p for p in pkgs if p in ["Scanpy", "AnnData", "scvi-tools", "scvi"]]
        py_viz = [v for v in viz if v in ["matplotlib", "seaborn", "plotly"]]
        pkg_str = " + ".join(py_pkgs) if py_pkgs else "Python"
        viz_str = f" + {py_viz[0]}" if py_viz else ""
        pipelines.append(f"Python: {pkg_str}{viz_str}")
        
    # Fallback if no specific pipeline is built
    if not pipelines:
        if lang:
            pipelines.append(", ".join(lang))
        else:
            pipelines.append("Not specified")
            
    return {
        "name": fm.get("name", file_path.stem),
        "pipeline": " | ".join(pipelines),
        "modules": ", ".join(fm.get("modules", [])),
        "intro": intro,
        "github_url": fm.get("github_url", "")
    }

# Test on 3 files
files = list(OBSIDIAN_ROOT.glob("**/*.md"))[:5]
for f in files:
    if f.name not in ["README.md", "Analysis_Modules.md", "Visualization_Methods.md"]:
        print(f"--- File: {f.name} ---")
        meta = extract_meta_from_file(f)
        for k, v in meta.items():
            print(f"  {k}: {v}")

#!/usr/bin/env python3
"""Translate Chinese VitePress notes to English using field mapping."""

import re
import shutil
from pathlib import Path

ZH_ROOT = Path("/mnt/d/scRNA/code/omics-kb/docs/zh")
EN_ROOT = Path("/mnt/d/scRNA/code/omics-kb/docs/en")

# Field/heading translation mapping
TRANSLATIONS = {
    # Category index portals
    "# 💻 Single Cell RNA seq": "# 💻 Single-cell RNA-seq",
    "# 🧬 Multi omics": "# 🧬 Multi-omics Integration",
    "# 🗺️ Spatial Omics": "# 🗺️ Spatial Omics",
    "# ⚡ Perturbation": "# ⚡ Perturbation Analysis",
    "本分类下收录了": "This category contains",
    "个工具与高影响力代码分析流程：": "tools and high-impact analysis pipelines:",

    # MOC Navigation Headers
    "# 🧬 高影响力多组学应用代码 Obsidian 知识库": "# 🧬 High-Impact Omics Code Knowledge Base",
    "## 📂 组学分类入口 (Primary Folders)": "## 📂 Omics Categories",
    "### 💻 单细胞 RNA-seq (Single-cell RNA-seq)": "### 💻 Single-cell RNA-seq",
    "### 🗺️ 空间组学 (Spatial Omics)": "### 🗺️ Spatial Omics",
    "### 🧬 多组学整合 (Multi-omics)": "### 🧬 Multi-omics Integration",
    "### ⚡ 扰动分析 (Perturbation)": "### ⚡ Perturbation Analysis",
    "## 🔍 多维度快捷检索 MOC": "## 🔍 Quick Access MOC",
    "欢迎使用多组学应用代码库。本知识库包含 87 个来自 Nature、Cell、Science 级别期刊的代码，已按照物理组学分类和多维度分析/可视化引擎建立关联。": 
        "Welcome to the Multi-omics Code Knowledge Base. This repository indexes and analyzes 87 front-line codebases from Nature, Cell, and Science publications, categorizing them by physical omics types, analysis modules, and plotting engines.",

    # Note section headings
    "## 📝 简介": "## 📝 Overview",
    "## ⚙️ 分析模块支持": "## ⚙️ Analysis Modules",
    "## 🎨 可视化实现": "## 🎨 Visualization",
    "## 📂 核心代码文件链接": "## 📂 Key Code Files",

    # Field labels
    "- **原始分类文件夹**:": "- **Original Category**:",
    "- **GitHub 链接**:": "- **GitHub Link**:",
    "- **本地源码路径**:": "- **Source Code**:",
    "- **导入与预处理**:": "- **Import & Preprocessing**:",
    "- **QC 质控**:": "- **Quality Control**:",
    "- **聚类与降维**:": "- **Clustering & Dim. Reduction**:",
    "- **细胞类型鉴定与注释**:": "- **Cell Type Annotation**:",
    "- **拟时序与轨迹分析**:": "- **Trajectory Analysis**:",
    "- **绘图引擎**:": "- **Plotting Engine**:",

    # Common phrases in content
    "检测到 Python 脚本文件。": "Python scripts detected.",
    "检测到 R 脚本文件。": "R scripts detected.",
    "未检测到显式 QC 过滤逻辑。": "No explicit QC filtering logic detected.",
    "未检测到显式可视化或绘图逻辑。": "No explicit plotting or visualization logic detected.",
    "支持": "Supported",
    "未检测到": "Not detected",

    # Analysis Modules MOC
    "# ⚙️ 分析模块检索 MOC": "# ⚙️ Analysis Modules Index",
    "本页面按照数据分析模块，对 87 个高影响力仓库进行分类静态索引。":
        "This page indexes 87 high-impact repositories by analysis module.",
    "## 🧼 1. QC 质控与细胞过滤": "## 🧼 1. Quality Control & Cell Filtering",
    "以下仓库代码中包含明显的质控（如线粒体过滤、双细胞过滤等）逻辑:":
        "The following repositories contain explicit quality control (e.g., mitochondrial filtering, doublet detection) logic:",
    "## 🧮 2. 降维与聚类分析": "## 🧮 2. Dimensionality Reduction & Clustering",
    "以下仓库代码中包含降维（PCA/UMAP/t-SNE）及细胞 Leiden/Louvain/Seurat 聚类逻辑:":
        "The following repositories contain dimensionality reduction (PCA/UMAP/t-SNE) and clustering (Leiden/Louvain/Seurat) logic:",
    "## 🏷️ 3. 细胞类型注释": "## 🏷️ 3. Cell Type Annotation",
    "以下仓库代码中包含基于 marker 基因或自动注释工具的细胞类型鉴定逻辑:":
        "The following repositories contain cell type identification and annotation logic based on marker genes or automated tools:",
    "## 🌊 4. 拟时序与轨迹推断": "## 🌊 4. Trajectory Inference",
    "以下仓库代码中包含拟时序、细胞轨迹或分化潜能分析逻辑:":
        "The following repositories contain trajectory inference, pseudotime, or differentiation potential analysis logic:",
    "## 🔬 5. 差异分析与统计": "## 🔬 5. Differential Analysis & Statistics",
    "以下仓库代码中包含组间差异表达基因（DEG）筛选或空间特异表达分析逻辑:":
        "The following repositories contain differential gene expression (DEG) analysis or spatially variable gene detection logic:",

    # Visualization MOC
    "# 🎨 可视化方法检索 MOC": "# 🎨 Visualization Methods Index",
    "本页面按照绘图引擎和编程语言，对 87 个高影响力仓库的可视化逻辑进行分类静态索引。":
        "This page indexes the visualization methods of 87 high-impact repositories by plotting engine and programming language.",
    "## 🐍 1. Python 可视化引擎": "## 🐍 1. Python Visualization Engines",
    "### 📊 A. matplotlib / seaborn / scanpy.pl": "### 📊 A. matplotlib / seaborn / scanpy.pl",
    "以下仓库使用 Python 标准绘图库进行可视化:":
        "The following repositories use Python standard plotting libraries for visualization:",
    "## 🧣 2. R 可视化引擎": "## 🧣 2. R Visualization Engines",
    "### 📊 A. ggplot2 / Seurat::DimPlot": "### 📊 A. ggplot2 / Seurat::DimPlot",
    "以下仓库使用 R/ggplot2 生态系统进行可视化:":
        "The following repositories use R/ggplot2 ecosystem for visualization:",
    "### 🗺️ B. 空间热图与特殊绘图": "### 🗺️ B. Spatial Heatmaps & Custom Plots",
    "以下仓库中包含定制化的空间点图、分子密度图或轨迹图等特殊可视化:":
        "The following repositories contain customized spatial plots, molecular density maps, or custom trajectory plots:",

    # MOC Quick Navigation link display names
    "按分析模块检索 (导入、QC、聚类、注释、拟时序等)": "Search by Analysis Modules (Import, QC, Clustering, Annotation, Trajectory, etc.)",
    "按可视化方法与语言检索 (R/ggplots, Python/matplotlib, built-in)": "Search by Visualization Methods & Languages (R/ggplot2, Python/matplotlib, built-in)",
}

# Sort keys by length in descending order to avoid partial substitutions
SORTED_TRANSLATIONS = sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0]))


def translate_file(src: Path, dest: Path) -> None:
    """Translate a single file using the mapping table."""
    content = src.read_text(encoding="utf-8")

    # Perform key-value translation
    for zh, en in SORTED_TRANSLATIONS:
        content = content.replace(zh, en)

    # Clean frontmatter tags if any
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_raw = parts[1]
            body = parts[2]
            # Replace tags in frontmatter for english pages
            fm_raw = fm_raw.replace("Single_Cell_RNA_seq", "single-cell-rna-seq")
            fm_raw = fm_raw.replace("Multi_omics", "multi-omics")
            fm_raw = fm_raw.replace("Spatial_Omics", "spatial-omics")
            fm_raw = fm_raw.replace("Perturbation", "perturbation")
            content = f"---{fm_raw}---{body}"

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")


def main():
    print("🌐 Translating zh/ → en/ ...")

    if EN_ROOT.exists():
        shutil.rmtree(EN_ROOT)

    count = 0
    for zh_file in sorted(ZH_ROOT.rglob("*.md")):
        rel = zh_file.relative_to(ZH_ROOT)
        en_file = EN_ROOT / rel
        translate_file(zh_file, en_file)
        count += 1

    print(f"✅ Translation complete! Generated {count} files in {EN_ROOT}")


if __name__ == "__main__":
    main()

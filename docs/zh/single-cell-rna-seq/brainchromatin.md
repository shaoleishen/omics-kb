---
github_url: https://github.com/alexandrotrevino/brainchromatin
language:
- R
modules:
- Clustering
name: brainchromatin
omics: Single_Cell_RNA_seq
packages:
- Seurat
tags:
- Single_Cell_RNA_seq
- R
- Seurat
- Clustering
visualizations:
- ggplot2
---

<div v-pre>

# brainchromatin

- **原始分类文件夹**:: brain_diseases_2023
- **GitHub 链接**:: [alexandrotrevino/brainchromatin](https://github.com/alexandrotrevino/brainchromatin)
- **本地源码路径**:: [brainchromatin](https://github.com/alexandrotrevino/brainchromatin/blob/main/)

---

## 📝 简介
Code used to analyze single cell RNA and ATAC sequencing in developing human cerebral cortex. Publication DOI: https://doi.org/10.1016/j.cell.2021.07.039 Data files can be accessed here using get_data.sh and links.txt, or just by pulling the files from links.txt. Note that their combined size exceeds 10 Gb!

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 未检测到自动化细胞标注逻辑。
- **拟时序与轨迹分析**:: 未检测到拟时序分析逻辑。

## 🎨 可视化实现
- **绘图引擎**:: ggplot2

## 📂 核心代码文件链接
- [R/Single_Cell_Functions.R](https://github.com/alexandrotrevino/brainchromatin/blob/main/R/Single_Cell_Functions.R)

</div>

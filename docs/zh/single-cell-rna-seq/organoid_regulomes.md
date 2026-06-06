---
github_url: https://github.com/quadbio/organoid_regulomes
language:
- R
- Python
modules:
- Clustering
- Annotation
- Trajectory
name: organoid_regulomes
omics: Single_Cell_RNA_seq
packages:
- Seurat
- Scanpy
tags:
- Single_Cell_RNA_seq
- R
- Python
- Seurat
- Scanpy
- Clustering
- Annotation
- Trajectory
visualizations:
- ggplot2
- matplotlib
- seaborn
---

<div v-pre>

# organoid_regulomes

- **原始分类文件夹**:: cancer_2023, brain_diseases_2023
- **GitHub 链接**:: [quadbio/organoid_regulomes](https://github.com/quadbio/organoid_regulomes)
- **本地源码路径**:: [cancer_2023/organoid_regulomes](https://github.com/quadbio/organoid_regulomes/blob/main/) and [brain_diseases_2023/organoid_regulomes](https://github.com/quadbio/organoid_regulomes/blob/main/)

---

## 📝 简介
The repo is structured as follows: * `integration/` contains scripts and functions used to integrate the RNA-seq and ATAC-seq data - `get_bipartite_matches.py` finds matching cells given a h5ad file with a common embedding (in our case CCA) between the datasets.

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R, Python 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: ggplot2, matplotlib, seaborn

## 📂 核心代码文件链接
- [utils/scripts/markers.R](https://github.com/quadbio/organoid_regulomes/blob/main/utils/scripts/markers.R)

</div>

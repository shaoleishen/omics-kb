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
omics: single-cell-rna-seq
packages:
- Seurat
- Scanpy
tags:
- single-cell-rna-seq
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

- **Original Category**:: cancer_2023, brain_diseases_2023
- **GitHub Link**:: [quadbio/organoid_regulomes](https://github.com/quadbio/organoid_regulomes)
- **Source Code**:: [cancer_2023/organoid_regulomes](https://github.com/quadbio/organoid_regulomes/blob/main/) and [brain_diseases_2023/organoid_regulomes](https://github.com/quadbio/organoid_regulomes/blob/main/)

---

## 📝 Overview
The repo is structured as follows: * `integration/` contains scripts and functions used to integrate the RNA-seq and ATAC-seq data - `get_bipartite_matches.py` finds matching cells given a h5ad file with a common embedding (in our case CCA) between the datasets.

## ⚙️ Analysis Modules
- **Import & Preprocessing**:: 检测到 R, Python 脚本文件。
- **Quality Control**:: No explicit QC filtering logic detected.
- **Clustering & Dim. Reduction**:: Supported
- **Cell Type Annotation**:: Supported
- **Trajectory Analysis**:: Supported

## 🎨 Visualization
- **Plotting Engine**:: ggplot2, matplotlib, seaborn

## 📂 Key Code Files
- [utils/scripts/markers.R](https://github.com/quadbio/organoid_regulomes/blob/main/utils/scripts/markers.R)

</div>

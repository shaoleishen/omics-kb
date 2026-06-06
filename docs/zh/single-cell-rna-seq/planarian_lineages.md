---
github_url: https://github.com/rajewsky-lab/planarian_lineages
language:
- R
- Python
modules:
- Clustering
- Annotation
- Trajectory
name: planarian_lineages
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
- matplotlib
- seaborn
---

<div v-pre>

# planarian_lineages

- **原始分类文件夹**:: cancer_2023, developmental_atlases_2023
- **GitHub 链接**:: [rajewsky-lab/planarian_lineages](https://github.com/rajewsky-lab/planarian_lineages)
- **本地源码路径**:: [cancer_2023/planarian_lineages](https://github.com/rajewsky-lab/planarian_lineages/blob/main/) and [developmental_atlases_2023/planarian_lineages](https://github.com/rajewsky-lab/planarian_lineages/blob/main/)

---

## 📝 简介
The following notebooks provide the analyses based on *partition-based graph abstraction (PAGA)* [(Wolf *et al.*, 2017)](https://doi.org/10.1101/208819): - [*planaria*](https://nbviewer.jupyter.org/github/rajewsky-lab/planarian_lineages/blob/master/paga/planaria.ipynb): inferring the lineage tree from the topology of the Planarian cell atlas - [*preprocessing*](https://nbviewer.jupyter.org/github/rajewsky-lab/planarian_lineages/blob/master/paga/preprocessing.ipynb): same as *planaria*, but including all preprocessing steps

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R, Python 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [paga/planaria.ipynb](https://github.com/rajewsky-lab/planarian_lineages/blob/main/paga/planaria.ipynb)

</div>

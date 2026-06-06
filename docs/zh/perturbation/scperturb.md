---
github_url: https://github.com/sanderlab/scPerturb
language:
- R
- Python
modules:
- QC
- Clustering
- Annotation
- Trajectory
name: scPerturb
omics: Perturbation
packages:
- Seurat
- Scanpy
tags:
- Perturbation
- R
- Python
- Seurat
- Scanpy
- QC
- Clustering
- Annotation
- Trajectory
visualizations:
- ggplot2
- matplotlib
- seaborn
---

<div v-pre>

# scPerturb

- **原始分类文件夹**:: perturbation_2023
- **GitHub 链接**:: [sanderlab/scPerturb](https://github.com/sanderlab/scPerturb)
- **本地源码路径**:: [scPerturb](https://github.com/sanderlab/scPerturb/blob/main/)

---

## 📝 简介
For the publication see: [Peidli, S., Green, T.D., et al. Nature Methods (2024)](https://www.nature.com/articles/s41592-023-02144-y). The datasets are available to download on [scperturb.org](https://scperturb.org/) (where you can also find an [interactive table](http://projects.sanderlab.org/scperturb/datavzrd/scPerturb_vzrd_v1/dataset_info/index_1.html) of all included datasets). The latest versions are available in full on Zenodo, depending on the modality you are interested in: - [RNA data](https://zenodo.org/records/13350497)

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R, Python 脚本文件。
- **QC 质控**:: 支持
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: ggplot2, matplotlib, seaborn

## 📂 核心代码文件链接
- [revision/snakemake/scripts/snake_plot_umap.py](https://github.com/sanderlab/scPerturb/blob/main/revision/snakemake/scripts/snake_plot_umap.py)

</div>

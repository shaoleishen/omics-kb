---
github_url: https://github.com/theislab/sc-pert
language:
- Python
modules:
- QC
- Clustering
- Annotation
- Trajectory
name: sc-pert
omics: Perturbation
packages:
- Scanpy
tags:
- Perturbation
- Python
- Scanpy
- QC
- Clustering
- Annotation
- Trajectory
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# sc-pert

- **原始分类文件夹**:: perturbation_2023
- **GitHub 链接**:: [theislab/sc-pert](https://github.com/theislab/sc-pert)
- **本地源码路径**:: [sc-pert](https://github.com/theislab/sc-pert/blob/main/)

---

## 📝 简介
*This repository provides a community-maintained summary of models and datasets. It was initially curated for [(Cell Systems, 2021)](https://doi.org/10.1016/j.cels.2021.05.016).* There are various resources for evaluation of single cell perturbation models. We discuss five tasks in the publication which can be supported by the following publicly available annotations: - [GDSC](https://www.cancerrxgene.org/downloads/bulk_download) provides a collection of cell viability measurements for many compounds and cell lines. We provide a [code snippet](https://github.com/theislab/sc-pert/blob/main/resources.py#L4) to conveniently load GDSC-provided z-score compound response rankings per cell line.

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 Python 脚本文件。
- **QC 质控**:: 支持
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [datasets/Srivatsan_2019_sciplex2_curation.ipynb](https://github.com/theislab/sc-pert/blob/main/datasets/Srivatsan_2019_sciplex2_curation.ipynb)

</div>

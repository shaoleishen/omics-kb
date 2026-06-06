---
github_url: https://github.com/broadinstitute/Tangram
language:
- Python
modules:
- Annotation
name: Tangram
omics: Spatial_Omics
packages:
- Scanpy
tags:
- Spatial_Omics
- Python
- Scanpy
- Annotation
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# Tangram

- **原始分类文件夹**:: spatial_applications_2023
- **GitHub 链接**:: [broadinstitute/Tangram](https://github.com/broadinstitute/Tangram)
- **本地源码路径**:: [Tangram](https://github.com/broadinstitute/Tangram/blob/main/)

---

## 📝 简介
&lt;img src="https://raw.githubusercontent.com/broadinstitute/Tangram/master/figures/tangram_large.png" width="400"&gt; [![PyPI version](https://badge.fury.io/py/tangram-sc.svg)](https://badge.fury.io/py/tangram-sc) Tangram is a Python package, written in [PyTorch](https://pytorch.org/) and based on [scanpy](https://scanpy.readthedocs.io/en/stable/), for mapping single-cell (or single-nucleus) gene expression data onto spatial gene expression data. The single-cell dataset and the spatial dataset should be collected from the same anatomical region/tissue type, ideally from a biological replicate, and need to share a set of genes. Tangram aligns the single-cell data in space by fitting gene expression on the shared genes. The best way to familiarize yourself with Tangram is to check out [our tutorial](https://github.com/broadinstitute/Tangram/blob/master/tutorial_tangram_with_squidpy.ipynb) and [our documentation](https://tangram-sc.readthedocs.io/en/latest/index.html). [![colab tutorial](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jP3M7wu-YJrtDzvHSdK5HIdee0SNVs0b?usp=sharing)\

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 Python 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 未检测到降维与聚类逻辑。
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 未检测到拟时序分析逻辑。

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [setup.py](https://github.com/broadinstitute/Tangram/blob/main/setup.py)

</div>

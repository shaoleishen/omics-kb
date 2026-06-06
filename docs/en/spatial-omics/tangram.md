---
github_url: https://github.com/broadinstitute/Tangram
language:
- Python
modules:
- Annotation
name: Tangram
omics: spatial-omics
packages:
- Scanpy
tags:
- spatial-omics
- Python
- Scanpy
- Annotation
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# Tangram

- **Original Category**:: spatial_applications_2023
- **GitHub Link**:: [broadinstitute/Tangram](https://github.com/broadinstitute/Tangram)
- **Source Code**:: [Tangram](https://github.com/broadinstitute/Tangram/blob/main/)

---

## 📝 Overview
&lt;img src="https://raw.githubusercontent.com/broadinstitute/Tangram/master/figures/tangram_large.png" width="400"&gt; [![PyPI version](https://badge.fury.io/py/tangram-sc.svg)](https://badge.fury.io/py/tangram-sc) Tangram is a Python package, written in [PyTorch](https://pytorch.org/) and based on [scanpy](https://scanpy.readthedocs.io/en/stable/), for mapping single-cell (or single-nucleus) gene expression data onto spatial gene expression data. The single-cell dataset and the spatial dataset should be collected from the same anatomical region/tissue type, ideally from a biological replicate, and need to share a set of genes. Tangram aligns the single-cell data in space by fitting gene expression on the shared genes. The best way to familiarize yourself with Tangram is to check out [our tutorial](https://github.com/broadinstitute/Tangram/blob/master/tutorial_tangram_with_squidpy.ipynb) and [our documentation](https://tangram-sc.readthedocs.io/en/latest/index.html). [![colab tutorial](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jP3M7wu-YJrtDzvHSdK5HIdee0SNVs0b?usp=sharing)\

## ⚙️ Analysis Modules
- **Import & Preprocessing**:: Python scripts detected.
- **Quality Control**:: No explicit QC filtering logic detected.
- **Clustering & Dim. Reduction**:: Not detected降维与聚类逻辑。
- **Cell Type Annotation**:: Supported
- **Trajectory Analysis**:: Not detected拟时序分析逻辑。

## 🎨 Visualization
- **Plotting Engine**:: matplotlib, seaborn

## 📂 Key Code Files
- [setup.py](https://github.com/broadinstitute/Tangram/blob/main/setup.py)

</div>

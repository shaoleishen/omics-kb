---
github_url: https://github.com/schulter/EMOGI
language:
- R
- Python
modules:
- Annotation
- Trajectory
name: EMOGI
omics: Multi_omics
packages: null
tags:
- Multi_omics
- R
- Python
- Annotation
- Trajectory
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# EMOGI

- **原始分类文件夹**:: multi_omics_disease_2023
- **GitHub 链接**:: [schulter/EMOGI](https://github.com/schulter/EMOGI)
- **本地源码路径**:: [EMOGI](https://github.com/schulter/EMOGI/blob/main/)

---

## 📝 简介
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4452728.svg)](https://doi.org/10.5281/zenodo.4452728) [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) This project predicts cancer genes based on multi-omics feature vectors and protein-protein interactions. Each gene is a data point/node and semi-supervised graph convolutional networks are used for classifying cancer genes. The results surrounding the analysis were published in Nature Machine Intelligence and can be accessed [here](https://www.nature.com/articles/s42256-021-00325-y).

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R, Python 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 未检测到降维与聚类逻辑。
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [network_preprocessing/preprocessing_IRefIndex.ipynb](https://github.com/schulter/EMOGI/blob/main/network_preprocessing/preprocessing_IRefIndex.ipynb)

</div>

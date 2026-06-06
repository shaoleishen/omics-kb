---
github_url: https://github.com/clinicalml/sc-foundation-eval
language:
- Python
modules:
- QC
- Annotation
- Trajectory
name: sc-foundation-eval
omics: Multi_omics
packages:
- Scanpy
tags:
- Multi_omics
- Python
- Scanpy
- QC
- Annotation
- Trajectory
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# sc-foundation-eval

- **原始分类文件夹**:: foundation_model_applications_2023
- **GitHub 链接**:: [clinicalml/sc-foundation-eval](https://github.com/clinicalml/sc-foundation-eval)
- **本地源码路径**:: [sc-foundation-eval](https://github.com/clinicalml/sc-foundation-eval/blob/main/)

---

## 📝 简介
Code for evaluating single cell foundation models scBERT and scGPT. This code was used for the analysis presented in A Deep Dive into Single-Cell RNA Sequencing Foundation Models, bioRxiv https://doi.org/10.1101/2023.10.19.563100. The repo is organized by model. Below are descriptions of the scripts and analysis code included for each: * [performer_pytorch/](scBERT/performer_pytorch) contains the code for the scBERT model

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 Python 脚本文件。
- **QC 质控**:: 支持
- **聚类与降维**:: 未检测到降维与聚类逻辑。
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [scBERT/performer_pytorch/reversible.py](https://github.com/clinicalml/sc-foundation-eval/blob/main/scBERT/performer_pytorch/reversible.py)

</div>

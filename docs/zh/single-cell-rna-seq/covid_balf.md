---
github_url: https://github.com/zhangzlab/covid_balf
language:
- R
modules:
- QC
- Clustering
- Annotation
name: covid_balf
omics: Single_Cell_RNA_seq
packages:
- Seurat
tags:
- Single_Cell_RNA_seq
- R
- Seurat
- QC
- Clustering
- Annotation
visualizations:
- ggplot2
---

<div v-pre>

# covid_balf

- **原始分类文件夹**:: cancer_2023, immune_diseases_2023
- **GitHub 链接**:: [zhangzlab/covid_balf](https://github.com/zhangzlab/covid_balf)
- **本地源码路径**:: [cancer_2023/covid_balf](https://github.com/zhangzlab/covid_balf/blob/main/) and [immune_diseases_2023/covid_balf](https://github.com/zhangzlab/covid_balf/blob/main/)

---

## 📝 简介
R script for the covid balf data analysis. (Liao M. et al, Single-cell landscape of bronchoalveolar immune cells in patients with COVID-19, Nature Medicine, 2020. https://www.nature.com/articles/s41591-020-0901-9) Integration of all samples with seurat. Integration of macrophage data with seurat.

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R 脚本文件。
- **QC 质控**:: 支持
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 未检测到拟时序分析逻辑。

## 🎨 可视化实现
- **绘图引擎**:: ggplot2

## 📂 核心代码文件链接
- [tcr_fig.R](https://github.com/zhangzlab/covid_balf/blob/main/tcr_fig.R)

</div>

---
github_url: https://github.com/CIMA-Project/CIMA
language:
- R
- Python
modules:
- QC
- Clustering
- Annotation
- Trajectory
name: CIMA
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

# CIMA

- **原始分类文件夹**:: cancer_2023, immune_diseases_2023
- **GitHub 链接**:: [CIMA-Project/CIMA](https://github.com/CIMA-Project/CIMA)
- **本地源码路径**:: [cancer_2023/CIMA](https://github.com/CIMA-Project/CIMA/blob/main/) and [immune_diseases_2023/CIMA](https://github.com/CIMA-Project/CIMA/blob/main/)

---

## 📝 简介
Chinese Immune Multi-Omics Atlas (CIMA), characterizing molecular variations linked to sex, age, and genetics through multi-omics analysis of &gt; 10 million immune cells from 428 adults. CIMA established an enhancer-driven gene regulatory network comprising 237 robust regulons, identified 9,600 cis-expression quantitative trait loci (eQTLs) and 52,361 chromatin accessibility QTLs (caQTLs) at cell-type resolution, and revealed pleiotropic associations among immune-related disease risk loci, eQTLs, and caQTLs. Furthermore, the novel CIMA-CLM model predicts chromatin accessibility and noncoding variant impacts from chromatin sequences and gene expression. &lt;img width="953" alt="截屏2025-04-21 22 24 44" src="https://github.com/user-attachments/assets/0a8affd5-fa65-4ac6-bbef-380b5b1b5e90" /&gt; &lt;img width="4790" height="6150" alt="CIMA-sFigure1_20250805-2116" src="https://github.com/user-attachments/assets/25835e11-52e4-4c82-8b50-9dfe37e18d97" /&gt;

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R, Python 脚本文件。
- **QC 质控**:: 支持
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: ggplot2, matplotlib, seaborn

## 📂 核心代码文件链接
- [CIMA-CLM/omiclm/omic_config/_training_config.py](https://github.com/CIMA-Project/CIMA/blob/main/CIMA-CLM/omiclm/omic_config/_training_config.py)

</div>

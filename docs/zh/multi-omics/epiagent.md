---
github_url: https://github.com/xy-chen16/EpiAgent
language:
- Python
modules:
- Clustering
- Annotation
- Trajectory
name: EpiAgent
omics: Multi_omics
packages:
- Scanpy
tags:
- Multi_omics
- Python
- Scanpy
- Clustering
- Annotation
- Trajectory
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# EpiAgent

- **原始分类文件夹**:: foundation_model_applications_2023
- **GitHub 链接**:: [xy-chen16/EpiAgent](https://github.com/xy-chen16/EpiAgent)
- **本地源码路径**:: [EpiAgent](https://github.com/xy-chen16/EpiAgent/blob/main/)

---

## 📝 简介
Although single-cell assay for transposase-accessible chromatin using sequencing (scATAC-seq) enables the exploration of the epigenomic landscape that governs transcription at the cellular level, the complicated characteristics of the sequencing data and the broad scope of downstream tasks mean that a sophisticated and versatile computational method is urgently needed. Here, we introduce EpiAgent, a foundation model pretrained on our manually curated large-scale [Human-scATAC-Corpus](https://health.tsinghua.edu.cn/human-scatac-corpus/index.php). EpiAgent encodes chromatin accessibility patterns of cells as concise ‘cell sentences’ and captures cellular heterogeneity behind regulatory networks via bidirectional attention. Comprehensive benchmarks show that EpiAgent excels in typical downstream tasks, including unsupervised feature extraction, supervised cell type annotation and data imputation. By incorporating external embeddings, EpiAgent enables effective cellular response prediction for both out-of-sample stimulated and unseen genetic perturbations, reference data integration and query data mapping. Through in silico knockout of cis-regulatory elements, EpiAgent demonstrates the potential to model cell state changes. EpiAgent is further extended to directly annotate cell types in a zero-shot manner. &lt;p align="center"&gt; &lt;img src="https://github.com/xy-chen16/EpiAgent/blob/main/inst/model.png" width="700" height="385" alt="image"&gt;

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 Python 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [setup.py](https://github.com/xy-chen16/EpiAgent/blob/main/setup.py)

</div>

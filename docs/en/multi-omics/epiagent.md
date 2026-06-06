---
github_url: https://github.com/xy-chen16/EpiAgent
language:
- Python
modules:
- Clustering
- Annotation
- Trajectory
name: EpiAgent
omics: multi-omics
packages:
- Scanpy
tags:
- multi-omics
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

- **Original Category**:: foundation_model_applications_2023
- **GitHub Link**:: [xy-chen16/EpiAgent](https://github.com/xy-chen16/EpiAgent)
- **Source Code**:: [EpiAgent](https://github.com/xy-chen16/EpiAgent/blob/main/)

---

## 📝 Overview
Although single-cell assay for transposase-accessible chromatin using sequencing (scATAC-seq) enables the exploration of the epigenomic landscape that governs transcription at the cellular level, the complicated characteristics of the sequencing data and the broad scope of downstream tasks mean that a sophisticated and versatile computational method is urgently needed. Here, we introduce EpiAgent, a foundation model pretrained on our manually curated large-scale [Human-scATAC-Corpus](https://health.tsinghua.edu.cn/human-scatac-corpus/index.php). EpiAgent encodes chromatin accessibility patterns of cells as concise ‘cell sentences’ and captures cellular heterogeneity behind regulatory networks via bidirectional attention. Comprehensive benchmarks show that EpiAgent excels in typical downstream tasks, including unsupervised feature extraction, supervised cell type annotation and data imputation. By incorporating external embeddings, EpiAgent enables effective cellular response prediction for both out-of-sample stimulated and unseen genetic perturbations, reference data integration and query data mapping. Through in silico knockout of cis-regulatory elements, EpiAgent demonstrates the potential to model cell state changes. EpiAgent is further extended to directly annotate cell types in a zero-shot manner. &lt;p align="center"&gt; &lt;img src="https://github.com/xy-chen16/EpiAgent/blob/main/inst/model.png" width="700" height="385" alt="image"&gt;

## ⚙️ Analysis Modules
- **Import & Preprocessing**:: Python scripts detected.
- **Quality Control**:: No explicit QC filtering logic detected.
- **Clustering & Dim. Reduction**:: Supported
- **Cell Type Annotation**:: Supported
- **Trajectory Analysis**:: Supported

## 🎨 Visualization
- **Plotting Engine**:: matplotlib, seaborn

## 📂 Key Code Files
- [setup.py](https://github.com/xy-chen16/EpiAgent/blob/main/setup.py)

</div>

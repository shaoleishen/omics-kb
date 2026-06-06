---
github_url: https://github.com/JinmiaoChenLab/SpatialGlue
language:
- Python
modules:
- Clustering
- Trajectory
name: SpatialGlue
omics: multi-omics
packages:
- Scanpy
tags:
- multi-omics
- Python
- Scanpy
- Clustering
- Trajectory
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# SpatialGlue

- **Original Category**:: multi_omics_disease_2023
- **GitHub Link**:: [JinmiaoChenLab/SpatialGlue](https://github.com/JinmiaoChenLab/SpatialGlue)
- **Source Code**:: [SpatialGlue](https://github.com/JinmiaoChenLab/SpatialGlue/blob/main/)

---

## 📝 Overview
This repository contains SpatialGlue script and jupyter notebooks essential for reproducing the benchmarking outcomes shown in the paper. We provide experimental data in each case with details available within the notebook. All experiment data is reproducible through the provided scripts of various methods (https://github.com/JinmiaoChenLab/SpatialGlue_notebook). Some notebooks will be uploaded shortly to complement the available resources. [![DOI](https://zenodo.org/badge/631763850.svg)](https://zenodo.org/badge/latestdoi/631763850) Integration of multiple data modalities in a spatially informed manner remains an unmet need for exploiting spatial multi-omics data. Here, we introduce SpatialGlue, a novel graph neural network with dual-attention mechanism, to decipher spatial domains by intra-omics integration of spatial location and omics measurement followed by cross-omics integration. We demonstrate that SpatialGlue can more accurately resolve spatial domains at a higher resolution across different tissue types and technology platforms, to enable biological insights into cross-modality spatial correlations. SpatialGlue is computation resource efficient and can be applied for data from various spatial multi-omics technological platforms, including Spatial-epigenome-transcriptome, Stereo-CITE-seq, SPOTS, and 10x Visium. Next, we will extend SpatialGlue to more platforms, such as 10x Genomics Xenium and Nanostring CosMx.

## ⚙️ Analysis Modules
- **Import & Preprocessing**:: Python scripts detected.
- **Quality Control**:: No explicit QC filtering logic detected.
- **Clustering & Dim. Reduction**:: Supported
- **Cell Type Annotation**:: Not detected自动化细胞标注逻辑。
- **Trajectory Analysis**:: Supported

## 🎨 Visualization
- **Plotting Engine**:: matplotlib, seaborn

## 📂 Key Code Files
- [setup.py](https://github.com/JinmiaoChenLab/SpatialGlue/blob/main/setup.py)

</div>

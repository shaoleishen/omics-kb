---
github_url: https://github.com/krasnowlab/HLCA
language:
- R
modules:
- QC
- Clustering
- Annotation
name: HLCA
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

# HLCA

- **原始分类文件夹**:: cancer_2023, developmental_atlases_2023
- **GitHub 链接**:: [krasnowlab/HLCA](https://github.com/krasnowlab/HLCA)
- **本地源码路径**:: [cancer_2023/HLCA](https://github.com/krasnowlab/HLCA/blob/main/) and [developmental_atlases_2023/HLCA](https://github.com/krasnowlab/HLCA/blob/main/)

---

## 📝 简介
Although single cell RNA sequencing studies have begun providing compendia of cell expression profiles, it has proven more difficult to systematically identify and localize all molecular cell types in individual organs to create a full molecular cell atlas. From droplet- and plate-based single cell RNA sequencing applied to ~75,000 human lung and blood cells, combined with a multi-pronged cell annotation approach that includes extensive tissue localization, we have defined the gene expression profiles and anatomical locations of 58 cell populations in the human lung, including 41 of 45 previously known cell types or subtypes and 14 new ones. Learn more in our [manuscript](https://www.biorxiv.org/content/10.1101/742320v2) or explore the data in your browser with [cellxgene](http://hlca.ds.czbiohub.org). These R markdown notebooks import patient-specific gene count/UMI tables (SS2/10x) with [Seurat](https://satijalab.org/seurat/), seperate the cells by tissue compartment, iteratively subclsuter them, and then assign each biologically meaningful cluster an identity based on canonical marker genes, novel bulk RNAseq markers (immune cells), tissue location, and biochemical function. Note: The specific version of Seurat used (as well as its dependencies) can produce slightly different clustering results. Early steps in these notebooks remove cells from patient-matched diseased regions of the lung, which are not yet released. These notebooks import annotated, patient-specific Seurat objects (see Data availability below) from the annotation notebooks and merges them for downstream analyses. They explore the biochemical functions of lung cell types and the cell-selective transcription factors and optimal markers for making and monitoring them; define the cell targets of circulating hormones and predicts local signaling interactions including sources and targets of chemokines in immune cell trafficking and expression changes on lung homing; and identify the cell types directly affected by lung disease genes. They also compare human and mouse cell types to identify cell types whose expression profiles have been substantially altered by evolution, revealing extensive plasticity of cell-type-specific gene expression. These notebooks output the Figures and Tables used in the manuscript.

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 R 脚本文件。
- **QC 质控**:: 支持
- **聚类与降维**:: 支持
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 未检测到拟时序分析逻辑。

## 🎨 可视化实现
- **绘图引擎**:: ggplot2

## 📂 核心代码文件链接
- [Annotation Patient 3/boilerplate.R](https://github.com/krasnowlab/HLCA/blob/main/Annotation%20Patient%203/boilerplate.R)

</div>

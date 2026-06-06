---
github_url: https://github.com/snap-stanford/GEARS
language:
- Python
modules:
- Annotation
- Trajectory
name: GEARS
omics: Perturbation
packages:
- Scanpy
tags:
- Perturbation
- Python
- Scanpy
- Annotation
- Trajectory
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# GEARS

- **原始分类文件夹**:: perturbation_2023
- **GitHub 链接**:: [snap-stanford/GEARS](https://github.com/snap-stanford/GEARS)
- **本地源码路径**:: [GEARS](https://github.com/snap-stanford/GEARS/blob/main/)

---

## 📝 简介
This repository hosts the official implementation of GEARS, a method that can predict transcriptional response to both single and multi-gene perturbations using single-cell RNA-sequencing data from perturbational screens. &lt;p align="center"&gt;&lt;img src="https://github.com/snap-stanford/GEARS/blob/master/img/gears.png" alt="gears" width="900px" /&gt;&lt;/p&gt; Install [PyG](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html), and then do `pip install cell-gears`.

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 Python 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 未检测到降维与聚类逻辑。
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [setup.py](https://github.com/snap-stanford/GEARS/blob/main/setup.py)

</div>

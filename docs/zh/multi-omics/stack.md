---
github_url: https://github.com/ArcInstitute/stack
language:
- Python
modules:
- Annotation
- Trajectory
name: stack
omics: Multi_omics
packages:
- Scanpy
tags:
- Multi_omics
- Python
- Scanpy
- Annotation
- Trajectory
visualizations:
- matplotlib
- seaborn
---

<div v-pre>

# stack

- **原始分类文件夹**:: foundation_model_applications_2023
- **GitHub 链接**:: [ArcInstitute/stack](https://github.com/ArcInstitute/stack)
- **本地源码路径**:: [stack](https://github.com/ArcInstitute/stack/blob/main/)

---

## 📝 简介
Stack is a large-scale encoder-decoder foundation model trained on 150 million uniformly-preprocessed single cells. It introduces a novel tabular attention architecture that enables both intra- and inter-cellular information flow, setting cell-by-gene matrix chunks as the basic input data unit. Through in-context learning, Stack offers substantial performance improvements in generalizing biological effects and enables generation of unseen cell profiles in novel contexts. Stack is primarily developed and tested on Linux systems. - **Operating system**: Tested on Ubuntu 22.04.5 LTS with Linux kernel 5.15.0-164-generic on x86_64

## ⚙️ 分析模块支持
- **导入与预处理**:: 检测到 Python 脚本文件。
- **QC 质控**:: 未检测到显式 QC 过滤逻辑。
- **聚类与降维**:: 未检测到降维与聚类逻辑。
- **细胞类型鉴定与注释**:: 支持
- **拟时序与轨迹分析**:: 支持

## 🎨 可视化实现
- **绘图引擎**:: matplotlib, seaborn

## 📂 核心代码文件链接
- [setup.py](https://github.com/ArcInstitute/stack/blob/main/setup.py)

</div>

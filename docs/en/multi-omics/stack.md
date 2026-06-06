---
github_url: https://github.com/ArcInstitute/stack
language:
- Python
modules:
- Annotation
- Trajectory
name: stack
omics: multi-omics
packages:
- Scanpy
tags:
- multi-omics
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

- **Original Category**:: foundation_model_applications_2023
- **GitHub Link**:: [ArcInstitute/stack](https://github.com/ArcInstitute/stack)
- **Source Code**:: [stack](https://github.com/ArcInstitute/stack/blob/main/)

---

## 📝 Overview
Stack is a large-scale encoder-decoder foundation model trained on 150 million uniformly-preprocessed single cells. It introduces a novel tabular attention architecture that enables both intra- and inter-cellular information flow, setting cell-by-gene matrix chunks as the basic input data unit. Through in-context learning, Stack offers substantial performance improvements in generalizing biological effects and enables generation of unseen cell profiles in novel contexts. Stack is primarily developed and tested on Linux systems. - **Operating system**: Tested on Ubuntu 22.04.5 LTS with Linux kernel 5.15.0-164-generic on x86_64

## ⚙️ Analysis Modules
- **Import & Preprocessing**:: Python scripts detected.
- **Quality Control**:: No explicit QC filtering logic detected.
- **Clustering & Dim. Reduction**:: Not detected降维与聚类逻辑。
- **Cell Type Annotation**:: Supported
- **Trajectory Analysis**:: Supported

## 🎨 Visualization
- **Plotting Engine**:: matplotlib, seaborn

## 📂 Key Code Files
- [setup.py](https://github.com/ArcInstitute/stack/blob/main/setup.py)

</div>

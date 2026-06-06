# 🧬 Omics Code Knowledge Base

> A curated knowledge base indexing and analyzing **87 high-impact omics analysis code repositories** from Nature, Cell, and Science publications.

🌐 **Live Site:** [https://bioshen.github.io/omics-kb/zh/](https://bioshen.github.io/omics-kb/zh/) (Chinese) or [https://bioshen.github.io/omics-kb/en/](https://bioshen.github.io/omics-kb/en/) (English)

---

## 📂 Categories

| Category | Count | Description |
|----------|-------|-------------|
| 💻 Single-cell RNA-seq | 28 | Transcriptomics analysis tools & pipelines |
| 🧬 Multi-omics | 23 | Data integration & foundation models |
| 🗺️ Spatial Omics | 11 | Spatial transcriptomics tools |
| ⚡ Perturbation | 12 | Gene perturbation prediction |

## 🔍 Features

- **Dual-language** (中文/English) browsing
- **Full-text search** across all 74 tool notes
- **Analysis Module index** — QC, clustering, annotation, trajectory, etc.
- **Visualization Method index** — by plotting engine (matplotlib, ggplot2, seaborn)
- **Dark mode** support
- **Mobile-responsive**

## 🛠 Project Structure

```
omics-kb/
├── docs/
│   ├── .vitepress/           # VitePress configurations and custom theme
│   ├── zh/                   # Chinese documentation notes
│   └── en/                   # Auto-translated English documentation notes
├── scripts/
│   ├── convert_obsidian.py   # Obsidian -> VitePress converter
│   ├── translate_notes.py    # Chinese -> English field translator
│   └── gen_sidebar.py        # Automatic sidebar generator from YAML frontmatter
└── .github/
    └── workflows/
        └── deploy.yml        # GitHub Actions CI/CD to deploy to GitHub Pages
```

## 🚀 Development

### Installation

```bash
npm install
```

### Dev Server

```bash
npm run docs:dev
```

### Build

```bash
npm run docs:build
```

## 📜 License

MIT

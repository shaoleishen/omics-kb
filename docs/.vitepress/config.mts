import { defineConfig } from 'vitepress'
import sidebarData from './sidebar.json'

export default defineConfig({
  title: 'Omics Code KB',
  description: 'A curated knowledge base of high-impact omics analysis code from Nature/Cell/Science publications',
  base: '/omics-kb/',
  ignoreDeadLinks: true, // Bypass build failures due to external or relative dead links in code bases

  head: [
    ['meta', { name: 'theme-color', content: '#6366f1' }],
    ['meta', { name: 'author', content: 'bioshen' }],
  ],

  locales: {
    zh: {
      label: '中文',
      lang: 'zh-CN',
      link: '/zh/',
      themeConfig: {
        nav: [
          { text: '首页', link: '/zh/' },
          { text: '单细胞RNA-seq', link: '/zh/single-cell-rna-seq/' },
          { text: '多组学', link: '/zh/multi-omics/' },
          { text: '空间组学', link: '/zh/spatial-omics/' },
          { text: '扰动分析', link: '/zh/perturbation/' },
          {
            text: '📑 索引',
            items: [
              { text: '⚙️ 分析模块', link: '/zh/guide/analysis-modules' },
              { text: '🎨 可视化方法', link: '/zh/guide/visualization' },
            ],
          },
        ],
        sidebar: sidebarData.zh as any,
        outline: { label: '目录' },
        docFooter: { prev: '上一篇', next: '下一篇' },
        lastUpdated: { text: '最后更新' },
      },
    },
    en: {
      label: 'English',
      lang: 'en',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'scRNA-seq', link: '/en/single-cell-rna-seq/' },
          { text: 'Multi-omics', link: '/en/multi-omics/' },
          { text: 'Spatial Omics', link: '/en/spatial-omics/' },
          { text: 'Perturbation', link: '/en/perturbation/' },
          {
            text: '📑 Index',
            items: [
              { text: '⚙️ Analysis Modules', link: '/en/guide/analysis-modules' },
              { text: '🎨 Visualization', link: '/en/guide/visualization' },
            ],
          },
        ],
        sidebar: sidebarData.en as any,
      },
    },
  },

  themeConfig: {
    search: {
      provider: 'local',
      options: {
        locales: {
          zh: {
            translations: {
              button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
              modal: {
                noResultsText: '没有找到结果',
                resetButtonTitle: '清除搜索',
                footer: { selectText: '选择', navigateText: '导航', closeText: '关闭' },
              },
            },
          },
        },
      },
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/bioshen/omics-kb' },
    ],
  },
})

# Pico CSS 中文文档站

Pico CSS 官方文档（https://picocss.com/docs）的中文翻译站。站点本身就用 Pico CSS 构建——框架即设计语言，主题色为官方默认 Indigo，明暗双模式。

> 本文件是项目与部署说明；`README.md` 保持 Pico 官方中文 README 原样。

## 技术栈

- [Astro](https://astro.build) 7（静态输出）+ [MDX](https://mdxjs.com)（@astrojs/mdx 8）
- [Pico CSS](https://picocss.com) 2.1.1（npm 包引入 `pico.min.css` + `pico.colors.min.css`）
- [Bun](https://bun.sh) 作为包管理器与脚本运行时
- Shiki 双主题代码高亮（vitesse-light / vitesse-dark，`defaultColor: false`，CSS 变量按 `html[data-theme]` 切换）

## 常用命令

```bash
bun install        # 安装依赖
bun run dev        # 开发服务器
bun run build      # 构建到 dist/（纯静态）
bun run preview    # 预览构建产物
bun run check      # astro check 类型检查
```

## 目录结构

```
src/
├─ content.config.ts        # docs 集合（glob loader，src/content/docs/**/*.mdx）
├─ content/docs/            # 39 页中文文档（MDX，slug 与官方 URL 一一对应）
│  └─ forms/                # 表单子页（input/textarea/select/checkboxes/radios/switch/range）
├─ data/docs-nav.ts         # 侧栏导航结构（7 组 39 项，含「新」标记）+ 上/下篇序列
├─ layouts/
│  ├─ Base.astro            # HTML 壳、主题 boot 脚本（localStorage + 跟随系统）、明暗切换
│  └─ Docs.astro            # 文档三栏壳：侧栏 / 正文 / 本页目录（scroll-spy）+ 页脚
├─ components/
│  ├─ SiteHeader.astro      # 顶栏（官方 logo 明暗双版本、版本徽章、GitHub、主题切换）
│  ├─ Sidebar.astro         # 分组侧栏（当前页所在组自动展开）
│  ├─ Ex.astro              # 示例组件：实时渲染 demo + 「查看代码」折叠（Shiki 高亮）
│  ├─ Raw.astro             # 原样 HTML 块（色板卡、色板选择器等专有组件 demo）
│  └─ DocPager.astro        # 上一篇/下一篇
├─ pages/
│  ├─ index.astro           # 营销首页（hero + 12 行起步 + 特性 + 20 色色带）
│  └─ docs/[...slug].astro  # 全部文档页路由（quickstart 映射到 /docs/）
└─ styles/global.css        # Pico 引入 + 中文字体回退 + 布局/示例/色板等站点样式
.probe/                     # 内容管线（不参与构建）
├─ fetch.py                 # 抓取官方 39 页 SSR HTML → en/
├─ extract.py               # HTML → 结构化块 JSON → en_src/
├─ TRANSLATION-GUIDE.md     # 翻译规范（块类型、组件用法、文风红线、自检清单）
└─ en_src/*.json            # 英文源（翻译与后续更新的对照基准）
.shots/                     # 无头验收脚本（shot / audit / contrast / all），产物不入库
```

## URL 约定

与官方一致：`/docs/`（快速开始）、`/docs/forms/input/`、`/docs/modal/` 等；锚点 id 保留官方英文 slug（保护既有深链与交叉引用）。

## 更新翻译的流程

1. `python .probe/fetch.py` 重新抓取（增量：已存在则跳过，删对应 `en/*.html` 可强制重抓）
2. `python .probe/extract.py` 重新生成 `en_src/*.json`
3. 对照 JSON 与 `TRANSLATION-GUIDE.md` 更新对应 `src/content/docs/*.mdx`
4. `bun run build` + `.shots/` 内脚本验收（链接/锚点/重复 id/对比度）

## 设计决策

- **框架即皮肤**：不引入第二套样式体系，站点全部版式由 Pico 语义元素 + 极少量自定义 CSS 构成
- **主题色**：官方默认 Indigo（`pico.min.css` 原样），不覆盖 `--pico-primary`
- **明暗模式**：`html[data-theme]` 显式钉死（boot 脚本首帧前写入，防闪烁）；用户未手动选择时跟随系统
- **示例呈现**：官方「demo + 源码」双视图合并为单组件（`<Ex>`），demo 实时渲染、源码折叠可展开并复制友好
- **安装呈现（首页）**：CDN / NPM / Sass 三页签单窗口（原生 `tablist`，方向键切换，复制按钮跟随当前页签）
- **阅读进度与入场（首页）**：顶栏 2px 主色进度条用纯 CSS `scroll-timeline`（无滚动监听）；hero 首屏 stagger 上浮 + 区块滚动渐入（`--d` 延时），全部动效在 `prefers-reduced-motion` 下收敛
- **模态框 demo**：`dialog[open]` 在示例区内以静态块呈现（CSS 覆盖），不注入官方演示 JS
- **降级项**：版本选择器页的色板/配置 select 为静态展示（官方为 React 交互组件）
- **对比度**：色板卡 350 级色号文字统一钉深色（亮黄绿底不满足 3:1），其余遵循 Pico 原色

## 部署

已部署 GitHub Pages 自定义域名：<https://picocss.ndjp.net>（main 分支，`.github/workflows/deploy.yml`：bun install → astro build → upload-pages-artifact → deploy-pages）。

- 根路径部署，`astro.config.mjs` 只设 `site: "https://picocss.ndjp.net"`，不设 `base`（`BASE_URL` 为 `/`，站点内链与资产均为根相对路径）
- 自定义域名绑定：`public/CNAME`（内容 `picocss.ndjp.net`，随构建进入 dist，部署后自动绑定）；DNS 侧在 ndjp.net 加一条 CNAME 记录（主机 `picocss` → `bbylw.github.io`），再在仓库 Settings → Pages 打开 Enforce HTTPS
- 页面内官方示例 demo 的 `href="/docs/..."` 保持英文源原样（忠实呈现），不参与 base 改写
- `.shots/` 验收脚本的本地静态服务器保留 `/pico-cn` 前缀剥离逻辑（根部署下为无操作，保持兼容）
- 无服务端依赖，不需要任何运行时 API

## 许可

内容翻译自 [picocss.com/docs](https://picocss.com/docs)，遵循 Pico 的 [MIT 许可证](https://github.com/picocss/pico/blob/master/LICENSE.md)。

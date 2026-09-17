# Pico CSS 中文站翻译规范（子代理作业手册）

## 输入 / 输出

- 输入：`C:/Users/bbylw/Desktop/web/.probe/en_src/<slug>.json` —— 官方文档的结构化块序列
- 输出：`C:/Users/bbylw/Desktop/web/src/content/docs/<路径>.mdx`
- 块类型：`p`（md 段落）、`h2`/`h3`（text+id）、`code`（lang/code/title/collapsed）、`example`（demo/code/lang/label）、`ul`/`ol`（items md）、`quote`（md）、`table`（md）、`raw`（html）、`hr`

## Frontmatter

```yaml
---
title: 按钮
chapter: 内容
lead: 按钮使用原生 <code>&lt;button&gt;</code> 标签，无需 <code>.classes</code> 即可获得默认样式。
badge: new            # 仅带「新」标记的页面需要
toc:
  - { id: variants, text: 变体, depth: 2 }
---
```

- `chapter` 七组固定译名：Getting started→入门、Customization→定制、Layout→布局、Content→内容、Forms→表单、Components→组件、About→关于
- `lead` 是 HTML 字符串（Docs 布局 set:html 渲染）：尖括号必须实体化 `&lt;` `&gt;`，代码用 `<code>`
- `toc`：每个 h2/h3 一条；`id` 沿用源 JSON 的英文 slug，`text` 用中文标题；无 h2 的页面 toc 省略

## 正文规则

1. **标题**：一律 `<h2 id="源id">中文标题</h2>`（h3 同理）。id 保持英文原 slug 不变（保护深链）。标题后不要加 `#`。
2. **段落**：普通 markdown。行内代码用反引号；`[text](url)` 链接。
3. **链接改写**：`https://picocss.com/docs/xxx` → `/docs/xxx/`；`https://picocss.com/docs` → `/docs/`；`https://picocss.com/docs/forms/input` → `/docs/forms/input/`。其余外链原样保留。
4. **代码块**：用围栏代码块，语言取源 `lang`（html/scss/bash/css/js）。代码内容与注释一律不翻译、不重排、不改缩进。
5. **示例**（type=example）：
   ```tsx
   import Ex from "../../components/Ex.astro";   // 二级目录用 ../../../

   <Ex
     html={`<button>Button</button>`}
     code={`<button>Button</button>`}
     lang="html"
     label="Button example"
   />
   ```
   - `html`/`code` 字符串原样保留（class、data-* 属性照抄）；`lang` 缺省即 html
   - 模板字符串内如出现反引号或 `${`（几乎不会），改用 frontmatter 方案并记录在交付说明中
   - demo 内的示例文案（Button / Primary / Solid Liquid Gas / 卡片内容等）保持英文，与官方站一致
6. **raw**（colors 色板卡、version-picker、brand 下载块等）：`<Raw html={`…`} />`（import Raw 同上）。块内英文标签可译（如色名 Red/Pink → 红/粉），CSS class、style 属性不动。
7. **列表/引用/表格**：标准 markdown。表格单元格文字翻译（表头、项目类型等），代码样片段（`<576px`、`.grid`）保留并加反引号。
8. **details 折叠代码**（type=code 且 collapsed:true）：写成
   ````
   <details>
     <summary>中文标题（译自 title 字段）</summary>

   ```scss
   …原代码…
   ```

   </details>
   ````

## 文风与红线

- 现代、直白、技术性；拒绝文言腔与古风；不添加任何装饰性序号
- 中英文之间加半角空格（"通过 CDN 引入 `pico.min.css`"）；全角标点；直引号改中文引号「」或 ""（自然即可）
- 术语统一：classless→无类版本、dropdown→下拉菜单、accordion→手风琴、modal→模态框、tooltip→工具提示、landmark→地标、group→分组、switch→开关、range→滑块、progress→进度条、grid→栅格、color scheme→配色方案、palette→调色板、utility classes→工具类
- Pico、Pico CSS、CDN、NPM、Sass、CSS、HTML、RTL 等专名保持原文

## 交付自检

- 文件以 UTF-8 保存；frontmatter YAML 合法
- 每个 h2/h3 的 id 与 toc 一一对应、顺序一致
- 不确定语法（MDX 会炸的）：正文裸 `<url>` 尖括号 → 必须写成 `` `<url>` `` 或 `[url](url)`；裸 `{` `}` → 放进字符串
- import 路径按目录层级数对（docs 顶层 `../../components`，forms/ 下 `../../../components`）

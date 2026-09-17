<p>
  <a href="https://picocss.com" target="_blank">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/picocss/pico/HEAD/.github/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/picocss/pico/HEAD/.github/logo-light.svg">
      <img alt="Pico CSS" src="https://raw.githubusercontent.com/picocss/pico/HEAD/.github/logo-light.svg" width="auto" height="60">
    </picture>
  </a>
</p>

[![Github release](https://img.shields.io/github/v/release/picocss/pico?color=0172ad&logo=github&logoColor=white)](https://github.com/picocss/pico/releases/latest)
[![npm version](https://img.shields.io/npm/v/@picocss/pico?color=0172ad)](https://www.npmjs.com/package/@picocss/pico)
[![License](https://img.shields.io/badge/license-MIT-%230172ad)](https://github.com/picocss/pico/blob/master/LICENSE.md)
[![X (formerly Twitter)](https://img.shields.io/twitter/url/https/twitter.com/picocss.svg?style=social&label=Follow%20%40picocss)](https://x.com/picocss)

## 面向语义化 HTML 的极简 CSS 框架

一套极简、轻量的起步套件，以语义化语法为先，让每个 HTML 元素默认就具备响应式与优雅的样式。

写 HTML，引入 Pico CSS，大功告成！

## v2 有什么新变化？

Pico v2.0 带来了更好的可访问性、借助 SASS 更轻松的定制、完整的调色板、全新的 group 组件，以及可通过 CDN 使用的 20 套预编译配色主题，组合总数超过 100 种。

[了解更多](https://picocss.com/docs/v2)

## 强化版 HTML 重置

Pico 恰到好处地提供了所需的一切，是构建干净、轻量设计系统的绝佳起点。

- 轻类且语义化
- 仅凭 CSS 即可获得出色样式
- 全面响应式
- 浅色或深色模式
- 轻松定制
- 性能优化

## 目录

- [快速开始](#快速开始)
- [无类版本](#无类版本)
- [局限性](#局限性)
- [文档](#文档)
- [浏览器支持](#浏览器支持)
- [贡献](#贡献)
- [版权与许可](#版权与许可)

## 快速开始

有 4 种方式可以开始使用 pico.css：

### 手动安装

[下载 Pico](https://github.com/picocss/pico/archive/refs/heads/main.zip)，并在你网站的 `<head>` 中引入 `/css/pico.min.css`。

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
```

### 通过 CDN 使用

或者，你可以使用 [jsDelivr CDN](https://www.jsdelivr.com/package/npm/@picocss/pico) 来引入 pico.css。

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
```

### 使用 NPM 安装

```shell
npm install @picocss/pico
```

或者

```shell
yarn add @picocss/pico
```

然后，通过 [@use](https://sass-lang.com/documentation/at-rules/use) 将 Pico 引入你的 SCSS 文件：

```SCSS
@use "pico";
```

### 使用 Composer 安装

```shell
composer require picocss/pico
```

### 起步 HTML 模板

```HTML
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light dark">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    <title>Hello world!</title>
  </head>
  <body>
    <main class="container">
      <h1>Hello world!</h1>
    </main>
  </body>
</html>
```

## 无类版本

Pico 提供 `.classless` 无类版本。

在该版本中，`<body>` 内的 `<header>`、`<main>` 和 `<footer>` 会作为容器，用来定义居中或流式的视口。

如果需要居中视口，请使用默认的 `.classless` 版本：

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css"
/>
```

如果需要流式容器，请使用 `.fluid.classless` 版本：

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.fluid.classless.min.css"
>
```

然后只需编写纯 HTML，它就会很好看：

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="color-scheme" content="light dark">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.classless.min.css"
    >
    <title>Hello, world!</title>
  </head>
  <body>
    <main>
      <h1>Hello, world!</h1>
    </main>
  </body>
</html>
```

## 局限性

对于快速或小型项目，Pico CSS 可以在不编写自定义 CSS 的情况下使用。不过，它被设计为起点，类似"加强版的 reset CSS"。由于 Pico 没有集成任何辅助类或工具类 `.classes`，这个极简 CSS 框架需要你具备 SCSS 或 CSS 知识才能构建大型项目。

[了解更多](https://picocss.com/docs/usage-scenarios)

## 文档

**入门**

- [快速开始](https://picocss.com/docs)
- [版本选择器 `新`](https://picocss.com/docs/version-picker)
- [配色方案](https://picocss.com/docs/color-schemes)
- [无类版本](https://picocss.com/docs/classless)
- [条件样式 `新`](https://picocss.com/docs/conditional)
- [RTL 从右到左排版](https://picocss.com/docs/rtl)

**定制**

- [CSS 变量](https://picocss.com/docs/css-variables)
- [Sass](https://picocss.com/docs/sass)
- [颜色 `新`](https://picocss.com/docs/colors)

**布局**

- [容器](https://picocss.com/docs/container)
- [地标与区块](https://picocss.com/docs/landmarks-section)
- [栅格](https://picocss.com/docs/grid)
- [溢出自动 `新`](https://picocss.com/docs/overflow-auto)

**内容**

- [排版](https://picocss.com/docs/typography)
- [链接](https://picocss.com/docs/link)
- [按钮](https://picocss.com/docs/button)
- [表格](https://picocss.com/docs/table)

**表单**

- [概览](https://picocss.com/docs/forms)
- [输入框](https://picocss.com/docs/forms/input)
- [文本域](https://picocss.com/docs/forms/textarea)
- [下拉选择](https://picocss.com/docs/forms/select)
- [复选框](https://picocss.com/docs/forms/checkboxes)
- [单选框](https://picocss.com/docs/forms/radios)
- [开关](https://picocss.com/docs/forms/switch)
- [滑块](https://picocss.com/docs/forms/range)

**组件**

- [手风琴](https://picocss.com/docs/accordion)
- [卡片](https://picocss.com/docs/card)
- [下拉菜单](https://picocss.com/docs/dropdown)
- [分组 `新`](https://picocss.com/docs/group)
- [加载](https://picocss.com/docs/loading)
- [模态框](https://picocss.com/docs/modal)
- [导航](https://picocss.com/docs/nav)
- [进度条](https://picocss.com/docs/progress)
- [工具提示](https://picocss.com/docs/tooltip)

**关于**

- [v2 有什么新变化？](https://picocss.com/docs/v2)
- [使命](https://picocss.com/docs/mission)
- [使用场景](https://picocss.com/docs/usage-scenarios)
- [品牌](https://picocss.com/docs/brand)
- [基于 Pico 构建](https://picocss.com/docs/built-with)

## 浏览器支持

Pico CSS 针对最新稳定版的 Chrome、Firefox、Edge 和 Safari 进行设计与测试。它不支持任何版本的 IE，包括 IE 11。

## 贡献

如果你有兴趣为 Pico CSS 做贡献，请阅读我们的[贡献指南](https://github.com/picocss/pico/blob/master/.github/CONTRIBUTING.md)。

## 版权与许可

基于 [MIT 许可证](https://github.com/picocss/pico/blob/master/LICENSE.md) 发布。

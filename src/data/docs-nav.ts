export interface NavItem {
  /** entry id in the docs collection (glob-normalized, e.g. "forms/input") */
  id: string;
  /** zh label */
  label: string;
  badge?: "new";
}
export interface NavGroup {
  group: string;
  items: NavItem[];
}

export const DOCS_NAV: NavGroup[] = [
  {
    group: "入门",
    items: [
      { id: "quickstart", label: "快速开始" },
      { id: "version-picker", label: "版本选择器", badge: "new" },
      { id: "color-schemes", label: "配色方案" },
      { id: "classless", label: "无类版本" },
      { id: "conditional", label: "条件样式", badge: "new" },
      { id: "rtl", label: "RTL 从右到左排版" },
    ],
  },
  {
    group: "定制",
    items: [
      { id: "css-variables", label: "CSS 变量" },
      { id: "sass", label: "Sass" },
      { id: "colors", label: "颜色", badge: "new" },
    ],
  },
  {
    group: "布局",
    items: [
      { id: "container", label: "容器" },
      { id: "landmarks-section", label: "地标与区块" },
      { id: "grid", label: "栅格" },
      { id: "overflow-auto", label: "溢出自动", badge: "new" },
    ],
  },
  {
    group: "内容",
    items: [
      { id: "typography", label: "排版" },
      { id: "link", label: "链接" },
      { id: "button", label: "按钮" },
      { id: "table", label: "表格" },
    ],
  },
  {
    group: "表单",
    items: [
      { id: "forms", label: "概览" },
      { id: "forms/input", label: "输入框" },
      { id: "forms/textarea", label: "文本域" },
      { id: "forms/select", label: "下拉选择" },
      { id: "forms/checkboxes", label: "复选框" },
      { id: "forms/radios", label: "单选框" },
      { id: "forms/switch", label: "开关" },
      { id: "forms/range", label: "滑块" },
    ],
  },
  {
    group: "组件",
    items: [
      { id: "accordion", label: "手风琴" },
      { id: "card", label: "卡片" },
      { id: "dropdown", label: "下拉菜单" },
      { id: "group", label: "分组", badge: "new" },
      { id: "loading", label: "加载" },
      { id: "modal", label: "模态框" },
      { id: "nav", label: "导航" },
      { id: "progress", label: "进度条" },
      { id: "tooltip", label: "工具提示" },
    ],
  },
  {
    group: "关于",
    items: [
      { id: "v2", label: "v2 有什么新变化？" },
      { id: "mission", label: "使命" },
      { id: "usage-scenarios", label: "使用场景" },
      { id: "brand", label: "品牌" },
      { id: "built-with", label: "基于 Pico 构建" },
    ],
  },
];

/** flat ordered list for prev/next navigation */
export const DOCS_FLAT: NavItem[] = DOCS_NAV.flatMap((g) => g.items);

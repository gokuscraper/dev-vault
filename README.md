<p align="center">
  <img src="https://img.shields.io/badge/工具-487-blue?style=flat-square" alt="487 个工具">
  <img src="https://img.shields.io/badge/测试-487%2F487-green?style=flat-square" alt="全部测试通过">
  <img src="https://img.shields.io/badge/许可证-MIT-white?style=flat-square" alt="MIT">
  <img src="https://img.shields.io/badge/依赖-0-orange?style=flat-square" alt="零依赖">
</p>

<h1 align="center">🧰 Dev Vault</h1>

<p align="center">487 个浏览器端开发工具 · 全离线 · 零依赖 · 每个工具一个 HTML 文件</p>

<p align="center"><a href="README.en.md">🌐 English</a></p>

---

## 📖 简介

**Dev Vault** 是一个包含 **487 个独立 HTML 工具**的开发工具合集，涵盖 CSS、JavaScript、安全、网络、设计、数据处理、DevOps 等领域。

每个工具都是一个独立的 HTML 文件——在浏览器打开就能用。不需要构建步骤、不需要 npm 安装、无需注册、无任何追踪。

- 🌐 **浏览门户** — 打开 `index.html` 按分类浏览所有工具
- 📁 **直接打开** — `tools/<分类>/<工具名>.html`
- 🧪 **运行测试** — `node tests/run.mjs`

## 📂 分类概览

| 分类 | 数量 | 示例 |
|------|------|------|
| CSS | 57 | 布局、动画、绘制、响应式、滚动吸附、容器查询 |
| JavaScript | 91 | Web API、设计模式、可视化工具、引擎内部 |
| 编码 | 63 | JSON、正则、JWT、哈希、Cron、环境变量、Docker、Git |
| 设计 | 42 | 颜色、字体、SVG、图标、图片、CSS 生成器 |
| 安全 | 19 | CSP、CORS、JWT、SRI、清理器、Cookie 检查 |
| 网络 | 17 | DNS、MAC、IPv4/6、HTTP、TLS、WebSocket |
| 数据 | 18 | npm、GitHub、PyPI、crate、许可证、SSL |
| AI | 5 | LLM 价格、提示词成本、模型选择 |
| DevOps | 10 | Docker、K8s、Terraform、Grafana、GitHub Actions |
| 转换工具 | 14 | JSON↔TOML↔YAML↔XML、温度、IBAN、电话 |
| 更多... | 151 | 数学、加密、音频、图片、写作、设备 API |

[→ 浏览全部 487 个工具](https://gokuscraper.github.io/dev-vault/)

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/gokuscraper/dev-vault.git

# 打开门户（或直接打开任意工具文件）
open index.html

# 运行测试（需 Node.js + Playwright）
npm install
node tests/run.mjs
```

## 💡 设计理念

- **单个 HTML 文件** — 查看源码，学习原理
- **完全离线** — 首次加载后，一切都在本地
- **零追踪** — 无分析、无追踪、无广告
- **深色主题** — 默认深色模式

---

## 🙏 致谢

部分内容来源于 [yurukusa/dev-toolkit](https://github.com/yurukusa/dev-toolkit)，部分设计参考了 [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools)。

---

<p align="center">MIT 许可证 · 用 ❤️ 打造</p>

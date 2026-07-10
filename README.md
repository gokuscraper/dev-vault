<p align="center">
  <img src="https://img.shields.io/badge/tools-487-blue?style=flat-square" alt="487 tools">
  <img src="https://img.shields.io/badge/tests-487%2F487-green?style=flat-square" alt="All tests passing">
  <img src="https://img.shields.io/badge/license-MIT-white?style=flat-square" alt="MIT">
  <img src="https://img.shields.io/badge/dependencies-0-orange?style=flat-square" alt="Zero dependencies">
</p>

# 🧰 Dev Vault

> 487 browser-based developer tools. All offline. Zero dependencies. One HTML file each.

**[English](#english) · [中文](#chinese)**

---

<a id="english"></a>

## 🇬🇧 English

**Dev Vault** is a collection of **487 standalone HTML tools** covering CSS, JavaScript, security, networking, design, data, DevOps, and more.

Every tool is a single HTML file — open it in a browser and it just works. No build step, no npm install, no signup, no tracking.

- 🌐 **Open the portal** — open `index.html` to browse all tools by category
- 📁 **Browse files** — `tools/<category>/<name>.html`
- 🧪 **Run tests** — `node tests/run.mjs`

### Categories

| Category | Count | Examples |
|----------|-------|---------|
| CSS | 57 | Layout, animation, painting, responsive, scroll-snap, container queries |
| JavaScript | 91 | Web APIs, patterns, visualizers, engine internals |
| Code | 63 | JSON, regex, JWT, hash, cron, env, docker, git |
| Design | 42 | Color, typography, SVG, icon, image, CSS generators |
| Security | 19 | CSP, CORS, JWT, SRI, sanitizer, cookie inspector |
| Network / Net | 17 | DNS, MAC, IPv4/6, HTTP, TLS, WebSocket |
| Data | 18 | npm, GitHub, pypi, crate, license, SSL |
| AI | 5 | LLM pricing, prompt cost, model picker |
| DevOps | 10 | Docker, K8s, Terraform, Grafana, GitHub Actions |
| Converter | 14 | JSON↔TOML↔YAML↔XML, temperature, IBAN, phone |
| More... | 151 | Math, crypto, audio, image, writing, device APIs |

[→ Browse all 487 tools](https://gokuscraper.github.io/dev-vault/)

### Quick Start

```bash
# Clone
git clone https://github.com/gokuscraper/dev-vault.git

# Open the portal (or open any tool file directly)
open index.html

# Run tests (requires Node.js + Playwright)
npm install
node tests/run.mjs
```

### Philosophy

- **Single HTML file** — view source, inspect, learn
- **Fully offline** — after first load, everything is local
- **Zero telemetry** — no analytics, no tracking, no ads
- **Dark theme** — defaults to dark mode

---

<a id="chinese"></a>

## 🇨🇳 中文

**Dev Vault** 是一个包含 **487 个独立 HTML 工具**的开发工具库，涵盖 CSS、JavaScript、安全、网络、设计、数据处理、DevOps 等领域。

每个工具都是一个独立的 HTML 文件——在浏览器打开就能用。不需要构建步骤、不需要 npm 安装、无需注册、无任何追踪。

- 🌐 **浏览门户** — 打开 `index.html` 按分类浏览所有工具
- 📁 **直接打开** — `tools/<分类>/<工具名>.html`
- 🧪 **运行测试** — `node tests/run.mjs`

### 分类概览

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

### 快速开始

```bash
# 克隆仓库
git clone https://github.com/gokuscraper/dev-vault.git

# 打开门户（或直接打开任意工具文件）
open index.html

# 运行测试（需 Node.js + Playwright）
npm install
node tests/run.mjs
```

### 设计理念

- **单个 HTML 文件** — 查看源码，学习原理
- **完全离线** — 首次加载后，一切都在本地
- **零追踪** — 无分析、无追踪、无广告
- **深色主题** — 默认深色模式

---

<p align="center">MIT License · Built with ❤️</p>

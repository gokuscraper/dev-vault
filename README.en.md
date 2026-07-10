<p align="center">
  <img src="https://img.shields.io/badge/tools-487-blue?style=flat-square" alt="487 tools">
  <img src="https://img.shields.io/badge/tests-487%2F487-green?style=flat-square" alt="All tests passing">
  <img src="https://img.shields.io/badge/license-MIT-white?style=flat-square" alt="MIT">
  <img src="https://img.shields.io/badge/dependencies-0-orange?style=flat-square" alt="Zero dependencies">
</p>

<h1 align="center">🧰 Dev Vault</h1>

<p align="center">487 browser-based developer tools · All offline · Zero dependencies · One HTML file each</p>

<p align="center"><a href="README.md">🌐 中文</a></p>

---

## 📖 About

**Dev Vault** is a collection of **487 standalone HTML tools** covering CSS, JavaScript, security, networking, design, data, DevOps, and more.

Every tool is a single HTML file — open it in a browser and it just works. No build step, no npm install, no signup, no tracking.

- 🌐 **Open the portal** — open `index.html` to browse all tools by category
- 📁 **Browse files** — `tools/<category>/<name>.html`
- 🧪 **Run tests** — `node tests/run.mjs`

## 📂 Categories

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

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/gokuscraper/dev-vault.git

# Open the portal (or open any tool file directly)
open index.html

# Run tests (requires Node.js + Playwright)
npm install
node tests/run.mjs
```

## 💡 Philosophy

- **Single HTML file** — view source, inspect, learn
- **Fully offline** — after first load, everything is local
- **Zero telemetry** — no analytics, no tracking, no ads
- **Dark theme** — defaults to dark mode

---

<p align="center">MIT License · Built with ❤️</p>

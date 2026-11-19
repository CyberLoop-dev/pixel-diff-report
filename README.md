<div align="center">

![Pixel Diff Report banner](https://capsule-render.vercel.app/api?type=waving&color=0:#7c3aed,100:#0f766e&height=170&section=header&text=Pixel%20Diff%20Report&fontSize=34&fontColor=ffffff)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&pause=1000&color=0f766e&center=true&vCenter=true&width=720&lines=See%20exactly%20what%20changed%20between%20images%3BLocal%20visual%20regression%20reports" alt="Typing SVG" />

[![MIT](https://img.shields.io/badge/license-MIT-0f766e.svg)](LICENSE)
[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/CyberLoop-dev/pixel-diff-report?style=flat)](https://github.com/CyberLoop-dev/pixel-diff-report/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/pixel-diff-report)](https://github.com/CyberLoop-dev/pixel-diff-report/commits/main)

**A simple, local visual comparison report for two images.**

<img src="assets/illustration.svg" alt="Pixel Diff Report illustration" width="560" />

</div>

## 🧭 Overview

Pixel Diff Report compares two images of the same dimensions and writes a difference heatmap, a blended overlay, copied input images, and a self-contained HTML report. It never uploads images.

## ✨ Features

- 🖼️ Compares local PNG, JPEG, and other Pillow-supported formats.
- 🔥 Highlights changed pixels in a difference image.
- 🌓 Creates a 50/50 overlay for visual inspection.
- 📊 Reports changed-pixel ratio and mean absolute error.
- 🔒 Processes everything locally; source files are never modified.

## 🖥️ Demo

```bash
python main.py baseline.png current.png --out-dir diff-report
```
Open <code>diff-report/index.html</code> to inspect the generated comparison.

## 🚀 Quick Start

```bash
git clone https://github.com/CyberLoop-dev/pixel-diff-report.git
cd pixel-diff-report
python -m pip install -r requirements.txt
python main.py baseline.png current.png --out-dir diff-report
```

## 🧱 Tech Stack

- 🐍 Python 3.10+
- 🖼️ Pillow

## 🗂️ Folder Structure

```text
pixel-diff-report/
├── main.py
├── requirements.txt
├── tests/test_main.py
├── pyproject.toml
├── assets/illustration.svg
└── README.md
```

## 🛣️ Roadmap

- [x] Difference heatmap and overlay
- [x] HTML and JSON summaries
- [ ] Optional perceptual color-space threshold

## 🤝 Contributing

Issues and pull requests are welcome. Please include a clear reproduction or sample input and keep changes focused.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:#0f766e,100:#7c3aed&height=100&section=footer)

</div>

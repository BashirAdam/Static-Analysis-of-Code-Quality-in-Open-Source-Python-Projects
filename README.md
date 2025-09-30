# Static Analysis of Code Quality in Open-Source Python Projects

This repository contains the datasets, scripts, and figures for the paper:

> **Static Analysis of Code Quality in Open-Source Python Projects**  
> Submitted to *Journal of Undergraduate Research International (JURI), 2025*

---

## 📖 Overview
This project evaluates the code quality of popular open-source Python projects using **static analysis metrics**.  
The goal is to provide empirical insights into maintainability, complexity, coding standard adherence, and security issues.

---

## 🔧 Tools Used
- **[Radon](https://radon.readthedocs.io/)** → Lines of Code (LOC), Cyclomatic Complexity (CC), Maintainability Index (MI)  
- **[Pylint](https://pylint.org/)** → Code quality score, code smells  
- **[Flake8](https://flake8.pycqa.org/)** → PEP8 style violations  
- **[Bandit](https://bandit.readthedocs.io/)** → Security issue detection  

---

## 📊 Workflow
1. **Project Selection** – Open-source Python projects (e.g., Requests, BeautifulSoup4).  
2. **Metric Extraction** – Run Radon, Pylint, Flake8, and Bandit on each source file.  
3. **Dataset Creation** – Export metrics into a CSV file.  
4. **Analysis** – Summarize metrics, detect high-risk modules, and visualize trends.  

---

---

## 📈 Example Results
- **Average Cyclomatic Complexity:** 1.87 across 6,962 files  
- **Maintainability Index:** 45.0 mean (0–100 scale)  
- **PEP8 Violations:** Ranged from 0 to 1,087 per file  
- **Security Issues:** Up to 596 flagged per file  

---

## 🛠 Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/Static-Analysis-Python-CodeQuality.git
cd Static-Analysis-Python-CodeQuality
pip install pandas radon pylint flake8 bandit tqdm

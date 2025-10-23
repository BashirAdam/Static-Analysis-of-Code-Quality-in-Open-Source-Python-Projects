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

## Quick Start
1. Clone this repository
2. Run: `pip install -r requirements.txt`
3. Run: `python run_analysis.py`
4. All results will be generated in the `results/` folder

## File Structure
- `analyze_metrics_per_module.py` - Core analysis script
- `generate_plots.py` - Visualization generation
- `run_analysis.py` - Complete automation script
- `requirements.txt` - Python dependencies
- `BeautifulSoup4_metrics.csv` - Raw metrics for BeautifulSoup4
- `requests_metrics.csv` - Raw metrics for Requests
- `figures/` - Generated visualization figures

## Reproducing Results
See the detailed instructions in [REPRODUCTION_GUIDE.md](REPRODUCTION_GUIDE.md)

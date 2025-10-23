# Static Analysis of Code Quality in Open-Source Python Projects

This repository contains the code, data, and figures for reproducing the analysis in the paper:

**Static Analysis of Code Quality in Open-Source Python Projects**  
*Submitted to Journal of Undergraduate Research International (JURI), 2025*

## 📖 Overview

This project conducts a systematic static analysis of two popular open-source Python projects (**Requests** and **BeautifulSoup4**) to evaluate code quality metrics including cyclomatic complexity, maintainability, and PEP8 compliance.

## 🔧 Tools Used

- **Radon** → Lines of Code (LOC), Cyclomatic Complexity (CC), Maintainability Index (MI)
- **Pylint** → Code quality scoring and code smells detection
- **Flake8** → PEP8 style violations

## 📊 Project Structure
```
Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects/
├── run_analysis.py # Main script to reproduce entire analysis
├── analyze_metrics_per_module.py # Core analysis script
├── generate_plots.py # Visualization script
├── requirements.txt # Python dependencies
├── BeautifulSoup4_metrics.csv # Analysis results for BeautifulSoup4
├── requests_metrics.csv # Analysis results for Requests
└── figures/ # Generated visualization plots
```

## 🚀 Quick Start (Full Reproduction)

1. **Clone this repository**
   ```bash
   git clone https://github.com/BashirAdam/Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects.git
   cd Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the complete analysis**
   ```bash
   python run_analysis.py
   ```

   This single command will:
   - Clone the target projects (Requests and BeautifulSoup4)
   - Run all static analysis tools
   - Generate all metrics CSV files
   - Create all visualization figures
   - Display summary statistics

## 🔍 Manual Execution

If you prefer to run steps individually:

```bash
# Run the metric analysis
python analyze_metrics_per_module.py

# Generate visualizations
python generate_plots.py
```

## 📈 Output Files

- **BeautifulSoup4_metrics.csv** - Metrics for 19 Python modules
- **requests_metrics.csv** - Metrics for 34 Python modules
- **figures/** - 6 visualization plots showing complexity distributions and relationships

### CSV Columns:
- **Module/File** - Name of the Python file
- **Lines of Code** - Total lines in the file
- **Cyclomatic Complexity (avg)** - Average complexity score
- **Maintainability Index** - Code maintainability score (0-100)
- **Pylint Score** - Code quality score (0-10)
- **PEP8 Violations** - Number of style guideline violations

## 📊 Key Findings (Summary)

- **BeautifulSoup4**: 7,755 LOC, average CC: 3.40, total PEP8 violations: 656
- **Requests**: 11,248 LOC, average CC: 2.87, total PEP8 violations: 533
- **High-complexity modules**: dammit.py (BeautifulSoup4) and test_requests.py (Requests) identified as refactoring candidates

## 📚 Research Context

This work contributes to software engineering by:

- Providing empirical code quality assessment of widely-used Python libraries
- Demonstrating a reproducible methodology for static analysis
- Identifying specific modules that would benefit most from refactoring
- Offering a template for similar code quality studies

## 🤝 Contact

- **Author**: Bashir Adam
- **Institution**: Ostim Technical University

## 🙏 Acknowledgments

- The open-source communities behind Requests and BeautifulSoup4
- Developers of Radon, Pylint, and Flake8 static analysis tools
- Journal of Undergraduate Research International for considering this work

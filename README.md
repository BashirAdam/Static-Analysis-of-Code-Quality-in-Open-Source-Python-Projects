# Static Analysis of Code Quality in Open-Source Python Projects

> **Status:** ✅ *Published Peer-Reviewed Research*  
> This work has been **peer-reviewed and published** in the *Journal of Undergraduate Research International (JURI)*.

---

This repository contains the code, data, and supplementary materials for the research paper:

**"Static Analysis of Code Quality in Open-Source Python Projects"**  
Preprint, 2025  
DOI (preprint): https://doi.org/10.64589/juri/215034

---

## Project Overview

This project presents a **reproducible static analysis** of code quality in two widely used open-source Python libraries:

- **Requests** – HTTP library for Python  
- **BeautifulSoup4** – HTML and XML parsing library

Using multiple static analysis tools, the study evaluates software quality at the **module level**, focusing on complexity, maintainability, and coding style. The goal is to identify refactoring candidates and demonstrate how automated static analysis can support long-term software sustainability.

---

## Analysis Metrics

The following metrics are extracted and analyzed:

- Lines of Code (LOC)
- Cyclomatic Complexity (average per module)
- Maintainability Index (MI)
- Pylint Score
- PEP8 Style Violations

---

## Tools & Technologies

- **Python**
- **Radon** – Complexity and maintainability metrics
- **Pylint** – Code quality scoring
- **Flake8** – PEP8 style analysis
- **Pandas / NumPy** – Data aggregation and analysis
- **Matplotlib / Seaborn** – Data visualization
- **Git & GitHub** – Version control and reproducibility

All tools are used with default configurations to ensure reproducibility and alignment with common industry practices.

---

## Methodology

1. Clone official GitHub repositories of Requests and BeautifulSoup4
2. Run static analysis tools on all Python modules
3. Automatically parse and extract metrics using Python scripts
4. Aggregate results into structured CSV files
5. Perform module-level analysis and visualization
6. Identify high-risk components and refactoring candidates

The entire workflow is automated and fully reproducible.

---

## Key Findings (Preliminary)

- Both projects show good overall maintainability but contain **specific high-risk modules** with elevated complexity and style violations.
- Requests demonstrates more consistent code quality across modules.
- A statistically significant **negative correlation** exists between cyclomatic complexity and maintainability.
- Static analysis tools are effective for identifying technical debt and guiding refactoring decisions.

> ⚠️ *Note:* These findings are based on the current preprint version and may be refined during peer review.

---

## How to Reproduce the Analysis

```bash
# Clone this repository
git clone https://github.com/BashirAdam/Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects.git
cd Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects

# Install dependencies
pip install -r requirements.txt

# Run the full analysis pipeline
python run_analysis.py
```

This will regenerate all tables, figures, and aggregated results used in the preprint.

---

## Repository Structure

```text
├── data/              # Raw and processed CSV files
├── scripts/           # Metric extraction and automation scripts
├── figures/           # Generated plots and visualizations
├── run_analysis.py    # Main reproduction script
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Relevance

This project is relevant for:

- **Data Analysts / Data Scientists** – metric analysis, aggregation, correlation studies
- **Software Engineers** – code quality, maintainability, refactoring insights
- **AI/ML Engineers** – reproducible pipelines and data-driven evaluation
- **Researchers & Students** – empirical software engineering research

---

## Citation

If you use or reference this work, please cite the **preprint**:

> Bashir Adam Ahmed Ali. *Static Analysis of Code Quality in Open-Source Python Projects*. Preprint, 2025. https://doi.org/10.64589/juri/215034

---

## Author

**Bashir Adam Ahmed Ali**  
BSc in Software Engineering, Ostim Technical University  
GitHub: https://github.com/BashirAdam  
ORCID: https://orcid.org/0009-0009-0267-2904

---

## License

This repository is provided for **academic and educational purposes**. Please respect the licenses of the analyzed open-source projects (Requests and BeautifulSoup4).


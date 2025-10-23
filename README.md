# Static Analysis of Code Quality in Open-Source Python Projects

This repository contains the datasets, scripts, and figures for the paper:

> **Static Analysis of Code Quality in Open-Source Python Projects**  
> Submitted to *Journal of Undergraduate Research International (JURI), 2025*

---

## 📖 Overview

This project evaluates the code quality of popular open-source Python projects using **static analysis metrics**.  
The goal is to provide empirical insights into maintainability, complexity, coding standard adherence, and security issues.

### Key Research Questions
- How do different Python projects compare in terms of code quality metrics?
- Which modules within projects show the highest complexity and lowest maintainability?
- What are the common patterns in code quality across popular open-source Python libraries?

---

## 🔧 Tools Used

- **[Radon](https://radon.readthedocs.io/)** → Lines of Code (LOC), Cyclomatic Complexity (CC), Maintainability Index (MI)  
- **[Pylint](https://pylint.org/)** → Code quality score, code smells  
- **[Flake8](https://flake8.pycqa.org/)** → PEP8 style violations  

---

## 📊 Project Structure

```
Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects/
├── README.md                           # This file
├── analyze_metrics_per_module.py       # Main analysis script
├── generate_plots.py                   # Visualization script
├── BeautifulSoup4_metrics.csv          # Analysis results for BeautifulSoup4
├── requests_metrics.csv                # Analysis results for requests
└── figures/                            # Generated plots and visualizations
```

---

## 🛠 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects.git
   cd Static-Analysis-of-Code-Quality-in-Open-Source-Python-Projects
   ```

2. **Install required dependencies:**
   ```bash
   pip install pandas radon pylint flake8 bandit tqdm matplotlib seaborn
   ```

3. **Clone the target Python projects for analysis:**
   ```bash
   # Clone BeautifulSoup4
   git clone https://github.com/waylan/BeautifulSoup4.git
   
   # Clone requests
   git clone https://github.com/psf/requests.git
   ```

4. **Update project paths in the analysis script:**
   Edit `analyze_metrics_per_module.py` and update the `projects` list with your local paths:
   ```python
   projects = [
       r"path/to/BeautifulSoup4",
       r"path/to/requests"
   ]
   ```

---

## 🚀 Usage

### Running the Analysis

1. **Execute the main analysis script:**
   ```bash
   python analyze_metrics_per_module.py
   ```

   This will:
   - Analyze each Python file in the target projects
   - Calculate complexity, maintainability, and quality metrics
   - Generate CSV files with detailed metrics per module
   - Display summary statistics

2. **Generate visualizations:**
   ```bash
   python generate_plots.py
   ```

   This will create:
   - Bar charts showing cyclomatic complexity per module
   - Histograms of Pylint scores distribution
   - Scatter plots of Lines of Code vs Cyclomatic Complexity

### Understanding the Output

The analysis generates CSV files with the following columns:
- **Module/File**: Name of the Python file
- **Lines of Code**: Total lines in the file
- **Cyclomatic Complexity (avg)**: Average complexity score
- **Maintainability Index**: Code maintainability score (0-100)
- **Pylint Score**: Code quality score (0-10)
- **PEP8 Violations**: Number of style violations

---

## 📈 Key Findings

### Summary Statistics
- **Average Cyclomatic Complexity:** 1.87 across 6,962 files  
- **Maintainability Index:** 45.0 mean (0–100 scale)  
- **PEP8 Violations:** Ranged from 0 to 1,087 per file  
- **Security Issues:** Up to 596 flagged per file  

### Quality Insights
- **High Complexity Modules**: Files with CC > 10 require refactoring attention
- **Low Maintainability**: MI < 20 indicates poor maintainability
- **Style Consistency**: Projects with fewer PEP8 violations show better code organization
- **Security Awareness**: Bandit analysis reveals potential security vulnerabilities

---

## 📊 Workflow

1. **Project Selection** – Open-source Python projects (e.g., Requests, BeautifulSoup4)  
2. **Metric Extraction** – Run Radon, Pylint, Flake8, and Bandit on each source file  
3. **Dataset Creation** – Export metrics into CSV files  
4. **Analysis** – Summarize metrics, detect high-risk modules, and visualize trends  
5. **Visualization** – Generate plots and charts for comprehensive analysis

---

## 🔍 Methodology

### Static Analysis Metrics

1. **Cyclomatic Complexity (CC)**
   - Measures the number of linearly independent paths through code
   - Higher values indicate more complex, harder-to-maintain code
   - Thresholds: 1-10 (simple), 11-20 (moderate), 21-50 (complex), 50+ (very complex)

2. **Maintainability Index (MI)**
   - Composite metric considering Halstead volume, cyclomatic complexity, and LOC
   - Scale: 0-100 (higher is better)
   - Thresholds: 0-20 (low), 21-40 (moderate), 41-60 (good), 61-100 (excellent)

3. **Pylint Score**
   - Overall code quality assessment
   - Scale: 0-10 (higher is better)
   - Considers code smells, design issues, and best practices

4. **PEP8 Violations**
   - Count of style guideline violations
   - Lower values indicate better code consistency

---

## 🚀 Quick Start

1. Clone this repository
2. Run: `pip install -r requirements.txt`
3. Run: `python run_analysis.py`
4. All results will be generated in the `results/` folder

---

## 📚 Research Context

This project contributes to the field of software engineering by:

- **Empirical Analysis**: Providing quantitative data on code quality in popular Python projects
- **Tool Evaluation**: Demonstrating the effectiveness of static analysis tools
- **Quality Benchmarking**: Establishing baselines for code quality metrics
- **Educational Value**: Serving as a learning resource for code quality assessment

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

- Add analysis for additional Python projects
- Improve the visualization scripts
- Enhance the metric calculation algorithms
- Add support for additional static analysis tools

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For questions or collaboration opportunities, please contact:
- **Author**: [Your Name]
- **Email**: [your.email@university.edu]
- **Institution**: [Your University]

---

## 🙏 Acknowledgments

- The open-source Python community for providing the projects analyzed
- The developers of Radon, Pylint, Flake8, and Bandit for their excellent tools
- The Journal of Undergraduate Research International (JURI) for considering this work

---

*This research was conducted as part of undergraduate research in Computer Science, focusing on software engineering and code quality assessment methodologies.*

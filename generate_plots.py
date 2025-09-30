import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: make plots prettier with seaborn
sns.set(style="whitegrid")

# --- Load CSV files ---
bs_file = "BeautifulSoup4_metrics.csv"  # update if needed
req_file = "requests_metrics.csv"       # update if needed

bs_data = pd.read_csv(bs_file)
req_data = pd.read_csv(req_file)

# --- Function to plot Bar Chart of Avg CC per Module ---
def plot_avg_cc(data, project_name):
    plt.figure(figsize=(12,6))
    plt.bar(data['Module/File'], data['Cyclomatic Complexity (avg)'], color='skyblue')
    plt.xticks(rotation=90)
    plt.ylabel("Average Cyclomatic Complexity")
    plt.title(f"{project_name}: Cyclomatic Complexity per Module")
    plt.tight_layout()
    plt.show()

# --- Function to plot Histogram of Pylint Scores ---
def plot_pylint_hist(data, project_name):
    plt.figure(figsize=(8,5))
    plt.hist(data['Pylint Score'].dropna(), bins=10, color='lightgreen', edgecolor='black')
    plt.xlabel("Pylint Score")
    plt.ylabel("Number of Modules")
    plt.title(f"{project_name}: Distribution of Pylint Scores")
    plt.show()

# --- Function to plot Scatter LOC vs CC ---
def plot_loc_vs_cc(data, project_name):
    plt.figure(figsize=(10,6))
    plt.scatter(data['Lines of Code'], data['Cyclomatic Complexity (avg)'], color='salmon')
    plt.xlabel("Lines of Code")
    plt.ylabel("Average Cyclomatic Complexity")
    plt.title(f"{project_name}: LOC vs Cyclomatic Complexity")
    plt.show()

# --- Generate plots for BeautifulSoup4 ---
plot_avg_cc(bs_data, "BeautifulSoup4")
plot_pylint_hist(bs_data, "BeautifulSoup4")
plot_loc_vs_cc(bs_data, "BeautifulSoup4")

# --- Generate plots for Requests ---
plot_avg_cc(req_data, "Requests")
plot_pylint_hist(req_data, "Requests")
plot_loc_vs_cc(req_data, "Requests")

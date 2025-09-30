import os
import subprocess
import csv
import re

# List of cloned projects (update paths)
projects = [
    r"C:\Users\bashi\BeautifulSoup4",
    r"C:\Users\bashi\requests"
]

# Run a shell command and capture output
def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    return result.stdout

# Parse Radon Cyclomatic Complexity by file
def parse_radon_cc(output):
    cc_data = {}
    lines = output.splitlines()
    current_file = None
    for line in lines:
        if line.endswith(".py"):
            current_file = os.path.basename(line.strip())
            cc_data[current_file] = []
        elif line.startswith(" ") and current_file:
            parts = line.strip().split()
            if len(parts) > 1 and ":" in parts[1]:
                try:
                    cc_score = int(parts[1].split(":")[1])
                    cc_data[current_file].append(cc_score)
                except:
                    pass
    avg_cc = {f: round(sum(vals)/len(vals), 2) if vals else 0 for f, vals in cc_data.items()}
    return avg_cc

# Parse Radon Maintainability Index by file
def parse_radon_mi(output):
    mi_data = {}
    lines = output.splitlines()
    for line in lines:
        match = re.match(r"(.+\.py) - MI: (\d+\.\d+)", line)
        if match:
            filename = os.path.basename(match.group(1).strip())
            mi = float(match.group(2))
            mi_data[filename] = mi
    return mi_data

# Count Flake8 violations per file
def parse_flake8(output):
    flake_data = {}
    lines = output.splitlines()
    for line in lines:
        parts = line.split(":")
        if len(parts) > 1:
            filename = os.path.basename(parts[0])
            flake_data[filename] = flake_data.get(filename, 0) + 1
    return flake_data

# Run Pylint per file (global score per module)
def get_pylint_score(file_path):
    output = run_command(f'py -m pylint "{file_path}" --score=y --reports=n')
    match = re.search(r"Your code has been rated at ([\d\.]+)/10", output)
    if match:
        return float(match.group(1))
    return None  # Handle files that fail Pylint

# Analyze a project
def analyze_project(project_path):
    project_name = os.path.basename(project_path)
    csv_file = f"{project_name}_metrics.csv"

    print(f"Analyzing {project_name}...\n")

    # Radon CC
    radon_cc_output = run_command(f'py -m radon cc "{project_path}" -s')
    cc_data = parse_radon_cc(radon_cc_output)

    # Radon MI
    radon_mi_output = run_command(f'py -m radon mi "{project_path}" -s')
    mi_data = parse_radon_mi(radon_mi_output)

    # Flake8
    flake8_output = run_command(f'py -m flake8 "{project_path}"')
    flake_data = parse_flake8(flake8_output)

    # Get all Python files in project
    py_files = []
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))

    # Initialize sums for summary
    total_loc = 0
    total_cc = 0
    total_mi = 0
    total_pylint = 0
    total_pep8 = 0
    count_cc = 0
    count_mi = 0
    count_pylint = 0

    # Write aggregated CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Module/File", "Lines of Code", "Cyclomatic Complexity (avg)", "Maintainability Index", "Pylint Score", "PEP8 Violations"])
        
        for file_path in py_files:
            filename = os.path.basename(file_path)
            
            # Lines of Code
            try:
                with open(file_path, 'r', encoding='utf-8') as ff:
                    loc = len(ff.readlines())
            except:
                loc = 0

            avg_cc = cc_data.get(filename, 0)
            mi = mi_data.get(filename, 0)
            pylint_score = get_pylint_score(file_path)
            pep8_violations = flake_data.get(filename, 0)

            # Accumulate for summary
            total_loc += loc
            if avg_cc > 0:
                total_cc += avg_cc
                count_cc += 1
            if mi > 0:
                total_mi += mi
                count_mi += 1
            if isinstance(pylint_score, float):
                total_pylint += pylint_score
                count_pylint += 1
            total_pep8 += pep8_violations

            # Replace None with "N/A" for CSV
            pylint_score_csv = pylint_score if pylint_score is not None else "N/A"

            writer.writerow([filename, loc, avg_cc, mi, pylint_score_csv, pep8_violations])

        # Write summary row
        writer.writerow([])
        writer.writerow([
            "SUMMARY",
            total_loc,
            round(total_cc / count_cc, 2) if count_cc else 0,
            round(total_mi / count_mi, 2) if count_mi else 0,
            round(total_pylint / count_pylint, 2) if count_pylint else "N/A",
            total_pep8
        ])

    print(f"Metrics saved to {csv_file}\n")

# Run analysis on all projects
for project in projects:
    analyze_project(project)

print("All projects analyzed successfully!")

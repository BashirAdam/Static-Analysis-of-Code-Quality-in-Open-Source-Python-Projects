#!/usr/bin/env python3
"""
Complete analysis script for Static Analysis of Code Quality in Open-Source Python Projects.

This script reproduces the entire analysis from the paper:
- Clones the target projects (Requests and BeautifulSoup4)
- Runs all static analysis tools
- Generates all metrics CSV files
- Creates all visualization figures
- Displays summary statistics

Usage: python run_analysis.py
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"\n {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f" {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f" Error in {description}:")
        print(f"Command: {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main execution function."""
    print(" Starting Complete Analysis for Static Analysis of Code Quality")
    print("=" * 70)
    
    # Check if we're in the right directory
    if not os.path.exists("analyze_metrics_per_module.py"):
        print(" Error: Please run this script from the project root directory")
        print("   Expected files: analyze_metrics_per_module.py, generate_plots.py")
        sys.exit(1)
    
    # Step 1: Clone BeautifulSoup4 (correct repository)
    if not os.path.exists("BeautifulSoup4"):
        success = run_command(
            "git clone https://github.com/wention/BeautifulSoup4.git",
            "Cloning BeautifulSoup4 repository"
        )
        if not success:
            print(" Failed to clone BeautifulSoup4. Continuing with existing data...")
    else:
        print(" BeautifulSoup4 directory already exists")
    
    # Step 2: Clone requests
    if not os.path.exists("requests"):
        success = run_command(
            "git clone https://github.com/psf/requests.git",
            "Cloning requests repository"
        )
        if not success:
            print(" Failed to clone requests. Continuing with existing data...")
    else:
        print(" requests directory already exists")
    
    # Step 3: Update project paths in analysis script
    print("\n Updating project paths in analysis script...")
    try:
        with open("analyze_metrics_per_module.py", "r") as f:
            content = f.read()
        
        # Update the projects list with current working directory paths
        current_dir = os.getcwd()
        updated_content = content.replace(
            'projects = [',
            f'projects = [\n    r"{current_dir}/BeautifulSoup4",\n    r"{current_dir}/requests"'
        )
        
        with open("analyze_metrics_per_module.py", "w") as f:
            f.write(updated_content)
        
        print(" Project paths updated successfully")
    except Exception as e:
        print(f" Error updating project paths: {e}")
        print("   You may need to manually update the paths in analyze_metrics_per_module.py")
    
    # Step 4: Run the metric analysis
    success = run_command(
        "python analyze_metrics_per_module.py",
        "Running static analysis and generating metrics"
    )
    if not success:
        print(" Analysis failed. Check the error messages above.")
        sys.exit(1)
    
    # Step 5: Generate visualizations
    success = run_command(
        "python generate_plots.py",
        "Generating visualization plots"
    )
    if not success:
        print(" Visualization generation failed. Check the error messages above.")
        sys.exit(1)
    
    # Step 6: Display summary
    print("\n" + "=" * 70)
    print(" ANALYSIS COMPLETE!")
    print("=" * 70)
    print("\n Generated Files:")
    
    # Check for generated files
    files_to_check = [
        "BeautifulSoup4_metrics.csv",
        "requests_metrics.csv",
        "figures/"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                file_count = len([f for f in os.listdir(file_path) if f.endswith(('.png', '.jpg', '.pdf'))])
                print(f"   {file_path} ({file_count} plots)")
            else:
                print(f"   {file_path}")
        else:
            print(f"   {file_path} (not found)")
    
    print("\n Quick Summary:")
    try:
        import pandas as pd
        
        # Read and display summary stats
        if os.path.exists("BeautifulSoup4_metrics.csv"):
            bs_data = pd.read_csv("BeautifulSoup4_metrics.csv")
            bs_summary = bs_data[bs_data['Module/File'] == 'SUMMARY'].iloc[0]
            print(f"  BeautifulSoup4: {bs_summary['Lines of Code']} LOC, CC: {bs_summary['Cyclomatic Complexity (avg)']:.2f}")
        
        if os.path.exists("requests_metrics.csv"):
            req_data = pd.read_csv("requests_metrics.csv")
            req_summary = req_data[req_data['Module/File'] == 'SUMMARY'].iloc[0]
            print(f"  Requests: {req_summary['Lines of Code']} LOC, CC: {req_summary['Cyclomatic Complexity (avg)']:.2f}")
            
    except Exception as e:
        print(f"  Could not load summary statistics: {e}")
    
    print("\n🔍 Next Steps:")
    print("  - Check the figures/ directory for visualization plots")
    print("  - Review the CSV files for detailed metrics")
    print("  - See README.md for detailed interpretation of results")
    
    print("\n Analysis reproduction complete!")

if __name__ == "__main__":
    main()

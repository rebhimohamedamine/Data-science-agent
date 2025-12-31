#!/usr/bin/env python
"""
Main script for Data Science Multi-Agent System
Orchestrates the crew to analyze datasets and generate reports
"""

import sys
import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
from crew import DataScienceCrew


def setup_environment():
    """Load environment variables and setup paths"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Create necessary directories
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    return reports_dir, data_dir


def validate_csv_path(csv_path: str) -> bool:
    """Validate that the CSV file exists"""
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return False
    
    if not csv_path.endswith('.csv'):
        print(f"Error: File must be a CSV file (got {csv_path})")
        return False
    
    return True


def run_analysis(topic: str, csv_path: str):
    """
    Run the data science multi-agent analysis
    
    Args:
        topic: Business problem description
        csv_path: Path to the CSV dataset
    """
    print("=" * 80)
    print("DATA SCIENCE MULTI-AGENT SYSTEM")
    print("=" * 80)
    print(f"\nBusiness Problem: {topic}")
    print(f"Dataset: {csv_path}")
    print("\nInitializing agents and tasks...")
    print("-" * 80)
    
    # Validate CSV path
    if not validate_csv_path(csv_path):
        sys.exit(1)
    
    try:
        # Initialize the crew
        crew = DataScienceCrew()
        
        # Prepare inputs
        inputs = {
            'topic': topic,
            'csv_path': os.path.abspath(csv_path)
        }
        
        print("\nStarting multi-agent analysis...")
        print("This may take several minutes depending on dataset size and LLM speed.")
        print("-" * 80)
        
        # Run the crew
        result = crew.crew().kickoff(inputs=inputs)
        
        print("\n" + "=" * 80)
        print("ANALYSIS COMPLETE")
        print("=" * 80)
        print(f"\nFinal report saved to: reports/report_final.md")
        print("\nYou can now review the generated technical report.")
        
        return result
        
    except Exception as e:
        print(f"\n\nError during analysis: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Data Science Multi-Agent System - Automated data analysis and reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --topic "Predict customer churn" --csv_path data/churn.csv
  python main.py -t "House price prediction" -c data/housing.csv
  
The system will:
  1. Create a detailed project plan
  2. Perform exploratory data analysis
  3. Propose baseline machine learning models
  4. Generate a comprehensive technical report
        """
    )
    
    parser.add_argument(
        '--topic', '-t',
        required=True,
        help='Business problem description (e.g., "Predict customer churn")'
    )
    
    parser.add_argument(
        '--csv_path', '-c',
        required=True,
        help='Path to the CSV dataset file'
    )
    
    args = parser.parse_args()
    
    # Setup environment
    setup_environment()
    
    # Run the analysis
    run_analysis(args.topic, args.csv_path)


if __name__ == "__main__":
    main()

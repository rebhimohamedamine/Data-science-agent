"""
Data Statistics Tool for Data Science Multi-Agent System
Calculates descriptive statistics, missing values, and cardinalities
"""

from crewai.tools import tool
import pandas as pd
import numpy as np
import os


@tool("Data Statistics Tool")
def data_stats_tool(csv_path: str) -> str:
    """Calculate comprehensive statistics for the dataset.
    
    Args:
        csv_path: Path to the CSV file
        
    Returns:
        Formatted string with statistical analysis
    """
    try:
        # Check if file exists
        if not os.path.exists(csv_path):
            return f"Error: File not found at {csv_path}"
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Separate numerical and categorical columns
        numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        output = []
        output.append("=" * 80)
        output.append("STATISTICAL ANALYSIS")
        output.append("=" * 80)
        output.append(f"\nDataset: {csv_path}")
        output.append(f"Total Rows: {len(df)}")
        output.append(f"Total Columns: {len(df.columns)}")
        output.append(f"Numerical Columns: {len(numerical_cols)}")
        output.append(f"Categorical Columns: {len(categorical_cols)}")
        
        # Overall missing values
        output.append(f"\n{'-' * 80}")
        output.append("MISSING VALUES ANALYSIS")
        output.append(f"{'-' * 80}")
        
        missing_counts = df.isnull().sum()
        missing_percentages = (missing_counts / len(df)) * 100
        
        if missing_counts.sum() == 0:
            output.append("\n✓ No missing values detected in the dataset")
        else:
            output.append("\nColumns with missing values:")
            for col in df.columns:
                if missing_counts[col] > 0:
                    output.append(f"  • {col}: {missing_counts[col]} ({missing_percentages[col]:.2f}%)")
        
        # Numerical statistics
        if numerical_cols:
            output.append(f"\n{'-' * 80}")
            output.append("NUMERICAL VARIABLES STATISTICS")
            output.append(f"{'-' * 80}\n")
            
            for col in numerical_cols:
                output.append(f"\n{col}:")
                output.append(f"  Count:    {df[col].count()}")
                output.append(f"  Mean:     {df[col].mean():.4f}")
                output.append(f"  Median:   {df[col].median():.4f}")
                output.append(f"  Std Dev:  {df[col].std():.4f}")
                output.append(f"  Min:      {df[col].min():.4f}")
                output.append(f"  Q1 (25%): {df[col].quantile(0.25):.4f}")
                output.append(f"  Q2 (50%): {df[col].quantile(0.50):.4f}")
                output.append(f"  Q3 (75%): {df[col].quantile(0.75):.4f}")
                output.append(f"  Max:      {df[col].max():.4f}")
                output.append(f"  Missing:  {missing_counts[col]}")
                
                # Detect potential outliers using IQR method
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
                output.append(f"  Outliers: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")
        
        # Categorical statistics
        if categorical_cols:
            output.append(f"\n{'-' * 80}")
            output.append("CATEGORICAL VARIABLES STATISTICS")
            output.append(f"{'-' * 80}\n")
            
            for col in categorical_cols:
                unique_count = df[col].nunique()
                most_common = df[col].mode()[0] if not df[col].mode().empty else "N/A"
                most_common_count = df[col].value_counts().iloc[0] if len(df[col].value_counts()) > 0 else 0
                
                output.append(f"\n{col}:")
                output.append(f"  Count:           {df[col].count()}")
                output.append(f"  Unique Values:   {unique_count}")
                output.append(f"  Most Frequent:   '{most_common}' ({most_common_count} occurrences)")
                output.append(f"  Missing:         {missing_counts[col]}")
                
                # Show top 5 most frequent values
                output.append(f"  Top 5 Values:")
                value_counts = df[col].value_counts().head(5)
                for idx, (value, count) in enumerate(value_counts.items(), 1):
                    percentage = (count / len(df)) * 100
                    output.append(f"    {idx}. '{value}': {count} ({percentage:.2f}%)")
        
        # Data quality summary
        output.append(f"\n{'-' * 80}")
        output.append("DATA QUALITY SUMMARY")
        output.append(f"{'-' * 80}")
        
        total_cells = len(df) * len(df.columns)
        missing_cells = missing_counts.sum()
        completeness = ((total_cells - missing_cells) / total_cells) * 100
        
        output.append(f"\nData Completeness: {completeness:.2f}%")
        output.append(f"Total Cells: {total_cells}")
        output.append(f"Missing Cells: {missing_cells}")
        output.append(f"Complete Cells: {total_cells - missing_cells}")
        
        # Check for duplicate rows
        duplicates = df.duplicated().sum()
        output.append(f"\nDuplicate Rows: {duplicates} ({duplicates/len(df)*100:.2f}%)")
        
        output.append(f"\n{'=' * 80}\n")
        
        return "\n".join(output)
        
    except Exception as e:
        return f"Error analyzing data: {str(e)}"


# Alias for backward compatibility
calculate_data_stats = data_stats_tool


if __name__ == "__main__":
    # Test the tool
    import sys
    
    if len(sys.argv) > 1:
        test_path = sys.argv[1]
        print(calculate_data_stats(test_path))
    else:
        print("Usage: python data_stats.py <path_to_csv>")

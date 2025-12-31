"""
CSV Reader Tool for Data Science Multi-Agent System
Reads CSV files and extracts basic information about structure and content
"""

from crewai.tools import tool
import pandas as pd
import os


@tool("CSV Reader Tool")
def csv_reader_tool(csv_path: str, num_rows: int = 5) -> str:
    """Read CSV file and return structured information about it.

    Args:
        csv_path: Path to the CSV file
        num_rows: Number of sample rows to return (default 5)

    Returns:
        Formatted string with dataset information
    """
    try:
        # -------------------------------
        # Validate file
        # -------------------------------
        if not os.path.exists(csv_path):
            return f"Error: File not found at {csv_path}"

        # -------------------------------
        # Load CSV
        # -------------------------------
        df = pd.read_csv(csv_path)

        # -------------------------------
        # Dataset metadata
        # -------------------------------
        num_rows_total = len(df)
        num_cols = df.shape[1]
        data_types = df.dtypes

        num_rows = int(num_rows)
        num_rows = min(num_rows, num_rows_total)
        sample_rows = df.head(num_rows)

        # -------------------------------
        # Format output
        # -------------------------------
        output = []
        output.append("=" * 80)
        output.append("CSV FILE INFORMATION")
        output.append("=" * 80)
        output.append(f"\nFile: {csv_path}")
        output.append(f"Dataset Shape: {num_rows_total} rows × {num_cols} columns")

        output.append("\n" + "-" * 80)
        output.append("COLUMNS AND DATA TYPES:")
        output.append("-" * 80)

        for i, (col, dtype) in enumerate(data_types.items(), 1):
            output.append(f"{i:3d}. {col:30s} - {dtype}")

        output.append("\n" + "-" * 80)
        output.append(f"SAMPLE ROWS (first {num_rows}):")
        output.append("-" * 80)
        output.append(sample_rows.to_string(index=False))
        output.append("\n" + "=" * 80)

        return "\n".join(output)

    except Exception as e:
        return f"Error reading CSV file: {str(e)}"


# Alias for backward compatibility
read_csv_info = csv_reader_tool


# -------------------------------
# Standalone test
# -------------------------------
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        test_path = sys.argv[1]
        print(read_csv_info(test_path))
    else:
        print("Usage: python csv_reader.py <path_to_csv>")

# Data Directory

Place your CSV datasets here for analysis.

## Sample Data

Generate sample data using:
```bash
python generate_sample_data.py
```

This creates `sample_churn.csv` - a synthetic customer churn dataset with:
- 1000 customer records
- 15 features (demographics, usage, service info)
- Binary classification target (churn: Yes/No)

## Your Own Data

You can use any tabular CSV dataset. Requirements:

### Data Format
- ✓ CSV format (.csv extension)
- ✓ First row contains column headers
- ✓ No special characters in column names (use underscores)
- ✓ Consistent data types per column

### Recommended Size
- **Minimum**: 100 rows
- **Optimal**: 1,000 - 10,000 rows
- **Maximum**: 100,000 rows (larger files take longer)

### Data Quality
- Clean column names
- Reasonable number of features (< 50 recommended)
- Mix of numerical and categorical features
- Target variable present (if classification/regression)

## Example Datasets

You can download datasets from:
- **Kaggle**: https://www.kaggle.com/datasets
  - Titanic (classification)
  - House Prices (regression)
  - Credit Card Fraud (classification)
- **UCI ML Repository**: https://archive.ics.uci.edu/ml
- **OpenML**: https://www.openml.org/

## Popular Dataset Examples

### Classification
- Customer churn prediction
- Credit default prediction
- Disease diagnosis
- Sentiment analysis
- Image classification

### Regression
- House price prediction
- Sales forecasting
- Stock price prediction
- Temperature forecasting

## Usage

```bash
# Place your CSV in this directory
cp ~/Downloads/my_dataset.csv data/

# Run analysis
python main.py --topic "Your problem description" --csv_path data/my_dataset.csv
```

## Notes

- Data files are ignored by git by default
- Ensure you have rights to use the data
- Consider data privacy and security
- Large files (>100MB) may cause memory issues

"""
Sample dataset generator for testing the Data Science Multi-Agent System
Creates a sample customer churn dataset
"""

import pandas as pd
import numpy as np
from pathlib import Path


def generate_churn_dataset(n_samples=1000, output_path='data/sample_churn.csv'):
    """
    Generate a sample customer churn dataset
    
    Args:
        n_samples: Number of samples to generate
        output_path: Path to save the CSV file
    """
    np.random.seed(42)
    
    # Generate features
    data = {
        'customer_id': range(1, n_samples + 1),
        'age': np.random.randint(18, 80, n_samples),
        'gender': np.random.choice(['Male', 'Female'], n_samples),
        'tenure_months': np.random.randint(1, 72, n_samples),
        'monthly_charges': np.random.uniform(20, 150, n_samples).round(2),
        'total_charges': None,  # Will calculate
        'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], 
                                         n_samples, p=[0.5, 0.3, 0.2]),
        'payment_method': np.random.choice(['Electronic check', 'Mailed check', 
                                           'Bank transfer', 'Credit card'], n_samples),
        'internet_service': np.random.choice(['DSL', 'Fiber optic', 'No'], 
                                            n_samples, p=[0.4, 0.4, 0.2]),
        'online_security': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'tech_support': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'streaming_tv': np.random.choice(['Yes', 'No', 'No internet service'], n_samples),
        'paperless_billing': np.random.choice(['Yes', 'No'], n_samples),
        'num_support_calls': np.random.poisson(2, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Calculate total charges
    df['total_charges'] = (df['monthly_charges'] * df['tenure_months']).round(2)
    
    # Generate churn based on some logic (more realistic)
    churn_probability = (
        0.1 +  # Base probability
        0.3 * (df['contract_type'] == 'Month-to-month').astype(int) +
        0.2 * (df['tenure_months'] < 12).astype(int) +
        0.15 * (df['num_support_calls'] > 4).astype(int) +
        0.1 * (df['monthly_charges'] > 100).astype(int) -
        0.2 * (df['online_security'] == 'Yes').astype(int) -
        0.15 * (df['tech_support'] == 'Yes').astype(int)
    )
    churn_probability = np.clip(churn_probability, 0, 1)
    df['churn'] = (np.random.random(n_samples) < churn_probability).astype(int)
    df['churn'] = df['churn'].map({0: 'No', 1: 'Yes'})
    
    # Add some missing values (realistic)
    missing_indices = np.random.choice(df.index, size=int(0.02 * n_samples), replace=False)
    df.loc[missing_indices, 'total_charges'] = np.nan
    
    # Create directory if it doesn't exist
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"Generated sample dataset with {n_samples} rows")
    print(f"Saved to: {output_path}")
    print(f"\nDataset Info:")
    print(f"  - Features: {len(df.columns)}")
    print(f"  - Churn Rate: {(df['churn'] == 'Yes').sum() / len(df) * 100:.1f}%")
    print(f"  - Missing Values: {df.isnull().sum().sum()}")
    
    return df


if __name__ == "__main__":
    # Generate sample dataset
    df = generate_churn_dataset(n_samples=1000)
    print("\nFirst few rows:")
    print(df.head())
    print("\nDataset statistics:")
    print(df.describe())

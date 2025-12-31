# Data Science Multi-Agent System

A comprehensive multi-agent AI system designed to assist data science teams with automated exploratory data analysis, modeling, and report generation using CrewAI.

## Overview

This system leverages multiple specialized AI agents that collaborate to:
- Transform business descriptions into structured data science plans
- Perform exploratory data analysis on tabular datasets
- Propose and evaluate baseline machine learning models
- Generate comprehensive technical reports

## Architecture

### Agents

#### 1. **Project Planner Agent**
- **Role**: Strategic Data Science Planner
- **Goal**: Transform business requirements into actionable data science plans
- **Backstory**: An experienced project manager with deep expertise in data science methodologies. Excels at breaking down complex problems into well-defined steps: exploratory data analysis (EDA), modeling, evaluation, and reporting.
- **Output**: Detailed work plan with clear milestones

#### 2. **Data Analyst Agent**
- **Role**: Expert Data Analyst
- **Goal**: Conduct thorough exploratory data analysis and extract meaningful insights
- **Backstory**: A seasoned statistician with years of experience analyzing complex datasets. Specializes in identifying patterns, anomalies, and relationships in data. Masters statistical techniques and data visualization principles.
- **Tools**: CSVReaderTool, DataStatsTool
- **Output**: Structured exploratory analysis report

#### 3. **Modelling Agent**
- **Role**: Machine Learning Engineer
- **Goal**: Design and propose baseline machine learning models with appropriate evaluation metrics
- **Backstory**: An ML expert with extensive knowledge of various algorithms from traditional machine learning to deep learning. Understands which models work best for different problem types and how to properly evaluate them.
- **Output**: Model proposals with evaluation strategies

#### 4. **Report Writer Agent**
- **Role**: Technical Report Specialist
- **Goal**: Synthesize all findings into a coherent, professional technical report
- **Backstory**: A technical writer with strong scientific background. Excels at transforming complex technical analyses into clear, well-structured documentation that serves both technical and business audiences.
- **Output**: Complete technical report in Markdown or LaTeX format

### System Workflow

```
Business Description + CSV Dataset
         ↓
   Project Planner
         ↓ (Work Plan)
   Data Analyst + Tools (CSV Reader, Stats)
         ↓ (EDA Report)
   Modelling Agent
         ↓ (Model Proposals + Metrics)
   Report Writer
         ↓
   Final Technical Report
```

## Components

### Tasks

1. **Task 1 - Planning**: Generate detailed data science project plan
   - Input: Business description
   - Output: Structured plan with EDA, modeling, and evaluation steps

2. **Task 2 - Exploratory Analysis**: Perform comprehensive EDA
   - Input: Work plan + CSV dataset
   - Output: Statistical analysis with insights

3. **Task 3 - Model Design**: Propose baseline models
   - Input: EDA results
   - Output: 2-3 model recommendations with evaluation metrics

4. **Task 4 - Report Generation**: Create final technical report
   - Input: All previous outputs
   - Output: Complete technical report (Markdown/LaTeX)

### Tools

- **CSVReaderTool**: Reads CSV files, extracts column names and sample rows
- **DataStatsTool**: Calculates descriptive statistics, identifies missing values, computes cardinalities

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys (OpenAI, Groq, or local LLM)
```

## Usage

```bash
python main.py --topic "Predict customer churn" --csv_path "data/customers.csv"
```

Or use the interactive mode:

```python
from crew import DataScienceCrew

crew = DataScienceCrew()
result = crew.run(
    topic="Customer churn prediction for telecom company",
    csv_path="data/telecom_churn.csv"
)

# Report saved to reports/report_final.md
```

## Configuration

Edit `.env` to configure:
- LLM provider (OpenAI, Groq, local model)
- Model name (gpt-4, llama-3.1-70b, etc.)
- Temperature and other parameters

## Requirements

- Python 3.10+
- CrewAI
- Pandas
- NumPy
- Scikit-learn
- LangChain

## Project Structure

```
.
├── README.md                 # This file
├── ARCHITECTURE.md           # Detailed architecture documentation
├── main.py                   # Main execution script
├── crew.py                   # Crew orchestration
├── agents.yaml               # Agent definitions
├── tasks.yaml                # Task definitions
├── tools/
│   ├── __init__.py
│   ├── csv_reader.py        # CSV reading tool
│   └── data_stats.py        # Statistical analysis tool
├── reports/                  # Generated reports directory
├── data/                     # Sample datasets directory
├── requirements.txt          # Python dependencies
└── .env.example             # Environment template
```

## Example Output

The system generates a comprehensive technical report including:
- Executive summary
- Dataset description
- Exploratory data analysis with statistics
- Model recommendations (e.g., Logistic Regression, Random Forest, XGBoost)
- Evaluation metrics (Accuracy, F1-score, RMSE, etc.)
- Conclusions and recommendations

## License

MIT License

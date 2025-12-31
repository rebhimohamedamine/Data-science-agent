# System Architecture - Data Science Multi-Agent

## System Overview

This multi-agent system implements a collaborative AI framework where specialized agents work together to solve data science problems. The architecture follows a sequential pipeline with information flowing from planning to analysis to modeling to reporting.

## Agents Description

### 1. Project Planner Agent

**Role**: Strategic Data Science Planner

**Goal**: Transform business requirements and problem descriptions into structured, actionable data science work plans. Break down complex analytical tasks into manageable steps.

**Backstory**: An experienced data science project manager with over 10 years leading analytical projects across various industries. Has deep expertise in CRISP-DM methodology, agile data science practices, and understanding what steps are needed to move from business question to analytical insight. Skilled at identifying the right sequence of activities: exploratory data analysis (EDA), feature engineering, modeling approaches, validation strategies, and reporting requirements.

**Capabilities**:
- Decompose business problems into technical tasks
- Identify data requirements and potential challenges
- Define success criteria and evaluation metrics
- Create structured timelines for analysis phases

**Outputs**:
- Detailed project plan with phases and milestones
- List of analytical objectives
- Potential risks and mitigation strategies

---

### 2. Data Analyst Agent

**Role**: Expert Data Analyst

**Goal**: Conduct thorough exploratory data analysis to understand dataset characteristics, identify patterns, detect anomalies, and extract meaningful statistical insights that inform modeling decisions.

**Backstory**: A highly skilled statistician and data analyst with 8 years of experience working with diverse datasets in finance, healthcare, and e-commerce domains. Expert in descriptive statistics, data quality assessment, and identifying relationships between variables. Known for meticulous attention to data quality issues and ability to spot subtle patterns that others miss. Uses both statistical rigor and intuitive understanding of data behavior.

**Tools Used**:
- **CSVReaderTool**: To load and inspect dataset structure
- **DataStatsTool**: To compute descriptive statistics and summaries

**Capabilities**:
- Load and inspect tabular data
- Calculate descriptive statistics (mean, median, std, quartiles)
- Identify missing values and data quality issues
- Analyze variable distributions and cardinalities
- Detect outliers and anomalies
- Identify correlations and relationships

**Outputs**:
- Dataset description (dimensions, variables, types)
- Descriptive statistics for numerical features
- Frequency distributions for categorical features
- Missing value analysis
- Data quality assessment
- Preliminary insights and observations

---

### 3. Modelling Agent

**Role**: Machine Learning Engineer

**Goal**: Design appropriate machine learning solutions by proposing 2-3 baseline models suited to the problem type, defining proper evaluation metrics, and establishing model selection criteria.

**Backstory**: A machine learning engineer with comprehensive knowledge of both classical ML algorithms and modern deep learning techniques. Holds a Ph.D. in Computer Science with specialization in machine learning. Has successfully deployed models in production environments and understands the trade-offs between model complexity, interpretability, and performance. Expert in model selection, hyperparameter tuning, and understanding which algorithms work best for different problem types (classification, regression, clustering, etc.).

**Capabilities**:
- Identify problem type (classification, regression, etc.)
- Recommend suitable baseline models
- Define appropriate evaluation metrics
- Suggest train-test split strategies
- Propose cross-validation approaches
- Consider model interpretability vs. performance trade-offs

**Model Recommendations Include**:
- **For Classification**: Logistic Regression, Random Forest, XGBoost, SVM
- **For Regression**: Linear Regression, Random Forest Regressor, Gradient Boosting
- **Metrics**: Accuracy, Precision, Recall, F1-score, ROC-AUC, RMSE, MAE, R²

**Outputs**:
- Problem type identification
- 2-3 baseline model recommendations with justification
- Evaluation metrics definition
- Model training strategy
- Expected performance considerations

---

### 4. Report Writer Agent

**Role**: Technical Report Specialist

**Goal**: Synthesize all analytical findings, model recommendations, and insights into a comprehensive, well-structured technical report that communicates results clearly to both technical and business stakeholders.

**Backstory**: A technical writer with 6 years of experience in data science and machine learning domains. Has a background in both computer science and technical communication. Excels at transforming complex statistical analyses and model outputs into clear, compelling narratives. Understands how to structure technical documents following academic and industry standards. Skilled in LaTeX and Markdown for professional document preparation.

**Capabilities**:
- Synthesize information from multiple sources
- Structure reports following scientific methodology
- Create clear section hierarchies
- Write technical content for mixed audiences
- Format reports in Markdown or LaTeX
- Include appropriate visualizations descriptions

**Report Structure**:
1. **Introduction**: Problem statement and objectives
2. **Data Description**: Dataset overview and characteristics
3. **Exploratory Data Analysis**: Statistical findings and insights
4. **Methodology**: Proposed models and evaluation approach
5. **Expected Results**: Performance metrics and interpretation
6. **Discussion**: Insights, limitations, and recommendations
7. **Conclusion**: Summary and next steps

**Outputs**:
- Complete technical report (Markdown or LaTeX)
- Professional formatting with sections and subsections
- Clear visualizations references
- Actionable recommendations

---

## Information Flow Diagram

```
┌─────────────────────────────────────────────────────────┐
│  INPUT: Business Description + CSV Dataset Path        │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────────┐
│  AGENT 1: Project Planner                                │
│  • Analyzes business requirements                        │
│  • Creates structured work plan                          │
│  • Defines objectives and success criteria               │
└──────────────────┬───────────────────────────────────────┘
                   │
                   │ Document: Project Plan
                   │
                   ▼
┌──────────────────────────────────────────────────────────┐
│  AGENT 2: Data Analyst                                   │
│  Tools: [CSVReaderTool, DataStatsTool]                   │
│  • Loads and inspects dataset                            │
│  • Computes descriptive statistics                       │
│  • Identifies data quality issues                        │
│  • Produces EDA report                                   │
└──────────────────┬───────────────────────────────────────┘
                   │
                   │ Document: EDA Report
                   │
                   ▼
┌──────────────────────────────────────────────────────────┐
│  AGENT 3: Modelling Agent                                │
│  • Reviews EDA findings                                  │
│  • Proposes 2-3 baseline models                          │
│  • Defines evaluation metrics                            │
│  • Outlines validation strategy                          │
└──────────────────┬───────────────────────────────────────┘
                   │
                   │ Document: Model Proposals
                   │
                   ▼
┌──────────────────────────────────────────────────────────┐
│  AGENT 4: Report Writer                                  │
│  • Collects all previous outputs                         │
│  • Synthesizes into coherent narrative                   │
│  • Formats as professional technical report              │
│  • Adds structure, sections, and conclusions             │
└──────────────────┬───────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────────┐
│  OUTPUT: report_final.md (or .tex)                       │
│  Complete technical report ready for stakeholders        │
└──────────────────────────────────────────────────────────┘
```

## Task Dependencies

```
Task 1 (Planning)
    ↓ depends on
Task 2 (EDA) 
    ↓ depends on
Task 3 (Modeling)
    ↓ depends on
Task 4 (Reporting)
```

## Tool Architecture

### CSVReaderTool
- **Purpose**: Load CSV files and extract basic structure
- **Inputs**: File path
- **Outputs**: Column names, data types, sample rows
- **Used by**: Data Analyst Agent

### DataStatsTool
- **Purpose**: Compute statistical summaries
- **Inputs**: CSV file path, column names
- **Outputs**: Mean, median, std, min, max, quartiles, missing values, cardinalities
- **Used by**: Data Analyst Agent

## Technology Stack

- **Framework**: CrewAI
- **LLM**: Configurable (OpenAI GPT-4, Groq Llama-3, local models via Ollama)
- **Data Processing**: Pandas, NumPy
- **ML References**: Scikit-learn (for model recommendations)
- **Configuration**: YAML for agents and tasks
- **Output Format**: Markdown or LaTeX

## Design Principles

1. **Separation of Concerns**: Each agent has a specific, well-defined role
2. **Sequential Processing**: Tasks execute in logical order with clear dependencies
3. **Tool Isolation**: Only the Data Analyst agent uses tools (as specified)
4. **Configurability**: YAML-based configuration for easy modification
5. **Reproducibility**: Structured outputs enable consistent report generation

## Extension Points

Future enhancements could include:
- Additional tools for data visualization generation
- Model training and evaluation agent
- Hyperparameter tuning agent
- Feature engineering agent
- Deployment preparation agent

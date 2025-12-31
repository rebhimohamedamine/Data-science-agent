# Quick Start Guide

## Installation

1. **Clone or download this project**

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API key
# For OpenAI:
OPENAI_API_KEY=your-key-here

# Or for Groq (fast and free tier available):
# GROQ_API_KEY=your-key-here
# LLM_PROVIDER=groq
```

## Quick Test

### Step 1: Generate Sample Data
```bash
python generate_sample_data.py
```

This creates `data/sample_churn.csv` with 1000 customer records.

### Step 2: Run Analysis
```bash
python main.py --topic "Predict customer churn for telecom company" --csv_path data/sample_churn.csv
```

### Step 3: View Results
The system will generate a comprehensive report at:
```
reports/report_final.md
```

## Using Your Own Data

```bash
python main.py --topic "Your business problem description" --csv_path path/to/your/data.csv
```

**Example topics:**
- "Predict house prices based on property features"
- "Classify credit card fraud transactions"
- "Forecast monthly sales revenue"
- "Segment customers for targeted marketing"

## What Happens During Execution

The system runs 4 sequential tasks:

1. **Planning** (1-2 min): Creates project plan
2. **EDA** (2-3 min): Analyzes dataset with tools
3. **Modeling** (1-2 min): Proposes ML models
4. **Reporting** (2-3 min): Generates final report

**Total time: ~8-10 minutes** (depends on LLM speed)

## LLM Provider Options

### OpenAI (Recommended for quality)
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL_NAME=gpt-4-turbo-preview
```

### Groq (Recommended for speed - free tier available)
```env
LLM_PROVIDER=groq
GROQ_API_KEY=gsk_...
GROQ_MODEL_NAME=llama-3.1-70b-versatile
```

### Ollama (Local - free but slower)
```bash
# Install Ollama first: https://ollama.ai
ollama pull llama3.1:70b

# In .env:
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.1:70b
```

## Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "API key not found"
Make sure `.env` file exists and contains your API key.

### "CSV file not found"
Check the path to your CSV file. Use absolute path if needed.

### Agents not using tools
This is expected - only the Data Analyst agent uses the CSVReader and DataStats tools.

## Project Structure
```
.
├── main.py              # Run this
├── crew.py              # Crew orchestration
├── agents.yaml          # Agent definitions
├── tasks.yaml           # Task definitions
├── tools/               # Custom tools
│   ├── csv_reader.py
│   └── data_stats.py
├── data/                # Your datasets
├── reports/             # Generated reports
└── requirements.txt     # Dependencies
```

## Next Steps

1. Try with your own dataset
2. Modify agent backstories in `agents.yaml`
3. Adjust task descriptions in `tasks.yaml`
4. Add more custom tools in `tools/`
5. Experiment with different LLM models

## Support

For issues or questions:
- Check ARCHITECTURE.md for system design
- Review agents.yaml and tasks.yaml for configuration
- Ensure your CSV has proper format (headers, no special characters)

## Tips for Best Results

1. **Clear topic**: Be specific about your business problem
2. **Clean data**: Ensure CSV is well-formatted
3. **Appropriate size**: 100-10,000 rows works best
4. **Good features**: Include relevant columns for analysis
5. **Patience**: Let the system complete all 4 tasks

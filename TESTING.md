# Testing Guide for Data Science Multi-Agent System

## Quick Test Checklist

Follow these steps to verify the system works correctly:

### ✅ Step 1: Environment Setup

```bash
# Check Python version (3.10+ required)
python --version

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import crewai; print('CrewAI installed:', crewai.__version__)"
python -c "import pandas; print('Pandas installed:', pandas.__version__)"
```

### ✅ Step 2: Configure API Key

```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your API key
# Option 1: OpenAI (recommended for quality)
OPENAI_API_KEY=sk-your-key-here

# Option 2: Groq (recommended for speed - free tier available)
# GROQ_API_KEY=gsk-your-key-here
# LLM_PROVIDER=groq
```

**Get Free API Keys:**
- OpenAI: https://platform.openai.com/api-keys (paid)
- Groq: https://console.groq.com/keys (free tier available)

### ✅ Step 3: Test Tools Independently

```bash
# Generate sample data
python generate_sample_data.py

# Test CSV Reader Tool
python tools/csv_reader.py data/sample_churn.csv

# Test Data Stats Tool
python tools/data_stats.py data/sample_churn.csv
```

**Expected Output:**
- Sample data generated with 1000 rows
- CSV reader shows columns and sample rows
- Data stats shows statistical summaries

### ✅ Step 4: Test Full System

```bash
# Run complete analysis (this takes 8-10 minutes)
python main.py --topic "Predict customer churn for telecom company" --csv_path data/sample_churn.csv
```

**What You Should See:**
1. System initialization message
2. Agent 1 (Project Planner) working...
3. Agent 2 (Data Analyst) working with tools...
4. Agent 3 (Modelling Agent) working...
5. Agent 4 (Report Writer) working...
6. "ANALYSIS COMPLETE" message
7. Report saved to `reports/report_final.md`

### ✅ Step 5: Verify Output

```bash
# Check if report was generated
ls -la reports/report_final.md

# View the report
cat reports/report_final.md
# or open in your editor/browser
```

**Expected Report Sections:**
- Executive Summary
- Introduction
- Data Description
- Exploratory Data Analysis
- Methodology (with 2-3 models)
- Expected Results
- Discussion
- Conclusion

---

## Troubleshooting

### Issue: "Module 'crewai' not found"

**Solution:**
```bash
pip install --upgrade crewai crewai-tools
```

### Issue: "API key not found"

**Solution:**
```bash
# Make sure .env file exists
ls .env

# Check content (should show OPENAI_API_KEY=...)
cat .env

# Verify it's not .env.example
mv .env.example .env  # if needed
```

### Issue: "CSV file not found"

**Solution:**
```bash
# Generate sample data first
python generate_sample_data.py

# Or use absolute path
python main.py --topic "..." --csv_path "C:\full\path\to\data.csv"
```

### Issue: Agents not using tools

**Verification:**
- This is expected! Only the Data Analyst agent uses tools
- Check the verbose output during Task 2 (EDA)
- You should see tool calls like "Using CSVReaderTool" and "Using DataStatsTool"

### Issue: "Rate limit exceeded"

**Solution:**
- If using OpenAI, wait a few minutes
- Consider switching to Groq (faster, generous free tier)
- Or use local Ollama (free, no rate limits)

### Issue: Report is empty or incomplete

**Solution:**
- Check that all 4 tasks completed successfully
- Review terminal output for errors
- Ensure your LLM has enough context length (4k+ tokens)
- Try with a smaller dataset first

---

## Validation Checklist

After running the system, verify:

| Component | Check | Expected Result |
|-----------|-------|-----------------|
| **Agents** | agents.yaml exists | ✅ 4 agents defined |
| **Tasks** | tasks.yaml exists | ✅ 4 tasks defined |
| **Tools** | tools/ directory | ✅ 2 tools present |
| **Sample Data** | data/sample_churn.csv | ✅ 1000 rows, 15 columns |
| **Report** | reports/report_final.md | ✅ 2000+ words, 7 sections |
| **Tool Usage** | Terminal output | ✅ Tools called in Task 2 |
| **Agent Flow** | Terminal output | ✅ 4 tasks executed sequentially |

---

## Performance Benchmarks

**With GPT-4:**
- Task 1 (Planning): ~60-90 seconds
- Task 2 (EDA): ~90-120 seconds (uses tools)
- Task 3 (Modeling): ~60-90 seconds
- Task 4 (Report): ~90-120 seconds
- **Total: 5-7 minutes**

**With Groq (Llama 3.1 70B):**
- Task 1: ~30-45 seconds
- Task 2: ~45-60 seconds
- Task 3: ~30-45 seconds
- Task 4: ~45-60 seconds
- **Total: 2.5-3.5 minutes**

**With Local Ollama:**
- Depends on hardware
- Expect 2-3x slower than cloud models
- **Total: 10-20 minutes**

---

## Testing Different Datasets

### Test with Classification Problem

```bash
# Use the provided churn dataset
python main.py \
  --topic "Predict customer churn with focus on retention strategies" \
  --csv_path data/sample_churn.csv
```

### Test with Your Own Data

```bash
# Example: House prices
python main.py \
  --topic "Predict house prices based on property features" \
  --csv_path /path/to/housing.csv

# Example: Credit risk
python main.py \
  --topic "Assess credit default risk for loan applications" \
  --csv_path /path/to/credit_data.csv
```

---

## Advanced Testing

### Test Individual Components

**Test Agent Definition:**
```python
from crew import DataScienceCrew

crew_instance = DataScienceCrew()
planner = crew_instance.project_planner()
print(f"Agent: {planner.role}")
print(f"Goal: {planner.goal}")
```

**Test Tool Directly:**
```python
from tools.csv_reader import CSVReaderTool

tool = CSVReaderTool()
result = tool._run(csv_path="data/sample_churn.csv", num_rows=3)
print(result)
```

**Test Task Definition:**
```python
from crew import DataScienceCrew

crew_instance = DataScienceCrew()
planning = crew_instance.planning_task()
print(f"Task: {planning.description}")
```

### Verify YAML Syntax

```bash
# Install yamllint (optional)
pip install yamllint

# Check YAML files
yamllint agents.yaml
yamllint tasks.yaml
```

---

## Expected Terminal Output Example

```
================================================================================
DATA SCIENCE MULTI-AGENT SYSTEM
================================================================================

Business Problem: Predict customer churn for telecom company
Dataset: data/sample_churn.csv

Initializing agents and tasks...
--------------------------------------------------------------------------------

Starting multi-agent analysis...
This may take several minutes depending on dataset size and LLM speed.
--------------------------------------------------------------------------------

[2025-12-27 10:30:15] Starting Task: planning_task
[2025-12-27 10:30:15] Agent: Project Planner
[2025-12-27 10:31:45] Completed: Project plan with objectives and milestones

[2025-12-27 10:31:46] Starting Task: exploratory_analysis_task
[2025-12-27 10:31:46] Agent: Data Analyst
[2025-12-27 10:31:50] Using CSVReaderTool on data/sample_churn.csv
[2025-12-27 10:31:52] Using DataStatsTool on data/sample_churn.csv
[2025-12-27 10:33:30] Completed: EDA report with statistics

[2025-12-27 10:33:31] Starting Task: modeling_proposal_task
[2025-12-27 10:33:31] Agent: Modelling Agent
[2025-12-27 10:35:00] Completed: Model proposals (3 models)

[2025-12-27 10:35:01] Starting Task: report_generation_task
[2025-12-27 10:35:01] Agent: Report Writer
[2025-12-27 10:37:15] Completed: Final technical report

================================================================================
ANALYSIS COMPLETE
================================================================================

Final report saved to: reports/report_final.md

You can now review the generated technical report.
```

---

## Success Criteria

Your system is working correctly if:

✅ All dependencies install without errors  
✅ Tools can read and analyze CSV files independently  
✅ All 4 agents execute in sequence  
✅ Data Analyst agent uses both tools  
✅ Final report is generated (2000+ words)  
✅ Report includes all required sections  
✅ Report contains actual data insights (not generic)  
✅ Model recommendations are appropriate for problem type  

---

## Next Steps After Testing

1. **Try with different datasets** - Test robustness
2. **Modify agent backstories** - Customize expertise
3. **Adjust task descriptions** - Fine-tune outputs
4. **Add more tools** - Extend functionality
5. **Experiment with LLM models** - Compare quality/speed
6. **Create visualizations** - Add plotting tools
7. **Implement actual training** - Add ML training agent

---

## Quick Reference Commands

```bash
# Setup
pip install -r requirements.txt
cp .env.example .env

# Generate sample data
python generate_sample_data.py

# Test tools
python tools/csv_reader.py data/sample_churn.csv
python tools/data_stats.py data/sample_churn.csv

# Run full analysis
python main.py --topic "Your problem" --csv_path data/your_data.csv

# View report
cat reports/report_final.md
```

---

## Support

If you encounter issues:

1. Check this testing guide
2. Review ARCHITECTURE.md for system design
3. Check QUICKSTART.md for setup steps
4. Verify .env configuration
5. Ensure CSV file is properly formatted
6. Check terminal output for specific error messages

---

**Happy Testing! 🧪🚀**

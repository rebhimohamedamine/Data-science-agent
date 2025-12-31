# System Architecture Diagram

## Multi-Agent Collaboration Flow

```
                    ┌─────────────────────────────────────┐
                    │         USER INPUT                  │
                    │  - Business Problem Description     │
                    │  - Path to CSV Dataset              │
                    └────────────┬────────────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────────────────┐
                    │      CREWAI ORCHESTRATOR            │
                    │   (Sequential Process Management)   │
                    └────────────┬────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        │         STEP 1: PLANNING                        │
        │                        │                        │
        │    ┌───────────────────▼──────────────────┐    │
        │    │  Agent 1: PROJECT PLANNER            │    │
        │    │  Role: Strategic DS Planner          │    │
        │    │  Tools: None                         │    │
        │    │                                      │    │
        │    │  Actions:                            │    │
        │    │  • Analyze business problem          │    │
        │    │  • Define objectives                 │    │
        │    │  • Create work plan                  │    │
        │    │  • Identify success criteria         │    │
        │    └───────────────────┬──────────────────┘    │
        │                        │                        │
        │           Output: PROJECT PLAN DOCUMENT         │
        │                        │                        │
        └────────────────────────┼────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        │      STEP 2: EXPLORATORY DATA ANALYSIS          │
        │                        │                        │
        │    ┌───────────────────▼──────────────────┐    │
        │    │  Agent 2: DATA ANALYST               │    │
        │    │  Role: Expert Data Analyst           │    │
        │    │  Tools: ✓ CSVReaderTool              │    │
        │    │         ✓ DataStatsTool              │    │
        │    │                                      │    │
        │    │  Actions:                            │    │
        │    │  • Load CSV using CSVReaderTool      │    │
        │    │  • Calculate stats with DataStats    │    │
        │    │  • Identify patterns & anomalies     │    │
        │    │  • Assess data quality               │    │
        │    │  • Generate insights                 │    │
        │    └───────────────────┬──────────────────┘    │
        │                        │                        │
        │         Output: EDA REPORT (Statistics + Insights)
        │                        │                        │
        └────────────────────────┼────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        │       STEP 3: MODEL DESIGN & STRATEGY           │
        │                        │                        │
        │    ┌───────────────────▼──────────────────┐    │
        │    │  Agent 3: MODELLING AGENT            │    │
        │    │  Role: ML Engineer                   │    │
        │    │  Tools: None                         │    │
        │    │                                      │    │
        │    │  Actions:                            │    │
        │    │  • Review EDA findings               │    │
        │    │  • Identify problem type             │    │
        │    │  • Propose 2-3 baseline models       │    │
        │    │  • Define evaluation metrics         │    │
        │    │  • Design validation strategy        │    │
        │    └───────────────────┬──────────────────┘    │
        │                        │                        │
        │      Output: MODEL PROPOSALS + METRICS          │
        │                        │                        │
        └────────────────────────┼────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        │      STEP 4: REPORT GENERATION                  │
        │                        │                        │
        │    ┌───────────────────▼──────────────────┐    │
        │    │  Agent 4: REPORT WRITER              │    │
        │    │  Role: Technical Report Specialist   │    │
        │    │  Tools: None                         │    │
        │    │                                      │    │
        │    │  Actions:                            │    │
        │    │  • Collect all previous outputs      │    │
        │    │  • Synthesize information            │    │
        │    │  • Structure sections logically      │    │
        │    │  • Format in Markdown/LaTeX          │    │
        │    │  • Add conclusions & recommendations │    │
        │    └───────────────────┬──────────────────┘    │
        │                        │                        │
        │    Output: FINAL TECHNICAL REPORT (.md/.tex)   │
        │                        │                        │
        └────────────────────────┼────────────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────────────────┐
                    │       DELIVERABLE                   │
                    │  reports/report_final.md            │
                    │                                     │
                    │  Complete technical report with:    │
                    │  • Executive Summary                │
                    │  • Data Description                 │
                    │  • EDA Findings                     │
                    │  • Model Recommendations            │
                    │  • Evaluation Strategy              │
                    │  • Discussion & Conclusions         │
                    └─────────────────────────────────────┘
```

## Agent Communication Pattern

```
Project Plan
     │
     ├─────────► Data Analyst (uses plan + CSV)
     │                │
     │                │ EDA Report
     │                │
     ├────────────────┼─────────► Modelling Agent
     │                │                 │
     │                │                 │ Model Proposals
     │                │                 │
     └────────────────┴─────────────────┴─────► Report Writer
                                                      │
                                                      ▼
                                              Final Report
```

## Tool Usage Pattern

```
                    CSV Dataset
                         │
                         │
         ┌───────────────┴───────────────┐
         │                               │
         ▼                               ▼
   CSVReaderTool                   DataStatsTool
         │                               │
         │ - Column names                │ - Mean, median, std
         │ - Data types                  │ - Missing values
         │ - Sample rows                 │ - Quartiles
         │ - Shape info                  │ - Cardinalities
         │                               │ - Outliers
         └───────────────┬───────────────┘
                         │
                         ▼
                   Data Analyst Agent
                         │
                         ▼
                   EDA Report
```

## Task Dependencies

```
Task 1: Planning Task
   ├─ Input: topic, csv_path
   ├─ Agent: Project Planner
   └─ Output: Work plan
         │
         ├─ context for ──► Task 2: Exploratory Analysis Task
         │                     ├─ Input: topic, csv_path, plan
         │                     ├─ Agent: Data Analyst (+ Tools)
         │                     └─ Output: EDA report
         │                           │
         │                           ├─ context for ──► Task 3: Modeling Task
         ├───────────────────────────┤                     ├─ Input: topic, EDA, plan
         │                           │                     ├─ Agent: Modelling Agent
         │                           │                     └─ Output: Model proposals
         │                           │                           │
         │                           │                           ├─ context for ──► Task 4: Report Task
         ├───────────────────────────┼───────────────────────────┤                     ├─ Input: All previous
         │                           │                           │                     ├─ Agent: Report Writer
         │                           │                           │                     └─ Output: Final report
         └───────────────────────────┴───────────────────────────┘
```

## Information Flow Detail

| Stage | Agent | Receives | Produces | Tools Used |
|-------|-------|----------|----------|------------|
| 1 | Project Planner | Business description, CSV path | Detailed project plan | None |
| 2 | Data Analyst | Plan, CSV path | EDA report with statistics | CSVReaderTool, DataStatsTool |
| 3 | Modelling Agent | Plan, EDA report | Model proposals, metrics | None |
| 4 | Report Writer | Plan, EDA, Models | Complete technical report | None |

## Key Design Principles

1. **Sequential Processing**: Each task builds on previous results
2. **Tool Isolation**: Only Data Analyst uses tools (as specified)
3. **Context Sharing**: Each agent receives relevant outputs from predecessors
4. **Specialization**: Each agent has distinct role and expertise
5. **Structured Output**: Each task produces well-defined deliverable

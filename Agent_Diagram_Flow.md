User Goal                                             

↓

LLM

↓

Need Tool?

↓

Yes

↓

Tool

↓

Observation

↓

LLM

↓

Need another Tool?

↓

Yes

↓

Tool

↓

Observation

↓

LLM

↓

Final Answer


╔═══════════════════════════════════════════════════════════════════════╗
║                     AGENTIC RAG SYSTEM                               ║
╚═══════════════════════════════════════════════════════════════════════╝

                         ┌──────────────────────┐
                         │   USER QUERY         │
                         │ "Refund + Payroll"   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────────┐
                    │   STEP 1: AGENT PLANNER          │
                    │   "Pehle HR, phir Payroll"       │
                    │   Tools: Search, Compare, Grade  │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────────┐
                    │   STEP 2: TOOL 1 - Search HR     │
                    │   [Vector Search]                 │
                    │   Result: No refund info         │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────────┐
                    │   STEP 3: AGENT EVALUATION       │
                    │   "Yahan refund nahi mila"       │
                    │   "Dosra tool try karo"          │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────────┐
                    │   STEP 4: TOOL 2 - Search Payroll│
                    │   [Vector Search]                 │
                    │   Result: Found refund policy    │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────────┐
                    │   STEP 5: GRADING                │
                    │   Relevance Score: 0.95          │
                    │   "Bohat relevant hai"           │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────────┐
                    │   STEP 6: COMPARE & SYNTHESIZE   │
                    │   "HR mein nahi, Payroll mein   │
                    │    hai"                          │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────────┐
                    │   STEP 7: GENERATE WITH CITATIONS│
                    │   + Source Tracking              │
                    └───────────────┬───────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   FINAL ANSWER       │
                         │ "Payroll Policy:    │
                         │  Refund in 30 days" │
                         │  Source: Payroll    │
                         │  Document Pg 45"    │
                         └──────────────────────┘

INPUTS:                       OUTPUTS:
- User Query                  - Final Answer
- Tool Definitions            - Source Citations
- Vector DB Access            - Tool Usage Logs
- Agent Instructions          - Decision Path
- System Prompts              - Confidence Score

AGENT DECISIONS:
1. Which tools to use?
2. What order to use them?
3. When to stop searching?
4. How to grade results?
5. When to regenerate?

TOOLS AVAILABLE:
🔧 Vector Search (Multiple DBs)
🔧 Document Ranking
🔧 Relevance Grading
🔧 Query Rewriting
🔧 Result Comparison
🔧 Citation Generation
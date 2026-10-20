# genai-testing-pocGenAI Banking Agent Testing POC
Objective
This POC demonstrates automated testing of a RAG and tool-using AI agent.

The focus is AI system evaluation rather than only UI automation.

Technology
Python
pytest
FastAPI
Promptfoo
JSON benchmark datasets
Areas Tested
RAG
Retrieval correctness
Answer grounding
Hallucination
Agentic AI
Intent
Tool selection
Function arguments
Tool results
Final response grounding
Security
Prompt injection
Unauthorized access
Unauthorized tool invocation
Regression
Failures are converted into permanent benchmark cases.

Architecture
Question | v Agent | +------> RAG ------> Knowledge Base | +------> Tool -----> Backend | +------> Security | v Response | v Evaluator | v PASS / FAIL / Reason

Install
Create virtual environment:

python -m venv .venv
Activate virtual environment.

Install dependencies:

pip install -r requirements.txt
Run Tests
pytest
Start API
uvicorn app.main:app --reload
Swagger:

http://127.0.0.1:8000/docs

Golden Benchmark
The benchmark dataset contains:

RAG cases
Tool-calling cases
Security cases
Out-of-scope cases
Each discovered AI defect should be converted into a permanent regression benchmark case.

Future Enhancements
Real LLM integration
Embedding-based RAG
Vector database
Answer relevancy evaluator
LLM-as-a-Judge
Promptfoo integration
WebSocket streaming
Performance testing
CI/CD pipeline
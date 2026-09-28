# TravelPilot ✈️

TravelPilot is an Agentic AI travel planning application that creates travel plans based on the user's destination, duration, budget, daily budget, and interests.

The agent uses tools, memory, budget checking, re-planning, an LLM-generated summary, and human approval.

## Features

* Travel requirement collection
* Agent-based travel planning
* User preference memory
* Weather checking tool
* Budget estimation and validation
* Automatic re-planning when the budget is exceeded
* LLM-generated travel summary
* Human approval demonstration
* Web-based frontend
* FastAPI backend

## Agent Workflow

1. Receive the user's travel goal and requirements.
2. Retrieve previous preferences from memory.
3. Create an initial travel plan.
4. Check destination weather using the mock weather tool.
5. Estimate the cost and compare it with the user's budget.
6. Re-plan if the estimated cost exceeds the budget.
7. Generate a travel summary using the OpenAI API when available.
8. Save the trip in memory.
9. Display the plan for human review and simulated approval.

## Project Structure

```
travel-agent/
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   └── memory.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── diagrams/
│   ├── architecture.png
│   ├── agent-lifecycle.png
│   └── replanning-flow.png
├── examples/
│   ├── successful-execution.md
│   └── failure-replanning.md
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Backend Setup

Install the dependencies from the `travel-agent` folder using `pip install -r requirements.txt`.

Start the backend from the `travel-agent` folder using:

`python -m uvicorn main:app --reload --app-dir backend`

The API runs at `http://127.0.0.1:8000`.

API documentation is available at `http://127.0.0.1:8000/docs`.

## Frontend Setup

Open `frontend/index.html` using VS Code Live Server.

The frontend collects travel requirements, sends them to the FastAPI backend, and displays the resulting travel plan, agent activity, estimated cost, and approval option.

## Tools

### Weather Tool

The current weather tool is a mock/demo tool. It returns a predefined travel status and does not retrieve live weather information.

### Budget Tools

The budget tools estimate trip costs, compare estimated costs against the user's total budget, and provide information for re-planning.

## Memory

TravelPilot stores user preferences and previous trip plans in memory while the backend process is running.

This memory is not persistent. It resets when the backend restarts.

## Re-planning

When the initial estimated cost exceeds the user's budget, the agent adjusts the daily budget and checks the revised plan.

Example:

* Total budget: ₹30,000
* Duration: 5 days
* Initial daily budget: ₹8,000
* Initial estimated cost: ₹40,000
* Revised daily budget: ₹6,000
* Revised estimated cost: ₹30,000

This demonstrates how the agent detects a budget constraint and adjusts its plan.

## LLM Integration

The application can use the OpenAI API to generate a natural-language travel summary.

If the API key is missing or the API request fails, the agent generates a fallback summary so the main planning workflow can continue.

To enable the OpenAI API, create a local `.env` file in the `travel-agent` folder and add your API key using the variable `OPENAI_API_KEY`.

Never commit the `.env` file or expose your API key on GitHub.

## Human-in-the-Loop

The frontend provides an approval button so the user can review the generated plan and confirm it.

The current approval feature is a frontend demonstration. It does not perform actual bookings or payments.

## Technologies Used

* Python
* FastAPI
* Pydantic
* HTML
* CSS
* JavaScript
* OpenAI API
* python-dotenv
* Git and GitHub

## Example Executions

The `examples` folder contains two demonstrations:

* `successful-execution.md` — a trip that fits within the user's budget.
* `failure-replanning.md` — a trip that initially exceeds the budget and requires re-planning.

## Diagrams

The `diagrams` folder contains:

* `architecture.png` — system architecture
* `agent-lifecycle.png` — agent lifecycle
* `replanning-flow.png` — budget re-planning flow

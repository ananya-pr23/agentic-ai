from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import TravelAgent

app = FastAPI(title="TravelPilot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = TravelAgent()


class TravelRequest(BaseModel):
    destination: str
    days: int
    budget: float
    interests: str
    daily_budget: float


@app.get("/")
def home():
    return {"message": "TravelPilot Agent is running."}


@app.post("/plan")
def create_travel_plan(request: TravelRequest):
    plan = agent.create_plan(
        destination=request.destination,
        days=request.days,
        budget=request.budget,
        interests=request.interests,
        daily_budget=request.daily_budget
    )

    return plan
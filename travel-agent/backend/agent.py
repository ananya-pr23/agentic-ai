import os

from dotenv import load_dotenv
from openai import OpenAI

from memory import TravelMemory
from tools import check_weather, estimate_budget, check_budget
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key) if api_key else None

class TravelAgent:
    def __init__(self):
        self.memory = TravelMemory()
    def generate_trip_summary(
        self,
        destination,
        days,
        budget,
        interests,
        estimated_cost
    ):
        if client is None:
            return (
                f"Travel plan for {destination}: "
                f"{days} days focused on {interests}. "
                f"Estimated cost is ₹{estimated_cost} "
                f"within the total budget of ₹{budget}."
            )
        try:
            response = client.responses.create(
                model="gpt-5-mini",
                input=(
                    "Create a short travel planning summary. "
                    f"Destination: {destination}. "
                    f"Duration: {days} days. "
                    f"Budget: ₹{budget}. "
                    f"Interests: {interests}. "
                    f"Estimated cost: ₹{estimated_cost}. "
                    "Mention the destination, duration, interests, "
                    "and whether the estimated cost fits the budget. "
                    "Keep it concise."
                )
            )

            return response.output_text

        except Exception:
            return (
                f"Travel plan for {destination}: "
                f"{days} days focused on {interests}. "
                f"Estimated cost is ₹{estimated_cost} "
                f"within the total budget of ₹{budget}."
            )
       
    def create_plan(
        self,
        destination,
        days,
        budget,
        interests,
        daily_budget
    ):
        steps = []

        steps.append(
            "🎯 Goal: Understand the user's travel requirements."
        )

        previous_preferences = self.memory.get_preferences()

        if previous_preferences:
            steps.append(
                "🧠 Memory: Retrieved the user's previous travel preferences."
            )

        preferences = {
            "destination": destination,
            "days": days,
            "budget": budget,
            "interests": interests
        }

        self.memory.save_preferences(preferences)

        steps.append(
            "🧠 Plan: Create an initial travel plan."
        )

        weather = check_weather(destination)

        steps.append(
            "🔧 Act: Check destination weather."
        )

        budget_result = check_budget(
            days,
            daily_budget,
            budget
        )

        steps.append(
            "👀 Observe: Check whether the plan fits the budget."
        )

        replanned = False

        if not budget_result["within_budget"]:
            steps.append(
                "❌ Observation: Initial plan exceeds the budget."
            )

            daily_budget = budget // days

            budget_result = check_budget(
                days,
                daily_budget,
                budget
            )

            replanned = True

            steps.append(
                "🔄 Re-plan: Adjust the daily budget to fit the budget."
            )

            steps.append(
                "✅ Observe: Updated plan fits within the budget."
            )

        else:
            steps.append(
                "✅ Observe: Plan is within the budget."
            )

        estimated_cost = estimate_budget(
            days,
            daily_budget
        )
        llm_summary = self.generate_trip_summary(
            destination,
            days,
            budget,
            interests,
            estimated_cost["estimated_total"]
        )
        steps.append(
            "🎯 Final decision: Prepare the travel plan."
        )

        plan = {
            "destination": destination,
            "days": days,
            "interests": interests,
            "weather": weather,
            "estimated_cost": estimated_cost["estimated_total"],
            "replanned": replanned,
            "message": budget_result["message"],
            "llm_summary": llm_summary,
            "steps": steps
        }

        self.memory.save_trip(plan)

        return plan
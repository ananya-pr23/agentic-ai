def check_weather(destination):
    return {
        "destination": destination,
        "status": "Weather check completed",
        "condition": "Suitable for travel"
    }


def estimate_budget(days, daily_budget):
    total = days * daily_budget

    return {
        "days": days,
        "daily_budget": daily_budget,
        "estimated_total": total
    }


def check_budget(days, daily_budget, total_budget):
    estimated_cost = days * daily_budget

    if estimated_cost <= total_budget:
        return {
            "within_budget": True,
            "estimated_cost": estimated_cost,
            "message": "Trip is within the user's budget."
        }

    return {
        "within_budget": False,
        "estimated_cost": estimated_cost,
        "message": "Trip exceeds the user's budget. Re-planning is required."
    }
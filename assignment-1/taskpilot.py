from datetime import datetime


def get_difficulty():
    while True:
        difficulty = input(
            "TaskPilot: Difficulty (Easy/Medium/Hard): "
        ).strip().lower()

        if difficulty in ("easy", "medium", "hard"):
            return difficulty

        print("TaskPilot: Please enter Easy, Medium, or Hard.")


def get_date():
    while True:
        deadline = input(
            "TaskPilot: Deadline (YYYY-MM-DD): "
        ).strip()

        try:
            return datetime.strptime(deadline, "%Y-%m-%d").date()

        except ValueError:
            print(
                "TaskPilot: Please enter the date in YYYY-MM-DD format."
            )


def get_assignment_count():
    while True:
        try:
            count = int(
                input(
                    "TaskPilot: How many pending assignments do you have?\n"
                    "You: "
                )
            )

            if count >= 1:
                return count

            print("TaskPilot: Please enter at least 1 assignment.")

        except ValueError:
            print("TaskPilot: Please enter a valid whole number.")


def calculate_priority(days_left, difficulty):
    if difficulty == "hard":
        difficulty_score = 3
    elif difficulty == "medium":
        difficulty_score = 2
    else:
        difficulty_score = 1

    if days_left < 0:
        deadline_score = 5
    elif days_left == 0:
        deadline_score = 5
    elif days_left == 1:
        deadline_score = 4
    elif days_left <= 3:
        deadline_score = 3
    elif days_left <= 7:
        deadline_score = 2
    else:
        deadline_score = 1

    return deadline_score + difficulty_score


def get_priority(score):
    if score >= 6:
        return "🔥 URGENT"
    elif score >= 4:
        return "⚠️ HIGH"
    return "🟢 NORMAL"


def get_reason(assignment):
    reasons = []

    if assignment["days_left"] < 0:
        reasons.append("the deadline has already passed")
    elif assignment["days_left"] <= 1:
        reasons.append("the deadline is very close")
    elif assignment["days_left"] <= 3:
        reasons.append("the deadline is approaching")

    if assignment["difficulty"] == "hard":
        reasons.append("it is difficult")
    elif assignment["difficulty"] == "medium":
        reasons.append("it has medium difficulty")

    if reasons:
        return " and ".join(reasons)

    return "it has the highest overall priority"


def main():
    print("\n==========================================")
    print("             🤖 TASKPILOT")
    print("       Assignment Priority Agent")
    print("==========================================")

    name = input(
        "\nTaskPilot: Hi! 👋 What's your name?\n"
        "You: "
    ).strip()

    if not name:
        name = "there"

    print(f"\nTaskPilot: Nice to meet you, {name}! 😊")
    print(
        "TaskPilot: I'll analyze your pending assignments "
        "and help you decide what to work on first.\n"
    )

    count = get_assignment_count()
    assignments = []
    today = datetime.now().date()

    for i in range(count):
        print(f"\nTaskPilot: Let's add assignment {i + 1}.")

        subject = input("You: Subject: ").strip()

        while not subject:
            print("TaskPilot: Subject cannot be empty.")
            subject = input("You: Subject: ").strip()

        deadline = get_date()
        difficulty = get_difficulty()

        days_left = (deadline - today).days
        priority_score = calculate_priority(
            days_left,
            difficulty
        )

        assignments.append(
            {
                "subject": subject,
                "deadline": deadline,
                "days_left": days_left,
                "difficulty": difficulty,
                "score": priority_score,
            }
        )

    print(
        "\nTaskPilot: Got it! Let me analyze your "
        "assignments... 🤔"
    )

    assignments.sort(
        key=lambda assignment: assignment["score"],
        reverse=True,
    )

    print("\n==========================================")
    print("          📊 PRIORITY ANALYSIS")
    print("==========================================")

    for number, assignment in enumerate(assignments, start=1):
        priority = get_priority(assignment["score"])

        if assignment["days_left"] < 0:
            days_status = (
                f"{abs(assignment['days_left'])} day(s) overdue"
            )
        else:
            days_status = f"{assignment['days_left']} day(s) left"

        print(f"\n{number}. {assignment['subject']}")
        print(f"   Deadline: {assignment['deadline']}")
        print(f"   Status: {days_status}")
        print(
            f"   Difficulty: "
            f"{assignment['difficulty'].capitalize()}"
        )
        print(f"   Priority: {priority}")

    highest = assignments[0]

    print("\n==========================================")
    print("          🎯 TASKPILOT'S DECISION")
    print("==========================================")

    print(
        f"\nTaskPilot: {name}, I recommend starting with "
        f"'{highest['subject']}'."
    )

    print(
        "TaskPilot: My decision is based on "
        f"{get_reason(highest)}."
    )

    if len(assignments) > 1:
        print("\nTaskPilot: Your recommended order is:")

        for number, assignment in enumerate(assignments, start=1):
            print(
                f"{number}. {assignment['subject']} "
                f"({get_priority(assignment['score'])})"
            )

    print("\nTaskPilot: You're all set! 🚀")
    print("TaskPilot: Focus on one task at a time and get it done.")
    print("\n==========================================")


if __name__ == "__main__":
    main()
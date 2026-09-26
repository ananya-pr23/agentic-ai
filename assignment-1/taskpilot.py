from datetime import datetime

print("\n==========================================")
print("          🤖 TASKPILOT")
print("     Assignment Priority Agent")
print("==========================================")

name = input("\nTaskPilot: Hi! 👋 What's your name?\nYou: ")

print(f"\nTaskPilot: Nice to meet you, {name}! 😊")
print("TaskPilot: I'll help you decide which assignment")
print("           you should work on first.\n")

count = int(input("TaskPilot: How many pending assignments do you have?\nYou: "))

assignments = []

for i in range(count):
    print(f"\nTaskPilot: Let's add assignment {i + 1}.")

    subject = input("You: Subject: ")
    deadline = input("You: Deadline (YYYY-MM-DD): ")
    difficulty = input("You: Difficulty (Easy/Medium/Hard): ").lower()

    deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
    today = datetime.now().date()

    days_left = (deadline_date - today).days

    if days_left < 0:
        days_left = 0

    if difficulty == "hard":
        difficulty_score = 3
    elif difficulty == "medium":
        difficulty_score = 2
    else:
        difficulty_score = 1

    if days_left == 0:
        deadline_score = 5
    elif days_left == 1:
        deadline_score = 4
    elif days_left <= 3:
        deadline_score = 3
    elif days_left <= 7:
        deadline_score = 2
    else:
        deadline_score = 1

    priority_score = deadline_score + difficulty_score

    assignments.append({
        "subject": subject,
        "deadline": deadline,
        "days_left": days_left,
        "difficulty": difficulty,
        "score": priority_score
    })

print("\nTaskPilot: Got it! Let me analyze your assignments... 🤔")

assignments.sort(key=lambda x: x["score"], reverse=True)

print("\n==========================================")
print("          📊 PRIORITY ANALYSIS")
print("==========================================")

for i, assignment in enumerate(assignments, 1):

    if assignment["score"] >= 6:
        priority = "🔥 URGENT"
    elif assignment["score"] >= 4:
        priority = "⚠️ HIGH"
    else:
        priority = "🟢 NORMAL"

    print(f"\n{i}. {assignment['subject']}")
    print(f"   Deadline: {assignment['deadline']}")
    print(f"   Days left: {assignment['days_left']}")
    print(f"   Difficulty: {assignment['difficulty'].capitalize()}")
    print(f"   Priority: {priority}")

print("\n==========================================")
print("          🎯 TASKPILOT'S DECISION")
print("==========================================")

highest = assignments[0]

print(
    f"\nTaskPilot: {name}, I recommend starting with "
    f"your {highest['subject']} assignment."
)

reasons = []

if highest["days_left"] <= 1:
    reasons.append("the deadline is very close")

if highest["difficulty"] == "hard":
    reasons.append("it is difficult")

if reasons:
    print("TaskPilot: My decision is based on " + " and ".join(reasons) + ".")
else:
    print("TaskPilot: It has the highest overall priority.")

if len(assignments) > 1:
    print("\nTaskPilot: Your recommended order is:")

    for i, assignment in enumerate(assignments, 1):
        print(f"{i}. {assignment['subject']}")

print("\nTaskPilot: You're all set! 🚀")
print("TaskPilot: Focus on one task at a time and get it done.")

print("\n==========================================")
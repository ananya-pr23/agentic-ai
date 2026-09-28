const form = document.getElementById("travelForm");
const loading = document.getElementById("loading");
const agentActivity = document.getElementById("agentActivity");
const result = document.getElementById("result");
const resultContent = document.getElementById("resultContent");
const approvalSection = document.getElementById("approvalSection");
const approveButton = document.getElementById("approveButton");
const approvalMessage = document.getElementById("approvalMessage");
form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const destination = document.getElementById("destination").value;
    const days = Number(document.getElementById("days").value);
    const budget = Number(document.getElementById("budget").value);
    const dailyBudget = Number(
        document.getElementById("dailyBudget").value
    );
    const interests = document.getElementById("interests").value;

    loading.classList.remove("hidden");
    agentActivity.classList.remove("hidden");
    result.classList.add("hidden");

    try {
        const response = await fetch("http://127.0.0.1:8000/plan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                destination: destination,
                days: days,
                budget: budget,
                interests: interests,
                daily_budget: dailyBudget
            })
        });

        if (!response.ok) {
            throw new Error("Unable to create travel plan.");
        }

        const plan = await response.json();

        const activitySteps = document.querySelectorAll(".activity-step");

        activitySteps.forEach((step) => {
            step.classList.add("hidden");
        });

        const steps = plan.steps || [
            "🎯 Goal: Understand the user's travel requirements.",
            "🧠 Plan: Create an initial travel plan.",
            "🔧 Act: Check destination weather.",
            "👀 Observe: Check whether the plan fits the budget.",
            plan.replanned
                ? "🔄 Re-plan: Adjust the plan to fit the budget."
                : "✅ Observe: Plan is within the budget.",
            "🎯 Final decision: Prepare the travel plan."
        ];

        steps.forEach((step, index) => {
            if (activitySteps[index]) {
                activitySteps[index].textContent = step;
                activitySteps[index].classList.remove("hidden");
            }
        });

        resultContent.innerHTML = `
            <div class="result-item">
                <strong>Destination:</strong> ${plan.destination}
            </div>

            <div class="result-item">
                <strong>Days:</strong> ${plan.days}
            </div>

            <div class="result-item">
                <strong>Interests:</strong> ${plan.interests}
            </div>
            <div class="result-item">
                <strong>🤖 AI Summary:</strong>
                ${plan.llm_summary}
            </div>
            <div class="result-item">
                <strong>Weather:</strong>
                ${plan.weather.condition}
            </div>

            <div class="result-item">
                <strong>Estimated Cost:</strong>
                ₹${plan.estimated_cost}
            </div>

            <div class="result-item">
                <strong>Re-planned:</strong>
                ${plan.replanned ? "Yes" : "No"}
            </div>

            <div class="success">
                ${plan.message}
            </div>
        `;

        result.classList.remove("hidden");
        approvalSection.classList.remove("hidden");
approvalMessage.innerHTML = "";
approveButton.disabled = false;
approveButton.textContent = "✅ Approve Travel Plan";

    } catch (error) {
        resultContent.innerHTML = `
            <div class="success">
                ❌ ${error.message}
            </div>
        `;

        result.classList.remove("hidden");

    } finally {
        loading.classList.add("hidden");
    }
});
approveButton.addEventListener("click", function () {
    approveButton.disabled = true;
    approveButton.textContent = "Processing...";

    setTimeout(function () {
        approvalMessage.innerHTML = `
            <div class="success">
                ✅ Travel plan approved successfully.
                <br>
                Human approval received before confirmation.
            </div>
        `;

        approveButton.textContent = "✓ Plan Approved";
    }, 800);
});
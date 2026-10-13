
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None



def ask_llm(prompt):
    if client is None:
        return "API key not found. Check GEMINI_API_KEY in your .env file."

    import time

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=prompt
            )
            return response.text or "The model returned an empty response."

        except Exception as e:
            error = str(e)

            if "503" in error or "UNAVAILABLE" in error:
                if attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue

            return f"Error: {error}"

    return "The model is temporarily unavailable. Please try again later."



def zero_shot_prompt():
    question = input("Enter your study question: ")
    prompt = f"""
Answer the student's question clearly and accurately.
Use simple language and provide a short explanation.

Question: {question}
"""
    print("\nZero-Shot Response:")
    print(ask_llm(prompt))


def few_shot_prompt():
    question = input("Enter your study question: ")
    prompt = f"""
Answer student questions in simple language.

Example 1:
Question: What is CPU?
Answer: CPU stands for Central Processing Unit. It executes
instructions and processes data.

Example 2:
Question: What is RAM?
Answer: RAM stands for Random Access Memory. It temporarily
stores data and instructions currently being used.

Follow the same style for this question.

Question: {question}
Answer:
"""
    print("\nFew-Shot Response:")
    print(ask_llm(prompt))


def role_prompting():
    question = input("Enter your study question: ")
    prompt = f"""
You are a friendly and knowledgeable college study tutor.
Explain concepts in simple language and use examples when helpful.

Student question: {question}
"""
    print("\nRole-Based Response:")
    print(ask_llm(prompt))


def faq_assistant():
    question = input("Ask your study assistant: ")
    prompt = f"""
You are an intelligent FAQ assistant for college students.
Answer questions about study techniques, exam preparation,
time management, programming fundamentals, and assignments.
Give clear, practical answers. Do not invent college-specific
rules or dates if you do not know them.

Student question: {question}
"""
    print("\nIntelligent FAQ Response:")
    print(ask_llm(prompt))


def main():
    while True:
        print("\n===== STUDY ASSISTANT AGENT =====")
        print("1. Zero-Shot Prompting")
        print("2. Few-Shot Prompting")
        print("3. Role Prompting")
        print("4. Intelligent FAQ Assistant")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            zero_shot_prompt()
        elif choice == "2":
            few_shot_prompt()
        elif choice == "3":
            role_prompting()
        elif choice == "4":
            faq_assistant()
        elif choice == "5":
            print("Exiting Study Assistant.")
            break
        else:
            print("Invalid choice. Select 1 to 5.")


if __name__ == "__main__":
    main()

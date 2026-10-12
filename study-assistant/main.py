
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


def ask_llm(prompt):
    if client is None:
        return "API key not found. Please configure OPENAI_API_KEY in your .env file."

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"Error: {e}"


def zero_shot_prompt():
    question = input("\nEnter your study question: ")

    prompt = f"""
    Answer the following student question clearly and accurately.
    Use simple language and provide a short explanation.

    Question: {question}
    """

    print("\nZero-Shot Response:")
    print(ask_llm(prompt))


def few_shot_prompt():
    question = input("\nEnter your study question: ")

    prompt = f"""
    Answer student questions using simple language and numbered points
    when appropriate.

    Example 1:
    Question: What is CPU?
    Answer: CPU stands for Central Processing Unit. It executes
    instructions and processes data in a computer.

    Example 2:
    Question: What is RAM?
    Answer: RAM stands for Random Access Memory. It temporarily
    stores data and instructions currently being used.

    Now answer this question in the same style.

    Question: {question}
    Answer:
    """

    print("\nFew-Shot Response:")
    print(ask_llm(prompt))


def role_prompting():
    question = input("\nEnter your study question: ")

    prompt = f"""
    You are a friendly and knowledgeable college study assistant.
    Explain concepts to students in simple language.
    Use examples when helpful, keep answers organized, and avoid
    unnecessary technical jargon.

    Student question: {question}
    """

    print("\nRole-Based Response:")
    print(ask_llm(prompt))


def faq_assistant():
    question = input("\nAsk your study assistant: ")

    prompt = f"""
    You are an intelligent FAQ assistant for college students.

    Help students with common academic questions about:
    - Study techniques
    - Exam preparation
    - Time management
    - Programming fundamentals
    - College assignments

    Give clear, practical, and accurate answers.
    If a question is outside your knowledge, acknowledge the limitation.
    Do not invent college-specific rules, dates, or policies.

    Student question: {question}
    """

    print("\nStudy Assistant Response:")
    print(ask_llm(prompt))


def main():
    while True:
        print("\n===== STUDY ASSISTANT AGENT =====")
        print("1. Zero-Shot Prompting")
        print("2. Few-Shot Prompting")
        print("3. Role Prompting")
        print("4. Intelligent FAQ Assistant")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            zero_shot_prompt()
        elif choice == "2":
            few_shot_prompt()
        elif choice == "3":
            role_prompting()
        elif choice == "4":
            faq_assistant()
        elif choice == "5":
            print("Thank you for using the Study Assistant Agent!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
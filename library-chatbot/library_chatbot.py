books = [
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "available": True
    },
    {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "available": True
    },
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "available": False
    },
    {
        "title": "Ikigai",
        "author": "Héctor García and Francesc Miralles",
        "available": True
    },
    {
        "title": "Think Like a Monk",
        "author": "Jay Shetty",
        "available": True
    }
]


print("========================================")
print("        COLLEGE LIBRARY CHATBOT")
print("========================================")
print("Hello! I can help you check our library books.")
print("Type 'exit' to leave the chatbot.")

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    found_book = None

    for book in books:
        if book["title"].lower() in question.lower():
            found_book = book
            break

    if found_book and found_book["available"]:
        print("Bot: The book is available.")
    elif found_book:
        print("Bot: The book is currently borrowed.")
    else:
        print("Bot: That book is not available in our library.")
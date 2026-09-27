books = [
    {
        "title": "Atomic Habits",
        "author": "James Clear"
    },
    {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey"
    },
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle"
    },
    {
        "title": "Ikigai",
        "author": "Héctor García and Francesc Miralles"
    },
    {
        "title": "Think Like a Monk",
        "author": "Jay Shetty"
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

    if found_book:
        print(
            f"Bot: Yes, we have '{found_book['title']}' "
            f"by {found_book['author']}."
        )
    else:
        print("Bot: That book is not available in our library.")
# College Library Chatbot 🤖

A simple Python-based college library chatbot created as part of Class Activity 2.

The chatbot uses a fixed inventory of five self-help books and answers questions about whether a book is available, borrowed, or not present in the library.

## Books in the Library

- Atomic Habits — James Clear
- The 7 Habits of Highly Effective People — Stephen R. Covey
- The Power of Now — Eckhart Tolle
- Ikigai — Héctor García and Francesc Miralles
- Think Like a Monk — Jay Shetty

## Version 1

The original chatbot checks whether a requested book exists in the five-book inventory and provides its author.

File: `library_chatbot_v1.py`

## Version 2 — GitHub Copilot Improved

GitHub Copilot was used to improve the chatbot by:

- Adding an `available` field to each book
- Checking whether a book is available or borrowed
- Handling books that are not present in the library
- Keeping the chatbot restricted to the existing five-book inventory

File: `library_chatbot.py`

## Example

You: Do you have Atomic Habits?

Bot: The book is available.

You: Do you have The Power of Now?

Bot: The book is currently borrowed.

You: Do you have Harry Potter?

Bot: That book is not available in our library.

## How to Run

Open the terminal inside the `library-chatbot` folder.

Run the original version:

`python library_chatbot_v1.py`

Run the GitHub Copilot improved version:

`python library_chatbot.py`

Type `exit` to close the chatbot.

## Tools Used

- Python
- Visual Studio Code
- GitHub Copilot
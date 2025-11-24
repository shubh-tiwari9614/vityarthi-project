📘 VIT Bhopal Digital Library System

A simple Python-based Digital Library System developed using
loops, conditions, and dictionaries.
This program allows users to view books, issue books, return books, and calculates late return fines automatically.


---

✨ Features

✅ 1. Show Available Books

Displays a list of all books currently available in the library.

✅ 2. Issue a Book

User can issue any book that is available.

The system stores the issue day.

User must return the book within 15 days.


✅ 3. Return a Book

User enters the return date.

Program calculates:

Number of days used

Whether the return is on time

Late fine (₹10 per extra day)



✅ 4. Exit System

Ends the program safely.


---

📂 Data Structures Used

Books List

books = ["Python Basics", "Data Science 101", "AI for Beginners", "Machine Learning Guide", "Maths for Engineers"]

Issued Books Dictionary

issued_books = { "Book Name" : issue_day }


---

💻 How the Fine is Calculated

Maximum allowed days: 15

If returned late:


extra_days = (return_day - issue_day) - 15
fine = extra_days * 10


---

📝 Program Flow

1. Menu is displayed again and again using a while loop.


2. Depending on user input, the program performs the selected action.


3. Conditions (if/elif/else) manage:

Issuing books

Checking availability

Validating returns

Fine calculation





---

📎 Requirements

Python 3.x

No external libraries required



---

🚀 How to Run

1. Copy the code into a Python file
Example: library_system.py


2. Run in terminal:



python library_system.py

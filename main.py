
books = ["Python Basics", "Data Science 101", "AI for Beginners", "Machine Learning Guide", "Maths for Engineers"]


issued_books = {}

while True:
    print("\n===== VIT BHOPAL DIGITAL LIBRARY =====")
    print("1. Show Available Books")
    print("2. Issue a Book")
    print("3. Return a Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        print("\nAvailable Books:")
        for b in books:
            print("- ", b)

    
    elif choice == 2:
        book = input("Enter book name to issue: ")

        if book in books:
            day = int(input("Enter today's day number (1-365): "))
            books.remove(book)
            issued_books[book] = day
            print(f"Book '{book}' issued successfully on day {day}!")
            print("NOTE: Please return within 15 days.")
        else:
            print("Book not available!")

    
    elif choice == 3:
        book = input("Enter book name to return: ")

        if book in issued_books:
            return_day = int(input("Enter today's day number (1-365): "))
            issue_day = issued_books[book]

            days_used = return_day - issue_day

            if days_used <= 15:
                print("Returned on time. No fine! 👍")
            else:
                extra = days_used - 15
                fine = extra * 10
                print(f"Late return by {extra} days. Fine = ₹{fine}")

            
            del issued_books[book]
            books.append(book)
            print(f"Book '{book}' returned successfully!")

        else:
            print("You never issued this book!")

    
    elif choice == 4:
        print("Thanks for using VIT Bhopal Library System!")
        break

    else:
        print("Invalid Choice! Try Again.")

    

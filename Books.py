books = {
    1: {"title": "Python Basics", "author": "Guido van Rossum", "available": True},
    2: {"title": "Data Structures", "author": "Mark Allen Weiss", "available": True},
    3: {"title": "Algorithms", "author": "CLRS", "available": True},
    4: {"title": "Operating Systems", "author": "Galvin", "available": True},
    5: {"title": "Java Basics", "author": "Andrew Tanenbaum", "available": True},
    6: {"title": "Database Systems", "author": "Korth", "available": True},
    7: {"title": "Software Engineering", "author": "Ian Sommerville", "available": True},
    8: {"title": "Artificial Intelligence", "author": "Stuart Russell", "available": True},
    9: {"title": "Machine Learning", "author": "Tom Mitchell", "available": True},
    10: {"title": "Discrete Mathematics", "author": "Kenneth Rosen", "available": True}
}


users = {}

borrowed_books = {}

due_days = 7
fine_per_day = 5


def register_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    users[email] = {
        "name": name,
        "phone": phone
    }

    print("User registered successfully\n")


def show_books():
    print("\nAvailable Books:")
    for book_id, details in books.items():
        status = "Available" if details["available"] else "Not Available"
        print(book_id, "-", details["title"], "|", details["author"], "|", status)
    print()


def borrow_book():
    email = input("Enter your email: ")

    if email not in users:
        print("User not registered\n")
        return

    show_books()
    book_id = int(input("Enter Book ID to borrow: "))

    if book_id not in books:
        print("Invalid Book ID\n")
        return

    if books[book_id]["available"]:
        day = int(input("Enter borrowing day number: "))
        borrowed_books[book_id] = {
            "email": email,
            "borrow_day": day
        }
        books[book_id]["available"] = False
        print("Book borrowed successfully\n")
    else:
        print("Book not available\n")


def return_book():
    book_id = int(input("Enter Book ID to return: "))

    if book_id not in borrowed_books:
        print("This book was not borrowed\n")
        return

    return_day = int(input("Enter return day number: "))
    borrow_day = borrowed_books[book_id]["borrow_day"]

    days_used = return_day - borrow_day
    fine = 0

    if days_used > due_days:
        fine = (days_used - due_days) * fine_per_day

    books[book_id]["available"] = True
    del borrowed_books[book_id]

    print("Book returned successfully")
    print("Fine:", fine, "\n")


while True:
    print("1. Register User")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        register_user()
    elif choice == 2:
        show_books()
    elif choice == 3:
        borrow_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        print("Exiting system")
        break
    else:
        print("Invalid choice\n")
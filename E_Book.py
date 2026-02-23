book_data = {
    "title": "The Basics of Python",
    "author": "Ayushman Kar",
    "publication_year": 2026
}
chapters = [
    {
        "title": "Introduction",
        "content": "Welcome to this e-book. Python is a powerful programming language. It is known for its simplicity and readability."
    },
    {
        "title": "Variables",
        "content": "Variables are used to store data values. In Python, you do not need to declare the type of a variable. x = 5 is enough."
    },
    {
        "title": "Loops",
        "content": "Loops allow you to iterate over a sequence. The for loop and while loop are the two main types of loops in Python."
    },
    {
        "title": "Functions",
        "content": "A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function."
    },
    {
        "title": "Conclusion",
        "content": "This concludes the basic overview. Keep practicing to master the language. Happy coding!"
    }
]
saved_bookmark = 0
def display_toc():
    print(f"\n--- {book_data['title']} ---")
    print(f"By {book_data['author']}")
    print("-" * 30)
    print("Table of Contents:")
    index = 1
    for chapter in chapters:
        print(f"{index}. {chapter['title']}")
        index += 1
def read_book():
    global saved_bookmark
    current_index = saved_bookmark
    while True:
        if current_index < 0:
            current_index = 0
        elif current_index >= len(chapters):
            print("\nYou have reached the end of the book.")
            current_index = len(chapters) - 1       
        chapter = chapters[current_index]       
        print("\n" + "=" * 40)
        print(f"Chapter {current_index + 1}: {chapter['title']}")
        print("=" * 40)
        print(chapter['content'])
        print("-" * 40)
        print(f"Page {current_index + 1} of {len(chapters)}")        
        command = input("\n[N]ext | [P]revious | [B]ookmark & Quit | [Q]uit: ").lower()        
        if command == 'n':
            if current_index < len(chapters) - 1:
                current_index += 1
            else:
                print("\nThis is the last chapter.")
        elif command == 'p':
            if current_index > 0:
                current_index -= 1
            else:
                print("\nThis is the first chapter.")
        elif command == 'b':
            saved_bookmark = current_index
            print(f"Bookmark saved at Chapter {current_index + 1}.")
            break
        elif command == 'q':
            break
        else:
            print("Invalid command.")
def main():
    while True:
        print("\n=== E-BOOK READER MENU ===")
        print("1. Table of Contents")
        print("2. Read / Resume")
        print("3. Reset Progress")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            display_toc()
        elif choice == '2':
            read_book()
        elif choice == '3':
            global saved_bookmark
            saved_bookmark = 0
            print("Progress reset to the beginning.")
        elif choice == '4':
            print("Closing E-book Reader.")
            break
        else:
            print("Invalid choice.")
main()
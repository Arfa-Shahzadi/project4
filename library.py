import os

FILENAME = "library.txt"

def load_books():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_books(books):
    with open(FILENAME, "w") as file:
        for book in books:
            file.write(book + "\n")

def add_book():
    title = input("Book title: ")
    author = input("Author: ")
    book = f"{title} by {author}"
    books = load_books()
    books.append(book)
    save_books(books)
    print("Book added successfully!")

def view_books():
    books = load_books()
    if not books:
        print("No books in library.")
    else:
        print("\n--- Your Library ---")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book}")
        print()

def search_book():
    keyword = input("Enter keyword to search: ").lower()
    books = load_books()
    found = [book for book in books if keyword in book.lower()]
    if found:
        print("\n--- Search Results ---")
        for book in found:
            print(book)
    else:
        print("No matching books found.")

def delete_book():
    view_books()
    books = load_books()
    try:
        index = int(input("Enter book number to delete: ")) - 1
        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books(books)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- Personal Library Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
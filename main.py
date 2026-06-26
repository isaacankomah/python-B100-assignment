"""Main menu for the library management system."""

from book import Book
from library import Library
from member import Member


def show_menu():
    """Display the main menu."""
    print("\nLibrary Management System")
    print("1. Add book")
    print("2. Register member")
    print("3. Search book")
    print("4. Borrow book")
    print("5. Return book")
    print("6. List books")
    print("7. List members")
    print("8. Exit")


def add_book_menu(library):
    """Ask the user for book details and add a book."""
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")

    book = Book(isbn, title, author, category)

    if library.add_book(book):
        print("Book added successfully.")
    else:
        print("Book could not be added.")


def register_member_menu(library):
    """Ask the user for member details and register a member."""
    member_id = input("Enter member ID: ")
    name = input("Enter member name: ")
    email = input("Enter member email: ")

    member = Member(member_id, name, email)

    if library.register_member(member):
        print("Member registered successfully.")
    else:
        print("Member could not be registered.")


def search_book_menu(library):
    """Ask for a search term and display matching books."""
    search_term = input("Enter title, author, category, or ISBN: ")
    results = library.search_book(search_term)

    if results:
        print("\nSearch results:")
        for book in results:
            print(book.display_info())
    else:
        print("No matching book found.")


def borrow_book_menu(library):
    """Ask for borrowing details and borrow a book."""
    member_id = input("Enter member ID: ")
    isbn = input("Enter ISBN of book to borrow: ")

    message = library.borrow_book(member_id, isbn)
    print(message)


def return_book_menu(library):
    """Ask for return details and return a book."""
    member_id = input("Enter member ID: ")
    isbn = input("Enter ISBN of book to return: ")

    message = library.return_book(member_id, isbn)
    print(message)


def list_books_menu(library):
    """Display all books in the library."""
    books = library.list_books()

    if books:
        print("\nBooks in the library:")
        for book in books:
            print(book.display_info())
    else:
        print("No books available.")


def list_members_menu(library):
    """Display all registered members."""
    members = library.list_members()

    if members:
        print("\nRegistered members:")
        for member in members:
            print(member.display_info())
    else:
        print("No members registered.")


def main():
    """Run the menu-driven program."""
    library = Library("Community Library")

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from the menu.")
            continue

        if choice == 1:
            add_book_menu(library)
        elif choice == 2:
            register_member_menu(library)
        elif choice == 3:
            search_book_menu(library)
        elif choice == 4:
            borrow_book_menu(library)
        elif choice == 5:
            return_book_menu(library)
        elif choice == 6:
            list_books_menu(library)
        elif choice == 7:
            list_members_menu(library)
        elif choice == 8:
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select a menu option from 1 to 8.")


if __name__ == "__main__":
    main()
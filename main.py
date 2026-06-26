"""Main menu for the library management system."""

from book import Book
from data_handler import read_csv, write_csv
from library import Library
from loan_record import LoanRecord
from member import Member


BOOKS_FILE = "data/books.csv"
MEMBERS_FILE = "data/members.csv"
LOANS_FILE = "data/loans.csv"

BOOK_FIELDS = ["isbn", "title", "author", "category", "is_available"]
MEMBER_FIELDS = ["member_id", "name", "email", "borrowed_books"]
LOAN_FIELDS = [
    "record_id",
    "member_id",
    "isbn",
    "borrow_date",
    "return_date",
    "status",
]


def load_library():
    """Load saved books, members, and loans from CSV files."""
    library = Library("Community Library")

    for row in read_csv(BOOKS_FILE):
        is_available = row["is_available"] == "True"
        book = Book(
            row["isbn"],
            row["title"],
            row["author"],
            row["category"],
            is_available,
        )
        library.add_book(book)

    for row in read_csv(MEMBERS_FILE):
        member = Member(row["member_id"], row["name"], row["email"])
        borrowed_books = row["borrowed_books"]

        if borrowed_books:
            member.borrowed_books = borrowed_books.split("|")

        library.register_member(member)

    for row in read_csv(LOANS_FILE):
        loan = LoanRecord(
            row["record_id"],
            row["member_id"],
            row["isbn"],
            row["borrow_date"],
            row["return_date"] or None,
            row["status"],
        )
        library.loan_records.append(loan)

    return library


def save_library(library):
    """Save books, members, and loans to CSV files."""
    book_rows = []
    for book in library.books:
        book_rows.append(
            {
                "isbn": book.isbn,
                "title": book.title,
                "author": book.author,
                "category": book.category,
                "is_available": str(book.is_available),
            }
        )

    member_rows = []
    for member in library.members:
        member_rows.append(
            {
                "member_id": member.member_id,
                "name": member.name,
                "email": member.email,
                "borrowed_books": "|".join(member.borrowed_books),
            }
        )

    loan_rows = []
    for loan in library.loan_records:
        loan_rows.append(loan.create_record())

    write_csv(BOOKS_FILE, BOOK_FIELDS, book_rows)
    write_csv(MEMBERS_FILE, MEMBER_FIELDS, member_rows)
    write_csv(LOANS_FILE, LOAN_FIELDS, loan_rows)


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
    library = load_library()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from the menu.")
            continue

        if choice == 1:
            add_book_menu(library)
            save_library(library)
        elif choice == 2:
            register_member_menu(library)
            save_library(library)
        elif choice == 3:
            search_book_menu(library)
        elif choice == 4:
            borrow_book_menu(library)
            save_library(library)
        elif choice == 5:
            return_book_menu(library)
            save_library(library)
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
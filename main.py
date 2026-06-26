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
    print("7. Exit")


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
            # TODO: Ask the user for book details.
            # TODO: Create a Book object and add it to the library.
            pass
        elif choice == 2:
            # TODO: Ask the user for member details.
            # TODO: Create a Member object and register it.
            pass
        elif choice == 3:
            # TODO: Ask for a search term and print matching books.
            pass
        elif choice == 4:
            # TODO: Ask for member_id and isbn, then borrow the book.
            pass
        elif choice == 5:
            # TODO: Ask for member_id and isbn, then return the book.
            pass
        elif choice == 6:
            # TODO: Print all books.
            pass
        elif choice == 7:
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select a menu option from 1 to 7.")


if __name__ == "__main__":
    main()


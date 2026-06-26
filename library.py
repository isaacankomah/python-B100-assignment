"""Library module that connects books, members, and loan records."""

from book import Book
from loan_record import LoanRecord
from member import Member


class Library:
    """Manage books, members, and borrowing records."""

    def __init__(self, name):
        """Create a library object."""
        self.name = name
        self.books = []
        self.members = []
        self.loan_records = []

    def add_book(self, book):
        """Add a book object to the library."""
        # TODO: Check that the argument is a Book before adding it.
        pass

    def register_member(self, member):
        """Register a member object with the library."""
        # TODO: Check that the argument is a Member before adding it.
        pass

    def search_book(self, search_term):
        """Search books by title, author, category, or ISBN."""
        # TODO: Use a loop to find matching books.
        pass

    def borrow_book(self, member_id, isbn):
        """Borrow a book for a member."""
        # TODO: Find the member and book, check availability, then create a
        # LoanRecord if borrowing succeeds.
        pass

    def return_book(self, member_id, isbn):
        """Return a borrowed book."""
        # TODO: Find the active loan record, close it, update the member, and
        # update the book availability.
        pass

    def list_books(self):
        """Return all books in the library."""
        # TODO: Return self.books or readable book descriptions.
        pass

    def list_members(self):
        """Return all registered members."""
        # TODO: Return self.members or readable member descriptions.
        pass


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
        if isinstance(book, Book):
            self.books.append(book)
            return True
        return False

    def register_member(self, member):
        """Register a member object with the library."""
        if isinstance(member, Member):
            self.members.append(member)
            return True
        return False

    def search_book(self, search_term):
        """Search books by title, author, category, or ISBN."""
        results = []
        search_term = search_term.lower()

        for book in self.books:
            if (
                search_term in book.title.lower()
                or search_term in book.author.lower()
                or search_term in book.category.lower()
                or search_term in book.isbn.lower()
            ):
                results.append(book)

        return results

    def find_book_by_isbn(self, isbn):
        """Find and return a book using its ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member_by_id(self, member_id):
        """Find and return a member using their member ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, isbn):
        """Borrow a book for a member."""
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)

        if member is None:
            return "Member not found."

        if book is None:
            return "Book not found."

        if not book.is_available:
            return "Book is already borrowed."

        book.borrow_book()
        member.borrow(isbn)

        record_id = f"L{len(self.loan_records) + 1:03}"
        loan_record = LoanRecord(record_id, member_id, isbn)
        self.loan_records.append(loan_record)

        return "Book borrowed successfully."

    def return_book(self, member_id, isbn):
        """Return a borrowed book."""
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)

        if member is None:
            return "Member not found."

        if book is None:
            return "Book not found."

        if isbn not in member.borrowed_books:
            return "This member did not borrow this book."

        book.return_book()
        member.return_book(isbn)

        for record in self.loan_records:
            if (
                record.member_id == member_id
                and record.isbn == isbn
                and record.is_active()
            ):
                record.close_record()
                break

        return "Book returned successfully."

    def list_books(self):
        """Return all books in the library."""
        return self.books

    def list_members(self):
        """Return all registered members."""
        return self.members
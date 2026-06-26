"""Book module for the library management system."""


class Book:
    """Represent one book in the library."""

    def __init__(self, isbn, title, author, category, is_available=True):
        """Create a book object with basic book details."""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
        self.is_available = is_available

    def display_info(self):
        """Return a readable description of the book."""
        status = "Available" if self.is_available else "Borrowed"
        return (
            f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, "
            f"Category: {self.category}, Status: {status}"
        )

    def borrow_book(self):
        """Mark the book as borrowed if it is available."""
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        """Mark the book as available again."""
        self.is_available = True
        return True

    def update_details(self, title=None, author=None, category=None):
        """Update book details when new values are provided."""
        if title is not None:
            self.title = title

        if author is not None:
            self.author = author

        if category is not None:
            self.category = category

        return True
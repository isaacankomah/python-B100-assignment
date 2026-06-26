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
        # TODO: Return a string that includes the title, author, ISBN,
        # category, and availability.
        pass

    def borrow_book(self):
        """Mark the book as borrowed if it is available."""
        # TODO: Use an if statement to check availability.
        # If the book is available, change is_available to False.
        # Return True when borrowing succeeds and False otherwise.
        pass

    def return_book(self):
        """Mark the book as available again."""
        # TODO: Set is_available back to True.
        pass

    def update_details(self, title=None, author=None, category=None):
        """Update book details when new values are provided."""
        # TODO: Use conditionals to update only the values that are not None.
        pass


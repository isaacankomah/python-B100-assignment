"""Member module for the library management system."""


class Member:
    """Represent one registered library member."""

    def __init__(self, member_id, name, email):
        """Create a member object."""
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def display_info(self):
        """Return a readable description of the member."""
        return (
            f"Member ID: {self.member_id}, Name: {self.name}, "
            f"Email: {self.email}, Borrowed Books: {len(self.borrowed_books)}"
        )

    def borrow(self, isbn):
        """Add a borrowed book ISBN to the member's list."""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
            return True
        return False

    def return_book(self, isbn):
        """Remove a returned book ISBN from the member's list."""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True
        return False

    def list_borrowed_books(self):
        """Return all borrowed book ISBNs."""
        if not self.borrowed_books:
            return "No borrowed books."
        return ", ".join(self.borrowed_books)

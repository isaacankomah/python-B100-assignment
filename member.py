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
        # TODO: Return a string with member ID, name, email, and number of
        # borrowed books.
        pass

    def borrow(self, isbn):
        """Add a borrowed book ISBN to the member's list."""
        # TODO: Add isbn to borrowed_books only if it is not already there.
        pass

    def return_book(self, isbn):
        """Remove a returned book ISBN from the member's list."""
        # TODO: Remove isbn if it exists in borrowed_books.
        pass

    def list_borrowed_books(self):
        """Return all borrowed book ISBNs."""
        # TODO: Return the borrowed_books list or a readable string.
        pass


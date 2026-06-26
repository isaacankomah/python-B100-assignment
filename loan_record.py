"""Loan record module for the library management system."""

from datetime import date


class LoanRecord:
    """Represent one borrowing record."""

    def __init__(
        self,
        record_id,
        member_id,
        isbn,
        borrow_date=None,
        return_date=None,
        status="active",
    ):
        """Create a loan record."""
        self.record_id = record_id
        self.member_id = member_id
        self.isbn = isbn
        self.borrow_date = borrow_date or str(date.today())
        self.return_date = return_date
        self.status = status

    def create_record(self):
        """Return the loan record details as a dictionary."""
        return {
            "record_id": self.record_id,
            "member_id": self.member_id,
            "isbn": self.isbn,
            "borrow_date": self.borrow_date,
            "return_date": self.return_date,
            "status": self.status,
        }

    def close_record(self):
        """Close the record when a book is returned."""
        self.return_date = str(date.today())
        self.status = "returned"
        return True

    def display_record(self):
        """Return a readable loan record summary."""
        return (
            f"Record ID: {self.record_id}, Member ID: {self.member_id}, "
            f"ISBN: {self.isbn}, Borrow Date: {self.borrow_date}, "
            f"Return Date: {self.return_date}, Status: {self.status}"
        )

    def is_active(self):
        """Check whether the record is still active."""
        return self.status == "active"
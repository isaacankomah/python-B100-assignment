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
        # TODO: Return a dictionary version of this record.
        pass

    def close_record(self):
        """Close the record when a book is returned."""
        # TODO: Set return_date to today's date and status to returned.
        pass

    def display_record(self):
        """Return a readable loan record summary."""
        # TODO: Return a formatted string with record details.
        pass

    def is_active(self):
        """Check whether the record is still active."""
        # TODO: Return True if status is active, otherwise False.
        pass


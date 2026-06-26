"""CSV file handling helpers for the library management system."""

import csv


def read_csv(file_path):
    """Read rows from a CSV file and return them as dictionaries."""
    # TODO: Use try/except to handle FileNotFoundError.
    # Hint: csv.DictReader is useful here.
    pass


def write_csv(file_path, fieldnames, rows):
    """Write dictionary rows to a CSV file."""
    # TODO: Use csv.DictWriter to write the header and rows.
    pass


def append_csv(file_path, fieldnames, row):
    """Append one dictionary row to a CSV file."""
    # TODO: Open the file in append mode.
    # Hint: you may need to write the header when the file is empty.
    pass


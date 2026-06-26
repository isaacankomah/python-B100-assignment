"""CSV file handling helpers for the library management system."""

import csv
import os


def read_csv(file_path):
    """Read rows from a CSV file and return them as dictionaries."""
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def write_csv(file_path, fieldnames, rows):
    """Write dictionary rows to a CSV file."""
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def append_csv(file_path, fieldnames, row):
    """Append one dictionary row to a CSV file."""
    file_exists = os.path.exists(file_path)
    file_is_empty = not file_exists or os.path.getsize(file_path) == 0

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file_is_empty:
            writer.writeheader()

        writer.writerow(row)
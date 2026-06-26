# B100 Library Management System - Learning Scaffold

## Purpose

This project is a small command-line library management system. It is designed
to help you practise the Python concepts required in the B100 assessment brief:
classes, methods, loops, conditionals, file handling, exception handling,
modules, comments, docstrings, and an interactive menu.

Important: use this scaffold as a guide for your own learning and coding. Your
final submitted work should be written and understood by you.

## Suggested Problem Statement

A small community library needs a simple system to keep track of:

- books in the library
- registered members
- borrowing and returning books
- loan records saved in files

The system should let a librarian use a menu to add books, register members,
search books, borrow books, return books, and view records.

## Class Design

### Book

Represents one book in the library.

Suggested attributes:

- `isbn`
- `title`
- `author`
- `category`
- `is_available`

Suggested methods:

- `display_info()`
- `borrow_book()`
- `return_book()`
- `update_details()`

### Member

Represents one library member.

Suggested attributes:

- `member_id`
- `name`
- `email`
- `borrowed_books`

Suggested methods:

- `display_info()`
- `borrow()`
- `return_book()`
- `list_borrowed_books()`

### LoanRecord

Represents one borrowing transaction.

Suggested attributes:

- `record_id`
- `member_id`
- `isbn`
- `borrow_date`
- `return_date`
- `status`

Suggested methods:

- `create_record()`
- `close_record()`
- `display_record()`
- `is_active()`

### Library

Controls the whole system.

Suggested attributes:

- `books`
- `members`
- `loan_records`

Suggested methods:

- `add_book()`
- `register_member()`
- `search_book()`
- `borrow_book()`
- `return_book()`
- `list_books()`

## Module Plan

- `book.py`: contains the `Book` class.
- `member.py`: contains the `Member` class.
- `loan_record.py`: contains the `LoanRecord` class.
- `library.py`: contains the `Library` class.
- `data_handler.py`: contains CSV reading and writing helper functions.
- `main.py`: contains the interactive menu.
- `data/books.csv`: stores book records.
- `data/members.csv`: stores member records.
- `data/loans.csv`: stores loan records.

## Step-by-Step Build Order

1. Complete `Book` first and test it with simple objects.
2. Complete `Member` and test borrowed book storage.
3. Complete `LoanRecord` and practise creating/closing records.
4. Complete CSV functions in `data_handler.py`.
5. Complete `Library` so it connects books, members, and loans.
6. Complete `main.py` so the user can operate the system from a menu.
7. Test normal and incorrect inputs.
8. Write your report using `REPORT_OUTLINE.md`.

## Testing Ideas

Test examples you can show in the report:

- Add a new book.
- Register a new member.
- Search for a book that exists.
- Search for a book that does not exist.
- Borrow an available book.
- Try to borrow a book that is already borrowed.
- Return a borrowed book.
- Enter invalid menu input and show exception handling.


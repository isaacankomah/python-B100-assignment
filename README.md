# Library Management System

## Project Purpose

This project is a Python command-line Library Management System designed for a small community library. The system helps a librarian manage books, register members, search for books, and record borrowing and returning activities. It reduces manual record keeping by storing library data in CSV files.

## Features

- Add new books to the library.
- Register new library members.
- Search for books by title, author, category, or ISBN.
- Borrow books for registered members.
- Return borrowed books.
- List all books and members.
- Save and load data using CSV files.
- Handle invalid menu input using exception handling.

## Files

- `main.py`: runs the interactive menu.
- `book.py`: defines the `Book` class.
- `member.py`: defines the `Member` class.
- `loan_record.py`: defines the `LoanRecord` class.
- `library.py`: manages books, members, and loan records.
- `data_handler.py`: handles CSV file reading and writing.
- `data/books.csv`: stores book records.
- `data/members.csv`: stores member records.
- `data/loans.csv`: stores loan records.

## How to Run

Make sure Python is installed on your computer.

Open the project folder in a terminal and run:

```bash
python main.py
```

## Example Usage

When the program starts, the user sees this menu:

```text
Library Management System
1. Add book
2. Register member
3. Search book
4. Borrow book
5. Return book
6. List books
7. List members
8. Exit
```

Example of adding a book:

```text
Enter your choice: 1
Enter ISBN: 9781234567890
Enter title: Introduction to Chemistry
Enter author: Isaac Ankomah
Enter category: Chemistry
Book added successfully.
```

Example of registering a member:

```text
Enter your choice: 2
Enter member ID: ANKOLIB001
Enter member name: Isaac Ankomah
Enter member email: isaackkankomah@gmail.com
Member registered successfully.
```

Example of borrowing a book:

```text
Enter your choice: 4
Enter member ID: ANKOLIB001
Enter ISBN of book to borrow: 9781234567890
Book borrowed successfully.
```

Example of returning a book:

```text
Enter your choice: 5
Enter member ID: ANKOLIB001
Enter ISBN of book to return: 9781234567890
Book returned successfully.
```

## Key Python Concepts Used

- Classes and objects
- Methods
- Loops
- Conditional statements
- File input/output with CSV files
- Exception handling
- Modular programming using multiple Python files
- Docstrings for code readability

## Data Storage

The system stores information in CSV files inside the `data` folder.

- Book details are saved in `data/books.csv`.
- Member details are saved in `data/members.csv`.
- Borrowing records are saved in `data/loans.csv`.

This allows the program to load saved records when it starts and save new changes after books are added, members are registered, or books are borrowed and returned.

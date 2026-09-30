# Student Grade Management System

## Project Description
The Student Grade Management System is a command-line Python application for maintaining student academic records. It allows the user to add student details, enter marks for four subjects, calculate total marks and percentage, assign a grade, search records, display all records, and delete records.

The project uses Python's basic programming concepts and JSON file handling, so it does not require any external Python package.

## Features
- Add a student record
- Validate marks between 0 and 100
- Calculate total and percentage
- Automatically assign grades
- Display all student records
- Search by roll number
- Delete a student record
- Store records permanently in a JSON file

## Requirements
- Python 3.8 or later
- A terminal/command prompt

## Installation
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Make sure Python is installed:
   ```bash
   python --version
   ```

No external dependencies are required.

## How to Run
From the project root directory:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## Usage
Choose an option from the menu:
1. Add student
2. Display all students
3. Search student
4. Delete student
5. Exit

Student data is automatically saved to `data/students.json`.

## Grade Criteria
- 90-100: A+
- 80-89.99: A
- 70-79.99: B
- 60-69.99: C
- 50-59.99: D
- Below 50: F

## Project Structure
```text
student-grade-management/
├── main.py
├── README.md
├── requirements.txt
└── data/
    └── students.json
```

## Concepts Demonstrated
- Variables and data types
- Input/output
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- Exception handling
- File handling
- JSON data storage

import json
from pathlib import Path

DATA_FILE = Path("data/students.json")


def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_students(students):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade


def add_student(students):
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()

    if not name or not roll_no:
        print("Name and roll number cannot be empty.")
        return

    if any(s["roll_no"] == roll_no for s in students):
        print("A student with this roll number already exists.")
        return

    marks = []
    for subject in ["Python", "Mathematics", "Computer Science", "English"]:
        while True:
            try:
                mark = float(input(f"Enter marks in {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total, percentage, grade = calculate_result(marks)

    students.append({
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade
    })
    save_students(students)
    print("Student added successfully.")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n" + "-" * 78)
    print(f"{'Roll No.':<12}{'Name':<22}{'Total':<10}{'Percentage':<14}{'Grade':<10}")
    print("-" * 78)
    for s in students:
        print(f"{s['roll_no']:<12}{s['name']:<22}{s['total']:<10.1f}"
              f"{s['percentage']:<14.2f}{s['grade']:<10}")
    print("-" * 78)


def search_student(students):
    key = input("Enter roll number to search: ").strip()
    for student in students:
        if student["roll_no"] == key:
            print("\nStudent Details")
            print(f"Name       : {student['name']}")
            print(f"Roll No.   : {student['roll_no']}")
            print(f"Marks      : {student['marks']}")
            print(f"Total      : {student['total']}")
            print(f"Percentage : {student['percentage']}%")
            print(f"Grade      : {student['grade']}")
            return
    print("Student not found.")


def delete_student(students):
    key = input("Enter roll number to delete: ").strip()
    for index, student in enumerate(students):
        if student["roll_no"] == key:
            removed = students.pop(index)
            save_students(students)
            print(f"Record for {removed['name']} deleted.")
            return
    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you for using the Student Grade Management System.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()

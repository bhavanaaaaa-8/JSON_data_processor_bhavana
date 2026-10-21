
import json


def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: data.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None


def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully.")


def display_students(data):
    for student in data["students"]:
        print("\nName:", student["name"])
        print("Marks:", student["marks"])
        print("Subjects:", student["subjects"])


def search_student(data):
    name = input("Enter student name: ").strip().lower()

    for student in data["students"]:
        if student["name"].lower() == name:
            print("Student found:", student)
            return

    print("Student not found.")


def filter_students(data):
    try:
        minimum = float(input("Enter minimum marks: "))

        results = [
            student for student in data["students"]
            if student["marks"] >= minimum
        ]

        if results:
            for student in results:
                print(student["name"], "-", student["marks"])
        else:
            print("No matching students found.")

    except ValueError:
        print("Please enter a valid number.")


def show_summary(data):
    students = data["students"]

    if not students:
        print("No student records available.")
        return

    total = len(students)
    average = sum(s["marks"] for s in students) / total
    highest = max(students, key=lambda s: s["marks"])
    lowest = min(students, key=lambda s: s["marks"])

    print("\n--- Summary ---")
    print("Total students:", total)
    print("Average marks:", round(average, 2))
    print("Highest scorer:", highest["name"], highest["marks"])
    print("Lowest scorer:", lowest["name"], lowest["marks"])


def add_student(data):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        subjects = input(
            "Enter subjects separated by commas: "
        ).split(",")

        student = {
            "name": name,
            "marks": marks,
            "subjects": [
                subject.strip()
                for subject in subjects
                if subject.strip()
            ]
        }

        data["students"].append(student)
        save_data(data)

    except ValueError:
        print("Invalid marks.")


def main():
    data = load_data()

    if data is None:
        return

    while True:
        print("\n--- Student Information System ---")
        print("1. Display students")
        print("2. Search student")
        print("3. Filter by marks")
        print("4. Show summary")
        print("5. Add student")
        print("6. Save data")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_students(data)
        elif choice == "2":
            search_student(data)
        elif choice == "3":
            filter_students(data)
        elif choice == "4":
            show_summary(data)
        elif choice == "5":
            add_student(data)
        elif choice == "6":
            save_data(data)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

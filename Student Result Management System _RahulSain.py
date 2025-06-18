

students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    subjects = {}
    total_marks = 0

    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            break
        except ValueError:
            print("❌ Please enter a valid number for subjects.")

    for i in range(num_subjects):
        subject = input(f"Enter name of subject {i+1}: ")
        while True:
            try:
                marks = int(input(f"Enter marks in {subject}: "))
                break
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        subjects[subject] = marks
        total_marks += marks

    percentage = total_marks / num_subjects
    status = "Pass" if percentage >= 33 else "Fail"

    student = {
        "name": name,
        "roll_no": roll_no,
        "subjects": subjects,
        "total": total_marks,
        "percentage": round(percentage, 2),
        "status": status
    }

    students.append(student)
    print("\n✅ Student added successfully!")
    try:
        with open("student_data.txt", "a") as f:
            f.write(str(student) + "\n")
    except Exception as e:
        print(f"⚠️ Error saving to file: {e}")


def display_results():
    if not students:
        print("⚠️ No student data available.\n")
        return

    for s in students:
        print("\n------------------------------")
        print(f"Name       : {s['name']}")
        print(f"Roll No    : {s['roll_no']}")
        print("Marks      :")
        for subject, mark in s['subjects'].items():
            print(f"  {subject}: {mark}")
        print(f"Total      : {s['total']}")
        print(f"Percentage : {s['percentage']}%")
        print(f"Result     : {s['status']}")
        print("------------------------------")


def main():
    while True:
        print("\n=== Student Result Management System ===")
        print("1. Add Student")
        print("2. Display Results")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_results()
        elif choice == "3":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

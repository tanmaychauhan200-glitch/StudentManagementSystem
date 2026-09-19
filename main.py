from student import Student
from student_manager import StudentManager

manager = StudentManager()
students = manager.students
while True:
    print("\n" + "=" * 45)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Add Marks")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 45)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Add New Student ---")
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")

        manager.add_student(Student(id, name, branch))
        print("Student added successfully!")

    elif choice == "2":
      print("\n--- Student Details ---")

      if len(students) == 0:
        print("No students found.")
      else:
         for s in students:
            print("ID:", s.id)
            print("Name:", s.name)
            print("Branch:", s.branch)
            print("Marks:", s.marks)
    

    elif choice == "3":
        print("\n--- Search Student ---")
        id = input("Enter Student ID: ")

        found = False

        for s in students:
            if s.id == id:
                s.show()
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("\n--- Add Marks ---")
        id = input("Enter Student ID: ")

        for s in students:
            if s.id == id:
                subject = input("Enter Subject: ")
                marks = input("Enter Marks: ")
                s.marks[subject] = marks
                manager.save()
                print("Marks added successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("\n--- Delete Student ---")
        id = input("Enter Student ID: ")

        old_count = len(students)
        students = [s for s in students if s.id != id]

        if len(students) < old_count:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("\nThank you for using Student Management System!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")
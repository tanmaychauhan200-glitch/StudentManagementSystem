from student import Student

students = []

while True:
    print("\n1.Add  2.View  3.Search  4.Marks  5.Delete  6.Exit")
    ch = input("Choice: ")

    if ch == "1":
        id = input("ID: ")
        name = input("Name: ")
        branch = input("Branch: ")
        students.append(Student(id, name, branch))

    elif ch == "2":
        for s in students:
            s.show()

    elif ch == "3":
        id = input("ID: ")
        for s in students:
            if s.id == id:
                s.show()

    elif ch == "4":
        id = input("ID: ")
        for s in students:
            if s.id == id:
                subject = input("Subject: ")
                marks = input("Marks: ")
                s.marks[subject] = marks

    elif ch == "5":
        id = input("ID: ")
        students = [s for s in students if s.id != id]

    elif ch == "6":
        break

    else:
        print("Invalid choice")
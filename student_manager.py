class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.save()

    def save(self):
      with open("students.txt", "w") as file:
        for s in self.students:
            file.write(f"{s.id}|{s.name}|{s.branch}|{s.marks}\n")
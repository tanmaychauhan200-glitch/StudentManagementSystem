class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        for student in self.students:
            student.show()

    def search_student(self, id):
        for student in self.students:
            if student.id == id:
                student.show()

    def delete_student(self, id):
        self.students = [s for s in self.students if s.id != id]
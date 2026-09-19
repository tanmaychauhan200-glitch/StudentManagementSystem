class Student:
    def __init__(self, id, name, branch):
        self.id = id
        self.name = name
        self.branch = branch
        self.marks = {}

    def show(self):
        print(self.id, self.name, self.branch, self.marks)
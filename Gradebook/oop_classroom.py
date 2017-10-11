from oop_students import Student


class Classroom(Student):
    # Start of classroom class.

    def __init__(self, name, teacher):
        # Create class with class name, teacher name, and roster array.
        self.name = name
        self.teacher = teacher
        self.roster = {}

    def add_student(self, student_name, ID):
        # Add student to roster array.
        self.roster[student_name] = super(Classroom, self).__init__(student_name, ID)

    def get_student_roster(self, roster):
        # Print all currently enrolled students.
        print(self.roster)

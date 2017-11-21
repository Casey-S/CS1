from oop_students import Student


class Classroom(Student):
    # Start of classroom class.

    def __init__(self, class_name, teacher_name):
        # Create class with class name, teacher name, and roster array.
        self.class_name = class_name
        self.teacher_name = teacher_name
        self.roster = {}

    def add_student(self, student_name, ID):
        # Add student to roster array.
        # self.roster[student_name] = super(Classroom, self).__init__(student_name, ID)
        self.roster[student_name] = ID

    def get_student_roster(self, roster):
        # Print all currently enrolled students.
        print(self.roster)

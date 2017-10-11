from oop_classroom import Classroom
from oop_students import Student


def setup_classroom():
    classroom = Classroom("CS1", "Yo Mamma")
    return classroom


def test_add_student_to_roster():
    classroom = setup_classroom()
    classroom.add_student("Test Student", 22)
    assert classroom.roster == {"Test Student": 22}

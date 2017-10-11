from oop_students import Student


def setup_student():
    # Create a new student entry.
    student = Student("Jeffrey Lebowski", 42)
    return student


def setup_student_assignments():
    # Add assignments to new student entry.
    student = setup_student()
    student.assignments = {"Retrieve Rug": 0, "Bowl": 70, "Abide": 100}
    return student


def test_student():
    # Test student creation.
    student = setup_student()
    assert student.name == "Jeffrey Lebowski"
    assert student.ID == 42


def test_add_assignment():
    # Test adding an assignment with score to assignments dict.
    student = setup_student()
    student.add_assignment("Defeat Nihilists", 20)
    assert student.assignments["Defeat Nihilists"] == 20


def test_remove_assignment():
    # Test removing entry from assignment dict.
    student = setup_student_assignments()
    student.remove_assignment("Retrieve Rug")
    assert student.assignments == {"Bowl": 70, "Abide": 100}


def test_update_assignment():
    # Test updating the score value in an assignment dict entry.
    student = setup_student_assignments()
    student.update_assignment("Bowl", 90)
    assert student.assignments["Bowl"] == 90


def test_get_assignment_score():
    # Test retrieving assignment dict entry value.
    student = setup_student_assignments()
    student.get_score("Abide")
    assert student.get_score("Abide") == 100


def test_get_GPA():
    # Test accuracy of GPA - (Abide + Bowl + Retrieve Rug) / 3
    student = setup_student_assignments()
    student.get_GPA(student.assignments)
    assert student.get_GPA(student.assignments) == 56

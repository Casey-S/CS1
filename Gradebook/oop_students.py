class Student(object):
    # Start of student class

    def __init__(self, name, ID):
        # Create student object with name and ID, create assignments dict.
        self.name = name
        self.ID = ID
        self.assignments = {}

    def add_assignment(self, assignment_name, score):
        # Add student assignment to assignments array with corresponding score.
        self.assignments[assignment_name] = score

    def remove_assignment(self, assignment_name):
        # Removes given assignment from assignment array.
        del self.assignments[assignment_name]

    def update_assignment(self, assignment_name, updated_score):
        # Updates assignment with an updated score.
        self.assignments[assignment_name] = updated_score

    def get_score(self, assignment_name):
        # Return the value of given assignment name.
        return self.assignments.get(assignment_name)

    def get_GPA(self, assignments):
        # Returns average score from all assignments.
        score_total = 0
        for assignment in self.assignments:
            score = self.assignments[assignment]
            score_total += score
        return score_total / len(self.assignments)

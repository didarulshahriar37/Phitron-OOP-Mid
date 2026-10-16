from Student import Student

class StudentDatabase:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        for st in self.student_list:
            if st.student_id == student.student_id:
                raise ValueError('Student already exists.')

        self.student_list.append(student)

    def view_all_students(self):
        if not self.student_list:
            print('No students found.')
            return

        for student in self.student_list:
            student.view_student_info()
            print('====================')
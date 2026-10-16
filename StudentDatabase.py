class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, student):
        for st in self.student_list:
            if st.student_id == student.student_id:
                raise ValueError(f'!!!!!! Student {st.student_id} already exists !!!!!!')

        self.student_list.append(student)

    @classmethod
    def view_all_students(self):
        if not self.student_list:
            print('No students found.')
            return

        for student in self.student_list:
            student.view_student_info()
            print('====================')
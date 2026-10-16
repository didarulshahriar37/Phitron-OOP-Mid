class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

        def enroll_student():
            if not is_enrolled:
                is_enrolled = True

        def drop_student():
            is_enrolled = False

        def view_student_info(student_id, name, department, is_enrolled):
            print(f'Student ID: {student_id}\nName: {name}\nDepartment: {department}\nEnrollment Status: {is_enrolled}')
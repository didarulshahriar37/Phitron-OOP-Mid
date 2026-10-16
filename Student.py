class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__department

    @property
    def is_enrolled(self):
        return self.__is_enrolled
    
    def enroll_student(self):
        if self.__is_enrolled:
            raise ValueError('Student is already enrolled.')
        else:
            self.__is_enrolled = True
            print('Student enrolled successfully..')

    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError('Student not found.')
        else:
            self.__is_enrolled = False
            print('Student dropped successfully..')

    def view_student_info(self):
        if self.__is_enrolled:
            enrollment_status = 'Enrolled'
        else:
            enrollment_status = 'Not enrolled'

        print(f'Student ID: {self.__student_id}\nName: {self.__name}\nDepartment: {self.__department}\nEnrollment Status: {enrollment_status}')
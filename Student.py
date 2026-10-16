from StudentDatabase import StudentDatabase

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
            print('Student enrolled successfully.')

    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError('Student enrollment not found.')
        else:
            self.__is_enrolled = False
            print('Student dropped successfully.')

    def view_student_info(self):
        if self.__is_enrolled:
            enrollment_status = 'Enrolled'
        else:
            enrollment_status = 'Not enrolled'

        print(f'Student ID: {self.__student_id}\nName: {self.__name}\nDepartment: {self.__department}\nEnrollment Status: {enrollment_status}')

student1 = Student('137', "Didarul Shahriar", "SWE", True)
student2 = Student('138', "Shahriar Didarul", "CSE", False)
student3 = Student('107', "Cristiano Ronaldo", "EEE", True)
student4 = Student('110', "Leonel Messi", "BTM", False)
# student5 = Student('137', "Didarul Shahriar", "SWE", True)

try:
    StudentDatabase.add_student(student1)
    StudentDatabase.add_student(student2)
    StudentDatabase.add_student(student3)
    StudentDatabase.add_student(student4)
    # StudentDatabase.add_student(student5)
except ValueError as error:
    print(error)
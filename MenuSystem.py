from Student import Student
from StudentDatabase import StudentDatabase

database = StudentDatabase()

while True:
    print('1. View All Students\n2. Enroll Student\n3. Drop Student\n4. Exit')
    
    option = input('Select an option: ')

    if option == '1':
        database.view_all_students()

    elif option == '2':
        student_id = input('Enter Student ID: ')

        for student in database.student_list:
            if student.student_id == student_id:
                try:
                    student.enroll_student()
                except ValueError as error:
                    print(error)
            else:
                print('Student not found.')
    
    elif option == '3':
        student_id = input('Enter Student ID: ')
        
        for student in database.student_list:
            if student.student_id == student_id:
                try:
                    student.enroll_student()
                except ValueError as error:
                    print(error)
            else:
                print('Student not found.')
                
    elif option == '4':
        print('Exiting...')
        break
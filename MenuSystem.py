from Student import Student
from StudentDatabase import StudentDatabase

while True:
    print('\n\n--- Student Management Menu ---')
    print('1. View All Students\n2. Enroll Student\n3. Drop Student\n4. Exit')
    
    option = input('Select an option (1-4): ')

    if option == '1':
        StudentDatabase.view_all_students()

    elif option == '2':
        student_id = input('Enter Student ID to enroll: ')

        student = None

        for st in StudentDatabase.student_list:
            if st.student_id == student_id:
                student = st
                break

        if student is None:
            print('Student not found.')
        else:
            try:
                student.enroll_student()
            except ValueError as error:
                print(error)
    
    elif option == '3':
        student_id = input('Enter Student ID to drop: ')

        student = None
        
        for st in StudentDatabase.student_list:
            if st.student_id == student_id:
                student = st
                break

        if student is None:
            print('Student not found.')
        else:
            try:
                student.drop_student()
            except ValueError as error:
                print(error)

    elif option == '4':
        print('Exiting...')
        break
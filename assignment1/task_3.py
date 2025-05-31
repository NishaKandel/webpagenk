# Implement a program to store student records (name, roll, contact number) using a dictionary. 
# a. Provide menu options to add, search, and display students.

student_records = []
loop = True

while loop:

    user_input = input('Enter:/n 1)Add record/n 2)Search record/n 3)Display all record/n 4)Exit/n')

    if user_input == "1":
        name = input('Enter name: ')
        roll_no = input('Enter roll number: ')
        marks_percent = input('Enter marks percentage: ')
        contact_num = input('Enter contact number: ')
        data = {'name': name, 'roll': roll_no, 'marks': marks_percent, 'contact': contact_num}
        student_records.append(data)
        print(f'Inserted data: {data}')

    elif user_input == "2":
        search = input('Enter student name to search for his/her record: ')

        for student in student_records:
            if(student['name'] == search):
                print(f"Name: {student['Name']} Roll Number: {student['roll']} Marks: {student['marks']} Contact: {student['contact']}")

    elif user_input == "3":
        for student in student_records:
            print(f"Name: {student['name']} Roll Number: {student['roll']} Marks: {student['marks']} Contact: {student['contact']}")

    elif user_input =="4":
        loop = False

    else:
        print("Invalid option")

    
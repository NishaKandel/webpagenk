# Create a program that takes a list of student names and stores them in a file. Then, read the file and display the contents.

num = int(input('Total number of students: '))

with open("data.txt", 'w') as file:
    for i in range(num):
        name = input('Input name: ')
        file.write(name+'/n')
print('/nDisplaying student names')

with open("data.txt", 'r') as file:
    for row in file:
        print(row)

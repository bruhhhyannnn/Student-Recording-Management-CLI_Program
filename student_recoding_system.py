# Student Recoding Management Program
import os

student_list = []


def dashboard():
    print("| Student Recoding Management Program |")
    print("[1] Add Student")
    print("[2] Search Student")
    print("[3] Display All Students")
    print("[0] Exit")
    choice = int(input("Enter your choice: "))
    validateChoice(choice)


def validateChoice(choice):
    choices = [1, 2, 3, 0]
    if choice not in choices:
        print("Invalid Choice.")
        os.system("cls")
        return
    if choice == 1:
        addStudent()
        return
    elif choice == 2:
        searchStudent()
        return
    elif choice == 3:
        displayStudents()
        return
    elif choice == 0:
        exit()


def addStudent():
    student = studentInfo()
    student_list.append(student)
    print(">>> Added Student!")
    pauseOutput()


def studentInfo():
    student_number = str(input("Student number: "))
    full_name = str(input("Full Name: "))
    age = int(input("Age: "))

    student = []
    student.append(student_number)
    student.append(full_name)
    student.append(age)
    return student


def searchStudent():
    index = 0
    student_number = str(input("Student number: "))
    for student in student_list:
        if student_number == student[0]:
            editStudent(index, student)
            break
        index += 1
    else:
        print(">>> Student not found ~")
        pauseOutput()


def editStudent(index, student):
    print("\n")
    print("Student Number: " + student[0], "Name: " + student[1] + "\n")
    print("What do you want to do next?")
    print("[1] Update Student Information")
    print("[2] Delete Student Record")
    print("[0] Go Back...")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 1:
        updateStudent(index, student)
    elif choice == 2:
        deleteStudent(index, student)
    else:
        pauseOutput()


def updateStudent(index, student):
    print("[1] Student Number")
    print("[2] Full name")
    print("[3] Age")
    print("[0] Go back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_list[index][choice -
                            1] = str(input("Enter new Student Number: "))
        print(">>> Student Updated!")
    elif choice == 2:
        student_list[index][choice - 1] = str(input("Enter new Full Name: "))
        print(">>> Student Updated!")
    elif choice == 2:
        student_list[index][choice - 1] = str(input("Enter new Age: "))
        print(">>> Student Updated!")
    elif choice == 0:
        editStudent(index, student)
    else:
        pauseOutput()
        editStudent(index, student)


def deleteStudent(index, student):
    print("\n")
    print("Are you sure you want to drop student?")
    print("[1] Yes")
    print("[0] No")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_list.pop(index)
        print(">>> Student Dropped!")

    elif choice == 0:
        editStudent(index, student)
    else:
        pauseOutput()
        editStudent(index, student)


def displayStudents():
    for i in student_list:
        print("Student Number: " + i[0], "Name: " + i[1], end="\n")
    print("\n")
    print("Do you want to display detailed records? ")
    print("[1] Yes")
    print("[0] No")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        displayDetailedRecords()
    else:
        pauseOutput()


def displayDetailedRecords():
    for i in student_list:
        print(i, end="\n")
    print("\n")
    pauseOutput()


# Output Util
def pauseOutput():
    input("Please Enter any key to continue ...")
    return


while True:
    os.system("cls")
    dashboard()

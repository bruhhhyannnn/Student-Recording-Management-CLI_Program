# Student Recoding Management Program
import os

file_path = 'Side Projects\\CLI Programs\\Automation with Python - freeCodeCamp\\test.txt'
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
        return
    elif choice == 1:
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
    else:
        print("Invalid Choice.")
        return


def addStudent():
    student = getStudentInfo()
    with open(file_path, 'a') as file:
        file.write("\n")
        for info in student:
            if info == student[len(student) - 1]:
                file.write(str(info))
                print(">>> Added Student!")
                pauseOutput()
                break
            file.write(str(info) + ", ")


def getStudentInfo():
    student_number = str(input("Student number: "))
    full_name = str(input("Full Name: "))
    age = int(input("Age: "))
    birthdate = str(input("Birthday: "))
    barangay = str(input("Barangay: "))
    city = str(input("City: "))
    province = str(input("Province: "))
    phone_number = int(input("Phone Number: "))
    email = str(input("Email: "))
    mother_name = str(input("Mother's Name: "))
    father_name = str(input("Father's Name: "))

    student_info = []
    student_info.append(student_number)
    student_info.append(full_name)
    student_info.append(age)
    student_info.append(birthdate)
    student_info.append(barangay)
    student_info.append(city)
    student_info.append(province)
    student_info.append(phone_number)
    student_info.append(email)
    student_info.append(mother_name)
    student_info.append(father_name)
    return student_info


def searchStudent():
    student_number = getStudentNumber()
    found_student = False
    student_index = 0
    student = []
    with open(file_path, 'r') as file:
        students_length = len(file.readlines())
        file.seek(0)
        while students_length > 0:
            student = file.readline().split(',')
            if student[0] == student_number:
                found_student = True
                break
            students_length -= 1
            student_index += 1

    if found_student:
        print(">>> Student found ~")
        editStudent(student_index, student)
    else:
        print(">>> Student not found ~")
        pauseOutput()


def getStudentNumber():
    student_number = str(input("Student number: "))
    return student_number


def editStudent(student_index, student):
    print("\n")
    print("Student Number: " + student[0],
          "\tName: " + student[1].strip() + "\n")
    print("What do you want to do next?")
    print("[1] Update Student Information")
    print("[2] Delete Student Record")
    print("[0] Go Back...")
    choice = int(input("Enter your choice: "))
    print("\n")
    if choice == 1:
        updateStudent(student_index, student)
    elif choice == 2:
        deleteStudent(student_index)
    else:
        pauseOutput()
        return


def updateStudent(student_index, student):
    print(student)
    print("What do you want to update?")
    print("[1] Student Number")
    print("[2] Full name")
    print("[3] Age")
    print("[4] Birthday")
    print("[5] Barangay")
    print("[6] City")
    print("[7] Province")
    print("[8] Phone Number")
    print("[9] Email")
    print("[10] Mother's Name")
    print("[11] Father's Name")
    print("[0] Go back")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student[choice - 1] = str(input("Enter new Student Number: "))
    elif choice == 2:
        student[choice - 1] = str(input("Enter new Full Name: "))
    elif choice == 3:
        student[choice - 1] = int(input("Enter new Age: "))
    elif choice == 4:
        student[choice - 1] = str(input("Enter new Birthday: "))
    elif choice == 5:
        student[choice - 1] = str(input("Enter new Barangay: "))
    elif choice == 6:
        student[choice - 1] = str(input("Enter new City: "))
    elif choice == 7:
        student[choice - 1] = str(input("Enter new Province: "))
    elif choice == 8:
        student[choice - 1] = int(input("Enter new Phone Number: "))
    elif choice == 9:
        student[choice - 1] = str(input("Enter new Email: "))
    elif choice == 10:
        student[choice - 1] = str(input("Enter new Mother's Name: "))
    elif choice == 11:
        student[choice - 1] = str(input("Enter new Father's Name: "))
    else:
        pauseOutput()
        return

    with open(file_path, 'r+') as file:
        while student_index > 0:
            file.readline()
            student_index -= 1
        for info in student:
            if info == student[len(student) - 1]:
                file.write(str(info.strip()))
                break
            file.write(str(info.strip()) + ", ")
    print(">>> Student Updated!")
    pauseOutput()


def deleteStudent(student_index):
    print("\n")
    print("Are you sure you want to drop student?")
    print("[1] Yes")
    print("[0] No")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for i, line in enumerate(lines):
                if i != student_index:
                    file.write(line)
        print(">>> Student Dropped!")
        pauseOutput()
    else:
        pauseOutput()
        return


def displayStudents():
    with open(file_path, 'r') as file:
        students_length = len(file.readlines())
        file.seek(0)
        while students_length > 0:
            student_info = file.readline().split(',')
            print(
                f"Student Number: {student_info[0]} Name: {student_info[1].strip()}")
            students_length -= 1
    print("\n")
    print("Do you want to display detailed records? ")
    print("[1] Yes")
    print("[0] No")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        displayDetailedRecords()
    else:
        pauseOutput()
        return


def displayDetailedRecords():
    with open(file_path, 'r') as file:
        students_length = len(file.readlines())
        file.seek(0)
        while students_length > 0:
            print(" >>> " + file.readline(), end="")
            students_length -= 1
    print("\n")
    pauseOutput()


# Output Util
def pauseOutput():
    input("Please Enter any key to continue ...")
    return


while True:
    os.system("cls")
    dashboard()

from weakref import finalize

students_information={
    "student1":{
    "fullname": "Yibeltal Marie",
     # "lastname": "Marie",
     "gender": "M",
     "age": 21,
     "studentID": 1411 / 16,
     "grade": 3.92,
    "phonenumber":915258501,
    "emailaddress":"@gmail.com"},

}
# print(students_information["student1"]["full_name"])

# to make the user able to add new student to the database
print("if you want to add new student to the data base , type 'add'.")
print("if you want to view a spefic student, type 'view'. ")
print("if you want to see all the list of students , type 'all'.")
print("if you want to update the specific student information , type 'update'. ")
print("if you want to delete the specific student information , type 'delete'.")

count = 2
def add_student(count,full_name,gender,age,Id,grade,phone,email):
    new_student = {}
    new_student["fullname"] = full_name
    # new_student["lastname"] = last_name
    new_student["gender"] = gender
    new_student["age"]  = age
    new_student["studentID"] = Id
    new_student["grade"] = grade
    new_student["phonenumber"] = phone
    new_student["emailaddress"] = email
    students_information[f"student{count}"] = new_student
final_choice = "no"
while final_choice == "no":
    task = input("Enter your task( want to 'add','view','see all list','update','delete' students) :")

    if task == "add":
        full_name = input("please enter the new student full name: ").title()
        # last_name = input("Enter a student's last name: ").title()
        gender = input("Enter the gender of a student: ").title()
        age  = int(input("Enter age of a student: "))
        Id = int(input("Enter the new student's Id: "))
        grade = float(input("Enter a student's grade: "))
        phone = int(input("Enter student's phone number: "))
        email = input("Enter a student's email address: ")
        add_student(count,full_name,gender,age,Id,grade,phone,email)
        count += 1
# to allow the user to view the details of a specific student

    if task == "view":
        want_student = input("Please enter a student's name you want to view? ").title()
        for key in students_information:
            if students_information[key]["fullname"] == want_student:
                print(f"full name: {students_information[key]["fullname"]}")
                # print(f"last name: {students_information[key]["lastname"]}")
                print(f"Gender: {students_information[key]["gender"]}")
                print(f"Age: {students_information[key]["age"]}")
                print(f"Student id: {students_information[key]["studentID"]}")
                print(f"grade: {students_information[key]["grade"]}")
                print(f"phone number: {students_information[key]["phonenumber"]}")
                print(f"email address: {students_information[key]["emailaddress"]}")
                print(" ")
            elif students_information == { }:
                print("there is no any list of names in the data base")
            else:
                print("student's name you enter is not in the list.")

# to let the user see the list of all students in the data base
    if task == "all":
        for key in students_information:
            print("full name: ",students_information[key]["fullname"])
            # print("last name: ",students_information[key]["lastname"])
            print("Gender: ",students_information[key]["gender"])
            print("Age: ",students_information[key]["age"])
            print("Student ID: ",students_information[key]["studentID"])
            print("Grade: ",students_information[key]["grade"])
            print(f"phone number: {students_information[key]["phonenumber"]}")
            print(f"email address: {students_information[key]["emailaddress"]}")


# to let the user delete the information of the specific student
    if task == "delete":
        name_delete = input("Enter the full name of a student you to delete: ").title()
        keys_to_remove = [key for key in students_information]

        for key in keys_to_remove:
            if students_information[key]["fullname"] == name_delete:
                students_information.pop(key)
                print(f"student {name_delete}'s information is deleted")
        # else:
        #     print("the student's name you entered is not in the list student database")

# to let the user update the specific student's information

    if task == "update":
        name = input("Enter the student's full name you want to update: ").title()
        for key in students_information:
            if students_information[key]["fullname"] == name:
                user_choice = "yes"
                while user_choice == "yes":
                    change = input("what information is you want to update(fullname/gender/age/studentID/grade/phone number/email address)")
                    user_change = input(f"Enter the {change} of a student: ")
                    students_information[key][change]=user_change
                    user_choice = input("is there any information you want to update ('yes' / 'no')")


    final_choice = input("have finished your work , do want to leave ?(press 'no' to continue/else)")


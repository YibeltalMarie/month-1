students_information={
    "student1":{
    "fullname": "Yibeltal Marie",
     # "lastname": "Marie",
     "gender": "male",
     "age": 21,
     "studentID": "ETS11453/16",
     "grade": 3.92,
    "phone":915258501,
    "email":"@gmail.com"},
}


def add_student(full_name,
                gender, age,
                student_id,
                grade, phone, email):

    new_student = {
        "fullname": full_name,
        "gender": gender,
        "age": age,
        "studentID": student_id,
        "grade": grade,
        "phone": phone,
        "email": email
    }
    students_information[f"student {len(students_information) + 1}"] = new_student


def register():
    print("Enter student information")
    full_name = prompt("Full Name: ").title()
    gender = prompt("Gender: ").title()
    age = int(prompt("Age: "))
    student_id = prompt("Id: ")
    grade = float(prompt("Grade: "))
    phone = int(prompt("Phone Number: "))
    email = prompt("Email: ")
    add_student(full_name, gender, age, student_id, grade, phone, email)


def search():
    full_name = prompt("Full Name: ").title()
    for key in students_information:
        if students_information[key]["fullname"] == full_name:
            print(f"full name: {students_information[key]["fullname"]}")
            print(f"Gender: {students_information[key]["gender"]}")
            print(f"Age: {students_information[key]["age"]}")
            print(f"Student id: {students_information[key]["studentID"]}")
            print(f"grade: {students_information[key]["grade"]}")
            print(f"phone number: {students_information[key]["phone"]}")
            print(f"email : {students_information[key]["email"]}")
            print(" ")
    else:
        print("Student not found!")


def view():
    print("_________________________________________________________________________________")
    print(":Full Name     : Gender : Age : Student ID : Grade : Phone number : Email :")
    for key in students_information:

        print(f":{students_information[key]["fullname"]}: {students_information[key]["gender"]} ",
              f"   :{students_information[key]["age"]}    :{students_information[key]["studentID"]}:",
              f" {students_information[key]["grade"]}:   {students_information[key]["phone"]}",
              f"   : {students_information[key]["email"]}")
    print("----------------------------------------------------------------------------------")

def delete():
    print("Welcome ...")
    name_delete = prompt("Full Name: ").title()
    keys_to_remove = [key for key in students_information]
    for key in keys_to_remove:
        if students_information[key]["fullname"] == name_delete:
            students_information.pop(key)
            print(f"student {name_delete}'s information is deleted")


def prompt(message):
    user_input = input(message)
    return user_input


def update():
    print("Update Student information...")
    name = prompt("Full Name: ").title()
    for key in students_information:
        if students_information[key]["fullname"] == name:
            user_choice = "yes"
            while user_choice == "yes":
                change = input(
                    "Update { fullname,gender,  age,studentID,grade, phone, email }:")
                user_change = input(f"{change}: ")
                students_information[key][change] = user_change
                user_choice = input("is there any information you want to update ('yes' / 'no')")

print('''
======== description =======
    1. Register
    2. Update
    3. Delete
    4. View
    5. Search
    6. Exit
''')

response = "yes"
while response.upper() != "NO":
    choice = int(input("Choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    elif choice == 4:
        view()
    elif choice == 5:
        search()
    elif choice == 6:
        break
    else:
        print("Please try again!")
    response  = input("Do you want to continue? [Yes/No]: ")


# while response.upper() != "NO":
#     choice = int(input("Choice: "))
#     match choice:
#         case 1:
#             register()
#             break
#         case 2:
#             update()
#             break
#         case 3:
#             delete()
#             break
#         case 4:
#             view()
#             break
#         case 5:
#             search()
#             break
#         case 6:
#             break
#         case _ :
#             continue
#             print("Please try again!")
#
#     response  = input("Do you want to continue? [Yes/No]: ")

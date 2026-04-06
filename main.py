students = []

#  Add Student
def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    age = input("Enter Age: ")
    
    try:
        marks = float(input("Enter Marks: "))
    except:
        print(" Invalid marks")
        return

    student = {
        "name": name,
        "roll": roll,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print(" Student added successfully\n")


# Search Student
def search_student():
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s['roll'] == roll:
            print("\n===== Student Found =====")
            print(f"Name  : {s['name']}")
            print(f"Roll  : {s['roll']}")
            print(f"Age   : {s['age']}")
            print(f"Marks : {s['marks']}")
            print(f"Grade : {calculate_grade(s['marks'])}\n")
            return

    print("Student not found\n")
#  Grade Calculation
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"
#  Update Student
def update_student():
    roll = input("Enter Roll Number to update: ")

    for s in students:
        if s['roll'] == roll:
            print("\n--- Update Details ---")
            s['name'] = input("Enter new name: ")
            s['age'] = input("Enter new age: ")

            try:
                s['marks'] = float(input("Enter new marks: "))
            except:
                print("Invalid marks")
                return

            print(" Student record updated successfully\n")
            return

    print(" Student not found\n")


#  View All Students 
def view_students():
    if not students:
        print(" No records found\n")
        return

    print("\n===== All Students =====")
    for s in students:
        print(f"{s['name']} | Roll: {s['roll']} | Marks: {s['marks']} | Grade: {calculate_grade(s['marks'])}")
    print()


# Menu System function 
def menu():
    while True:
        print("===== Student Record System =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            view_students()
        elif choice == '5':
            print(" Exiting...")
            break
        else:
            print(" Invalid choice\n")


#  Run all the main function 
menu()
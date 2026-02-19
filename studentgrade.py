# ===============================================
#        STUDENT GRADE CALCULATOR SYSTEM
# ===============================================

import csv

# -------------------------------
# Function to calculate grade
# -------------------------------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


# -------------------------------
# Function to calculate result
# -------------------------------
def calculate_result(marks_list):
    for mark in marks_list:
        if mark < 40:
            return "FAIL"
    return "PASS"


# -------------------------------
# Function to add student
# -------------------------------
def add_student():
    student = {}

    student["roll"] = input("Enter Roll Number: ")
    student["name"] = input("Enter Student Name: ")

    subjects = int(input("Enter number of subjects: "))
    marks = []

    for i in range(subjects):
        mark = float(input(f"Enter marks for Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / subjects

    grade = calculate_grade(percentage)
    result = calculate_result(marks)

    student["marks"] = marks
    student["total"] = total
    student["percentage"] = percentage
    student["grade"] = grade
    student["result"] = result

    return student


# -------------------------------
# Function to display student
# -------------------------------
def display_student(student):
    print("\n----------------------------------")
    print("Roll Number :", student["roll"])
    print("Name        :", student["name"])
    print("Marks       :", student["marks"])
    print("Total       :", student["total"])
    print("Percentage  :", round(student["percentage"], 2), "%")
    print("Grade       :", student["grade"])
    print("Result      :", student["result"])
    print("----------------------------------\n")


# -------------------------------
# Save to CSV File
# -------------------------------
def save_to_file(students, filename="student_results.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Total", "Percentage", "Grade", "Result"])

        for s in students:
            writer.writerow([
                s["roll"],
                s["name"],
                s["total"],
                round(s["percentage"], 2),
                s["grade"],
                s["result"]
            ])

    print("Data saved successfully to", filename)


# -------------------------------
# Calculate class average
# -------------------------------
def class_average(students):
    if len(students) == 0:
        print("No student data available.")
        return

    total_percentage = sum(s["percentage"] for s in students)
    avg = total_percentage / len(students)
    print("Class Average Percentage:", round(avg, 2), "%")


# -------------------------------
# Main Program
# -------------------------------
def main():
    students = []

    while True:
        print("\n====== STUDENT GRADE CALCULATOR ======")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Class Average")
        print("4. Save to File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student = add_student()
            students.append(student)
            print("Student added successfully!")

        elif choice == "2":
            if len(students) == 0:
                print("No students available.")
            else:
                for s in students:
                    display_student(s)

        elif choice == "3":
            class_average(students)

        elif choice == "4":
            save_to_file(students)

        elif choice == "5":
            print("Exiting program... Thank You!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the program
if __name__ == "__main__":
    main()

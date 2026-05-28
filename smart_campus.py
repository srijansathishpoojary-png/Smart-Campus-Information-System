# =========================================================
# SMART CAMPUS INFORMATION SYSTEM (Integrated Lab 1 - Lab 8)
# =========================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


student_list = []
course_enrollment_records = {}


# =========================================================
# LAB 1: Student Registration and Grade Evaluation
# =========================================================

def student_registration_grade_evaluation():

    print("\n--- [Lab 1] Student Registration & Grade Evaluation ---")

    name = input("Enter student name: ")

    try:
        score = float(input("Enter exam score (0-100): "))

        if not (0 <= score <= 100):
            print("Error: Score must be between 0 and 100.")
            return

    except ValueError:
        print("Error: Invalid numeric input.")
        return

    if score >= 90:
        grade = "A"
        remark = "Excellent"

    elif score >= 75:
        grade = "B"
        remark = "Very Good"

    elif score >= 60:
        grade = "C"
        remark = "Good"

    elif score >= 40:
        grade = "D"
        remark = "Average"

    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Performance Remark: {remark}")


# =========================================================
# LAB 2: Course Enrollment Management System
# =========================================================

def course_enrollment_management():

    print("\n--- [Lab 2] Course Enrollment Management System ---")

    student_name = input("Enter student name for enrollment: ")

    if student_name not in course_enrollment_records:
        course_enrollment_records[student_name] = []

    courses = course_enrollment_records[student_name]

    max_courses = 5

    print(f"\nMaximum allowed courses = {max_courses}")
    print("Enter 'done' to stop enrollment.")

    while True:

        if len(courses) >= max_courses:
            print("\nMaximum course limit reached!")
            break

        course_name = input("\nEnter course name: ")

        if course_name.lower() == "done":
            break

        if course_name == "":
            print("Course name cannot be empty!")
            continue

        try:
            credits = int(input("Enter subject credits: "))

            if credits <= 0:
                print("Credits must be positive!")
                continue

        except ValueError:
            print("Invalid credit value!")
            continue

        courses.append((course_name, credits))

        print(f"Course '{course_name}' added successfully.")

    print(f"\n--- Enrollment Details for {student_name} ---")

    for course, credit in courses:
        print(f"{course} --> {credit} Credits")

    print("Total Courses Enrolled:", len(courses))


# =========================================================
# LAB 3: Student Record Data Management
# =========================================================

def student_record_management():

    print("\n--- [Lab 3] Student Record Data Management ---")

    print("1. Add Default Records")
    print("2. View Records")

    choice = input("Enter your choice: ")

    if choice == "1":

        student_list.append({
            "name": "Priya",
            "age": 20,
            "id": 105,
            "grades": [85, 90, 78]
        })

        student_list.append({
            "name": "Rahul",
            "age": 21,
            "id": 102,
            "grades": [72, 88, 91]
        })

        student_list.append({
            "name": "Anita",
            "age": 19,
            "id": 110,
            "grades": [95, 89, 92]
        })

        print("\nDefault records added successfully!")

    elif choice == "2":

        if not student_list:
            print("\nNo records available.")
            return

        print("\n--- Student Records ---")

        for student in student_list:

            print(f"\nName : {student['name']}")
            print(f"Age  : {student['age']}")
            print(f"ID   : {student['id']}")
            print(f"Grades : {student['grades']}")

        # SET OPERATIONS

        event_A = {"Priya", "Rahul", "Anita", "Kiran"}
        event_B = {"Rahul", "Anita", "Sneha"}

        print("\n--- Event Analysis ---")

        print("Intersection :", event_A & event_B)
        print("Union :", event_A | event_B)
        print("Difference :", event_A - event_B)

    else:
        print("Invalid choice.")


# =========================================================
# LAB 4: Sorting and Searching Student IDs
# =========================================================

def sorting_and_searching_ids():

    print("\n--- [Lab 4] Sorting and Searching Student IDs ---")

    if student_list:
        local_ids = [student["id"] for student in student_list]

    else:
        local_ids = [105, 102, 110, 108, 101]

    print("\nOriginal IDs :", local_ids)

    # BUBBLE SORT

    bubble_sorted = local_ids.copy()

    n = len(bubble_sorted)

    for i in range(n):

        for j in range(0, n - i - 1):

            if bubble_sorted[j] > bubble_sorted[j + 1]:

                bubble_sorted[j], bubble_sorted[j + 1] = bubble_sorted[j + 1], bubble_sorted[j]

    print("Bubble Sorted IDs :", bubble_sorted)

    # SELECTION SORT

    selection_sorted = local_ids.copy()

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if selection_sorted[j] < selection_sorted[min_index]:
                min_index = j

        selection_sorted[i], selection_sorted[min_index] = (
            selection_sorted[min_index],
            selection_sorted[i]
        )

    print("Selection Sorted IDs :", selection_sorted)

    # SEARCHING

    try:
        target = int(input("\nEnter ID to Search: "))

    except ValueError:
        print("Invalid ID.")
        return

    # LINEAR SEARCH

    linear_found = False

    for i in range(len(bubble_sorted)):

        if bubble_sorted[i] == target:
            print(f"Linear Search: ID found at index {i}")
            linear_found = True
            break

    if not linear_found:
        print("Linear Search: ID not found")

    # BINARY SEARCH

    low = 0
    high = len(bubble_sorted) - 1

    binary_found = False

    while low <= high:

        mid = (low + high) // 2

        if bubble_sorted[mid] == target:
            print(f"Binary Search: ID found at index {mid}")
            binary_found = True
            break

        elif bubble_sorted[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    if not binary_found:
        print("Binary Search: ID not found")


# =========================================================
# LAB 5: Student Fee Calculation using Functions
# =========================================================

def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):

    return tuition_fee + hostel_fee + transportation_fee


def student_fee_calculation_dashboard():

    print("\n--- [Lab 5] Student Fee Calculation ---")

    try:

        tuition = float(input("Enter tuition fee: "))

        hostel_choice = input("Include hostel fee? (y/n): ").lower()

        if hostel_choice == "y":
            hostel = float(input("Enter hostel fee: "))
        else:
            hostel = 0

        transport_choice = input("Include transport fee? (y/n): ").lower()

        if transport_choice == "y":
            transport = float(input("Enter transport fee: "))
        else:
            transport = 0

        total = calculate_fee(tuition, hostel, transport)

        print("\nTotal Fee =", total)

    except ValueError:
        print("Invalid numeric input.")


# =========================================================
# LAB 6: File Handling for Student Academic Records
# =========================================================

def file_handling_records_management():

    print("\n--- [Lab 6] File Handling Records Management ---")

    filename = "student_records.txt"

    print("1. Write Records")
    print("2. Read Records")

    choice = input("Enter choice: ")

    if choice == "1":

        with open(filename, "w") as file:

            file.write("ID,Name,Marks\n")
            file.write("101,Arjun,85\n")
            file.write("102,Meera,92\n")
            file.write("103,Ravi,76\n")
            file.write("104,Anita,89\n")

        print("\nRecords written successfully.")

    elif choice == "2":

        try:

            with open(filename, "r") as file:

                records = file.readlines()

            print("\n--- Stored Records ---")

            for record in records:
                print(record.strip())

        except FileNotFoundError:
            print("File not found. Write records first.")

    else:
        print("Invalid choice.")


# =========================================================
# LAB 7: File-Based Academic Record Management
# =========================================================

def academic_record_management():

    print("\n--- [Lab 7] Academic Record Management ---")

    filename = "academic_records.txt"

    print("1. Add Academic Record")
    print("2. View Academic Records")

    choice = input("Enter choice: ")

    if choice == "1":

        usn = input("Enter USN: ")
        name = input("Enter Student Name: ")
        semester = input("Enter Semester: ")
        sgpa = input("Enter SGPA: ")

        with open(filename, "a") as file:

            file.write(f"{usn},{name},{semester},{sgpa}\n")

        print("\nAcademic record added successfully.")

    elif choice == "2":

        try:

            with open(filename, "r") as file:

                records = file.readlines()

            if not records:
                print("\nNo records found.")
                return

            print("\n--- Academic Records ---")

            for record in records:
                print(record.strip())

        except FileNotFoundError:
            print("\nAcademic record file not found.")

    else:
        print("Invalid choice.")


# =========================================================
# LAB 8: Directory Scanning with Exception Handling
# =========================================================

def directory_scanning():

    print("\n--- [Lab 8] Directory Scanning ---")

    path = input("Enter directory path: ")

    try:

        files = os.listdir(path)

        print("\nFiles and Folders:")

        for file in files:
            print(file)

    except FileNotFoundError:
        print("Directory not found.")

    except PermissionError:
        print("Permission denied.")

    except Exception as e:
        print("Error:", e)


# =========================================================
# STUDENT PERFORMANCE ANALYTICS
# =========================================================

def student_performance_analytics():

    print("\n--- Student Performance Analytics ---")

    names = ["Arjun", "Meera", "Ravi", "Anita"]
    marks = [85, 92, 76, 89]

    # NUMPY ANALYSIS

    average = np.mean(marks)
    highest = np.max(marks)
    lowest = np.min(marks)

    print("\nAverage Marks :", average)
    print("Highest Marks :", highest)
    print("Lowest Marks :", lowest)

    # PANDAS DATAFRAME

    df = pd.DataFrame({
        "Student": names,
        "Marks": marks
    })

    print("\nDataFrame Report:")
    print(df)

    # MATPLOTLIB GRAPH

    plt.figure(figsize=(7, 5))

    plt.bar(names, marks)

    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.title("Student Performance Analytics")

    plt.show()


# =========================================================
# MAIN MENU
# =========================================================

def main():

    while True:

        print("\n" + "=" * 60)
        print(" SMART CAMPUS INFORMATION SYSTEM DASHBOARD ")
        print("=" * 60)

        print("1. Student Registration & Grade Evaluation (Lab 1)")
        print("2. Course Enrollment Management System (Lab 2)")
        print("3. Student Record Data Management (Lab 3)")
        print("4. Sorting and Searching Student IDs (Lab 4)")
        print("5. Student Fee Calculation using Functions (Lab 5)")
        print("6. File Handling for Academic Records (Lab 6)")
        print("7. File-Based Academic Record Management (Lab 7)")
        print("8. Directory Scanning with Exception Handling (Lab 8)")
        print("9. Student Performance Analytics")
        print("10. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            student_registration_grade_evaluation()

        elif choice == "2":
            course_enrollment_management()

        elif choice == "3":
            student_record_management()

        elif choice == "4":
            sorting_and_searching_ids()

        elif choice == "5":
            student_fee_calculation_dashboard()

        elif choice == "6":
            file_handling_records_management()

        elif choice == "7":
            academic_record_management()

        elif choice == "8":
            directory_scanning()

        elif choice == "9":
            student_performance_analytics()

        elif choice == "10":
            print("\nShutting down system dashboard. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose correctly.")


# =========================================================
# RUN PROGRAM
# =========================================================

main()
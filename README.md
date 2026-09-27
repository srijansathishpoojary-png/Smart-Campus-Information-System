# Smart Campus Information System

A Python-based **Smart Campus Information System** that integrates multiple student and academic management features into a single menu-driven application.

The project combines **8 laboratory modules** covering Python fundamentals, data structures, algorithms, functions, file handling, exception handling, and directory operations. It also includes a **Student Performance Analytics** module using NumPy, Pandas, and Matplotlib.

## Features

### 1. Student Registration & Grade Evaluation

* Accepts student name and examination score.
* Validates scores between 0 and 100.
* Automatically assigns grades:

  * **A** – Excellent
  * **B** – Very Good
  * **C** – Good
  * **D** – Average
  * **F** – Needs Improvement
* Displays a student performance report.

### 2. Course Enrollment Management

* Stores courses enrolled by each student.
* Accepts course names and subject credits.
* Allows a maximum of **5 courses** per student.
* Validates course names and credit values.
* Displays enrollment details and total courses.

### 3. Student Record Data Management

* Maintains student records using Python lists and dictionaries.
* Includes sample student records.
* Stores:

  * Student name
  * Age
  * ID
  * Grades
* Demonstrates Python **set operations**:

  * Intersection
  * Union
  * Difference

### 4. Sorting and Searching Student IDs

Demonstrates fundamental searching and sorting algorithms.

**Sorting:**

* Bubble Sort
* Selection Sort

**Searching:**

* Linear Search
* Binary Search

Student IDs are sorted before binary searching is performed.

### 5. Student Fee Calculation

Calculates the total student fee using a reusable function.

The total can include:

* Tuition fee
* Hostel fee
* Transportation fee

The `calculate_fee()` function uses optional parameters for hostel and transportation fees.

### 6. File Handling for Academic Records

Demonstrates basic text-file operations.

The system can:

Write student academic records to student_records.txt
Read and display stored records
Handle missing files using FileNotFoundError
7. File-Based Academic Record Management

Provides persistent academic record management.

Each record contains:

USN
Student Name
Semester
SGPA

Records are stored in academic_records.txt and can be added or viewed through the application.

8. Directory Scanning

Allows the user to enter a directory path and displays its files and folders.

Exception handling is included for:

FileNotFoundError
PermissionError
Other unexpected exceptions
9. Student Performance Analytics

Analyzes student marks using Python data-analysis libraries.

The module calculates:

Average marks
Highest marks
Lowest marks

It also:

Creates a Pandas DataFrame.
Generates a bar chart using Matplotlib.

The source code uses NumPy, Pandas, Matplotlib, and OS functionality.

Technologies Used
Python 3
NumPy – numerical analysis
Pandas – tabular data processing
Matplotlib – data visualization
OS module – directory and filesystem operations
Python built-in data structures:
Lists
Dictionaries
Tuples
Sets
Project Structure
Smart Campus Information System
│
├── Lab 1  → Student Registration & Grade Evaluation
├── Lab 2  → Course Enrollment Management
├── Lab 3  → Student Record Data Management
├── Lab 4  → Sorting & Searching Student IDs
├── Lab 5  → Student Fee Calculation
├── Lab 6  → File Handling
├── Lab 7  → Academic Record Management
├── Lab 8  → Directory Scanning
│
└── Student Performance Analytics

The application exposes all modules through a single main dashboard.

Requirements

Make sure Python 3 is installed.

Install the required external libraries with:

pip install numpy pandas matplotlib

The project uses these libraries for numerical analysis, DataFrame creation, and graphical visualization.

How to Run
Save the Python program as:
smart_campus.py
Install the dependencies:
pip install numpy pandas matplotlib
Run the program:
python smart_campus.py
The Smart Campus dashboard will appear.
Select an option from 1–10.

The main menu provides options for all eight labs, performance analytics, and program exit.

Main Menu
============================================================
 SMART CAMPUS INFORMATION SYSTEM DASHBOARD
============================================================

1. Student Registration & Grade Evaluation (Lab 1)
2. Course Enrollment Management System (Lab 2)
3. Student Record Data Management (Lab 3)
4. Sorting and Searching Student IDs (Lab 4)
5. Student Fee Calculation using Functions (Lab 5)
6. File Handling for Academic Records (Lab 6)
7. File-Based Academic Record Management (Lab 7)
8. Directory Scanning with Exception Handling (Lab 8)
9. Student Performance Analytics
10. Exit
Data Files

The program creates/uses the following text files:

student_records.txt

Used by Lab 6 to store basic academic records.

Example format:

ID,Name,Marks
101,Arjun,85
102,Meera,92
103,Ravi,76
104,Anita,89
academic_records.txt

Used by Lab 7 to store academic records.

Example format:

USN,Name,Semester,SGPA

The actual records are appended as users add academic information.

Concepts Demonstrated

This project is useful for demonstrating a broad range of Python programming concepts:

User input and output
Conditional statements
Loops
Functions
Lists
Dictionaries
Tuples
Sets
Exception handling
File handling
String processing
Sorting algorithms
Searching algorithms
NumPy operations
Pandas DataFrames
Matplotlib visualization
Operating-system directory operations
Algorithms
Bubble Sort

Student IDs are sorted by repeatedly comparing adjacent elements and swapping them when necessary.

Selection Sort

The algorithm repeatedly finds the smallest remaining element and places it in its correct position.

Linear Search

Checks each element sequentially until the target student ID is found.

Binary Search

Searches a sorted list by repeatedly dividing the search range in half.

The sorting and searching implementations are included in Lab 4.

Error Handling

The application includes validation and exception handling for common user errors, including:

Invalid numerical input
Scores outside the 0–100 range
Invalid course credits
Empty course names
Invalid student IDs
Missing files
Missing directories
Permission errors

This helps prevent the application from terminating unexpectedly during normal user interaction.

Performance Analytics

The analytics module uses sample student marks:

Arjun  → 85
Meera  → 92
Ravi   → 76
Anita  → 89

NumPy is used to calculate statistical values, Pandas creates a tabular report, and Matplotlib generates a bar chart.

Learning Objectives

By completing this project, students can demonstrate practical knowledge of:

Python programming fundamentals
Data structures
Functions and modular programming
Searching and sorting algorithms
File management
Exception handling
Basic data analysis
Data visualization
Menu-driven application development

*Future Improvements*

Possible enhancements include:

Add a graphical user interface (GUI).
Store records in a database such as SQLite or MySQL.
Add student login/authentication.
Allow users to edit and delete records.
Add automatic GPA/CGPA calculation.
Export reports to CSV or PDF.
Add attendance management.
Add course timetable management.
Generate more advanced performance charts.
Improve data validation and input sanitization.

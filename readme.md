# Student Record System (Python)

A simple and efficient **Student Record System** built using **Python**.
This application allows users to manage student data, including adding new records, searching for students, and updating academic and personal information.

---

##  Features

*  Add New Student Details
*  Search Student Records (by Roll Number)
*  Update Student Information
*  View All Students
*  Automatic Grade Calculation
*  Menu-driven Interface

---
##  Functionality Overview

###  Add Student

Store student details such as:

* Name
* Roll Number
* Age
* Marks

---

###  Search Student

* Search using **Roll Number**
* Displays:

  * Personal details
  * Marks
  * Grade

---

###  Update Student

* Modify:

  * Name (Personal Info)
  * Age (Personal Info)
  * Marks (Academic Info)
* Grade updates automatically based on marks

---

###  Grade Calculation Logic

| Marks Range  | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 75 – 89      | A     |
| 60 – 74      | B     |
| 50 – 59      | C     |
| Below 50     | F     |

---

##  Tech Stack

*  Python
* CLI (Command Line Interface)

---

##  Project Structure

```
studentrecord/
│
├── main.py        # Main application file
├── README.md      # Documentation
```

---

##  Installation

### 1 Clone the Repository

```
git clone https://github.com/nagavardhan888/studentrecord.git
cd studentrecord
```

---

### 2️ Requirements

* Python 3.x installed

Check version:

```
python --version
```

---

##  Running the Application

```
python main.py
```

---

##  Sample Output

```
===== Student Record System =====
1. Add Student
2. Search Student
3. Update Student
4. View All Students
5. Exit
```

---

##  Use Cases

* Academic mini-project
* Learning Python fundamentals
* Understanding CRUD operations
* Practicing data handling

---

##  Future Enhancements

*  GUI using Tkinter
*  Database integration (SQLite / MongoDB)
*  Export student reports (PDF)
*  Web-based version (React + Node.js)

---

## 🙌 Acknowledgements

Developed as a **learning and academic project** to understand core programming concepts.

---

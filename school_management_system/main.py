import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        class TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        subject TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        status TEXT,
        date TEXT
    )''')
    conn.commit()

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    cls = input("Enter class: ")
    cursor.execute("INSERT INTO students (name, age, class) VALUES (?, ?, ?)", (name, age, cls))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_teacher():
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")
    cursor.execute("INSERT INTO teachers (name, subject) VALUES (?, ?)", (name, subject))
    conn.commit()
    print("Teacher added successfully!")

def view_teachers():
    cursor.execute("SELECT * FROM teachers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def mark_attendance():
    student_id = int(input("Enter student ID: "))
    status = input("Enter status (Present/Absent): ")
    date = input("Enter date (YYYY-MM-DD): ")
    cursor.execute("INSERT INTO attendance (student_id, status, date) VALUES (?, ?, ?)",
                   (student_id, status, date))
    conn.commit()
    print("Attendance marked!")

def view_attendance():
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def menu():
    while True:
        print("\n--- School Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Teacher")
        print("4. View Teachers")
        print("5. Mark Attendance")
        print("6. View Attendance")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            add_teacher()
        elif choice == '4':
            view_teachers()
        elif choice == '5':
            mark_attendance()
        elif choice == '6':
            view_attendance()
        elif choice == '7':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    create_tables()
    menu()

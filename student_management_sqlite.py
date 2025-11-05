
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade REAL,
    major TEXT
)
""")

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    grade = float(input("Enter grade: "))
    major = input("Enter major: ")
    cursor.execute("INSERT INTO students (name, age, grade, major) VALUES (?, ?, ?, ?)",
                   (name, age, grade, major))
    conn.commit()
    print("✅ Student added successfully!\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    print("\n=== Student List ===")
    for r in result:
        print(r)
    print()

def update_student():
    sid = input("Enter student ID to update: ")
    new_grade = float(input("Enter new grade: "))
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, sid))
    conn.commit()
    print("✅ Student updated!\n")

def delete_student():
    sid = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
    conn.commit()
    print("🗑️ Student deleted!\n")

def search_student():
    sid = input("Enter student ID to search: ")
    cursor.execute("SELECT * FROM students WHERE id = ?", (sid,))
    result = cursor.fetchall()
    print("\n=== Search Result ===")
    for r in result:
        print(r)
    print()

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")

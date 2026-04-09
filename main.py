import sqlite3

class StudentDB:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                grade TEXT
            )
        """)
        self.conn.commit()
        
    def add_student(self,name,age,grade):
        
        self.cursor.execute("""
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
    """, (name, age, grade))
        self.conn.commit()
        print("student added to database")
        
    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        rows= self.cursor.fetchall()
        
        for row in rows:
            print(row)
            
    def update_student(self,student_id, name, age, grade):
        self.cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, grade = ?
        WHERE id = ?
    """, (name, age, grade, student_id))
        self.conn.commit()
        print("Student updated")
        
    def delete_student(self,student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
        print("Student is deleted")
        
        
    def menu(self):
        while True:
            print("\n1. Add a student")
            print("2. View student")
            print("3. Update a student")
            print("4. Delete a student")
            print("5. Exit")
        
            choice = input("Enter a number:")
        
            if choice =="1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                grade = input("Enter grade: ")
                self.add_student(name, age, grade)
            
            elif choice == "2":
                self.view_students()
            
            elif choice == "3":
                student_id = int(input("Enter student ID: "))
                name = input("Enter new name: ")
                age = int(input("Enter new age: "))
                grade = input("Enter new grade: ")
                self.update_student(student_id, name, age, grade)
            
            elif choice == "4":
                student_id = int(input("Enter student ID: "))
                self.delete_student(student_id)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")
                
db=StudentDB()
#db.update_student(1,"bushi",20,"B-")
#db.view_students()
db.menu()
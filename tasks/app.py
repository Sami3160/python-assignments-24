import tkinter as tk
from tkinter import ttk
import sqlite3

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.attendance_vars = []

        self.create_database()
        self.create_student_table()
        self.create_finish_button()

    def create_database(self):
        self.conn = sqlite3.connect('attendance.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                enroll TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                present INTEGER,
                FOREIGN KEY (student_id) REFERENCES students (id)
            )
        ''')
        self.conn.commit()

    def fetch_students(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def create_student_table(self):
        frame = tk.Frame(self.root)
        frame.pack()

        self.tree = ttk.Treeview(frame, columns=("Name", "Enroll"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Enroll", text="Enroll")

        students = self.fetch_students()
        for student in students:
            self.tree.insert("", "end", values=(student[0], student[1]))

        self.tree.pack(side=tk.LEFT)

        checkbox_frame = tk.Frame(frame)
        checkbox_frame.pack(side=tk.RIGHT)

        for student in students:
            var = tk.BooleanVar()
            self.attendance_vars.append((student[0], var))
            cb = tk.Checkbutton(checkbox_frame, variable=var)
            cb.pack(anchor='w')

    def create_finish_button(self):
        self.finish_button = tk.Button(self.root, text="Finish", command=self.finish)
        self.finish_button.pack()

    def finish(self): 
        self.students = self.fetch_students()
        # present_students = [student for student, var in zip(self.students, self.attendance_vars) if var.get()]
        # absent_students = [student for student, var in zip(self.students, self.attendance_vars) if not var.get()]
        
        
        for student_id, var in self.attendance_vars:
            self.cursor.execute('''
                INSERT INTO attendance (student_id, present)
                VALUES (?, ?)
            ''', (student_id, int(var.get())))
            print(student_id, int(var.get()))
        
        self.conn.commit()
        self.show_results()

    def show_results(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Attendance Results")

        present_label = tk.Label(result_window, text="Present Students")
        present_label.pack()

        present_tree = ttk.Treeview(result_window, columns=("Name", "Enroll"), show="headings")
        present_tree.heading("Name", text="Name")
        present_tree.heading("Enroll", text="Enroll")

        self.cursor.execute('''
            SELECT students.name, students.enroll FROM students
            JOIN attendance ON students.enroll = attendance.student_id
            WHERE attendance.present = 1
        ''')
        self.cursor.execute('''
            SELECT student_id, id FROM attendance
            WHERE present = '1'
        ''')
        
        present_students = self.cursor.fetchall()
        print(present_students)
        for student in present_students:
            present_tree.insert("", "end", values=(student[0], student[1]))

        present_tree.pack()

        absent_label = tk.Label(result_window, text="Absent Students")
        absent_label.pack()

        absent_tree = ttk.Treeview(result_window, columns=("Name", "Enroll"), show="headings")
        absent_tree.heading("Name", text="Name")
        absent_tree.heading("Enroll", text="Enroll")

        self.cursor.execute('''
            SELECT students.name, students.enroll FROM students
            JOIN attendance ON students.enroll = attendance.student_id
            WHERE attendance.present = 0
        ''')
        self.cursor.execute('''
            SELECT student_id, id FROM attendance
            WHERE present = '0'
        ''')
        absent_students = self.cursor.fetchall()
        print(absent_students)
        for student in absent_students:
            print(student)  # Add this line to debug
            absent_tree.insert("", "end", values=(student[0], student[1]))

        absent_tree.pack()

root = tk.Tk()
app = AttendanceApp(root)
root.mainloop()
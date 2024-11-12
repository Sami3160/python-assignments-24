# import tkinter as tk
# from tkinter import ttk

# class AttendanceApp:
#     def __init__(self, root, students):
#         self.root = root
#         self.students = students
#         self.attendance_vars = []

#         self.create_student_table()
#         self.create_finish_button()

#     def create_student_table(self):
#         frame = tk.Frame(self.root)
#         frame.pack()

#         self.tree = ttk.Treeview(frame, columns=("Name", "Enroll"), show="headings")
#         self.tree.heading("Name", text="Name")
#         self.tree.heading("Enroll", text="Enroll")

#         for student in self.students:
#             self.tree.insert("", "end", values=(student["name"], student["enroll"]))

#         self.tree.pack(side=tk.LEFT)

#         checkbox_frame = tk.Frame(frame)
#         checkbox_frame.pack(side=tk.RIGHT)

#         for student in self.students:
#             var = tk.BooleanVar()
#             self.attendance_vars.append(var)
#             cb = tk.Checkbutton(checkbox_frame, variable=var)
#             cb.pack(anchor='w')

#     def create_finish_button(self):
#         self.finish_button = tk.Button(self.root, text="Finish", command=self.finish)
#         self.finish_button.pack()

#     def finish(self):
#         present_students = [student for student, var in zip(self.students, self.attendance_vars) if var.get()]
#         absent_students = [student for student, var in zip(self.students, self.attendance_vars) if not var.get()]
#         self.show_results(present_students, absent_students)
#         print("Present students:", present_students)
#         print("Absent students:", absent_students)
#     def show_results(self, present_students, absent_students):
#         result_window = tk.Toplevel(self.root)
#         result_window.title("Attendance Results")

#         present_label = tk.Label(result_window, text="Present Students")
#         present_label.pack()

#         present_tree = ttk.Treeview(result_window, columns=("Name", "Enroll"), show="headings")
#         present_tree.heading("Name", text="Name")
#         present_tree.heading("Enroll", text="Enroll")

#         for student in present_students:
#             present_tree.insert("", "end", values=(student["name"], student["enroll"]))

#         present_tree.pack()

#         absent_label = tk.Label(result_window, text="Absent Students")
#         absent_label.pack()

#         absent_tree = ttk.Treeview(result_window, columns=("Name", "Enroll"), show="headings")
#         absent_tree.heading("Name", text="Name")
#         absent_tree.heading("Enroll", text="Enroll")

#         for student in absent_students:
#             absent_tree.insert("", "end", values=(student["name"], student["enroll"]))

#         absent_tree.pack()

# root = tk.Tk()
# students = [
# {"name": "Aarav Patil", "enroll": "001"},
# {"name": "Vivaan Deshmukh", "enroll": "002"},
# {"name": "Aditya Joshi", "enroll": "003"},
# {"name": "Vihaan Kulkarni", "enroll": "004"},
# {"name": "Arjun Shinde", "enroll": "005"},
# {"name": "Kiara Kharat", "enroll": "018"},
# {"name": "Rudra Rane", "enroll": "027"},
# {"name": "Kabir Naik", "enroll": "028"},
# {"name": "Omkar More", "enroll": "029"},
# ]
# app = AttendanceApp(root, students)
# root.mainloop()





import sqlite3

conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

students = [
    {"name": "Aarav Patil", "enroll": "1"},
    {"name": "Vivaan Deshmukh", "enroll": "2"},
    {"name": "Aditya Joshi", "enroll": "3"},
    {"name": "Vihaan Kulkarni", "enroll": "4"},
    {"name": "Arjun Shinde", "enroll": "5"},
    {"name": "Sai Pawar", "enroll": "6"},
    {"name": "Ayaan Rane", "enroll": "7"},
    {"name": "Krishna Jadhav", "enroll": "8"},
    {"name": "Ishaan Naik", "enroll": "9"},
    {"name": "Atharva More", "enroll": "10"},
]
cursor.execute('delete from attendance')
cursor.execute('delete from students')
cursor.execute('create table if not exists students (name text, enroll text)')
for student in students:
    cursor.execute('''
        INSERT INTO students (name, enroll)
        VALUES (?, ?)
     ''', (student["name"], student["enroll"]))

conn.commit()
conn.close()
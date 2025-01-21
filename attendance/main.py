import tkinter as tk
from tkinter import ttk,messagebox
import pandas as pd
import os
from datetime import datetime

CSV_FILE = "students.csv"

def login():
    if username_entry.get() == "sami" and password_entry.get() == "1234":
        login_window.destroy()
        show_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

def show_main_window():
    global main_window
    main_window = tk.Tk()
    main_window.title("Attendance Tracker")
    tk.Button(main_window, text="Register a student", width=20, command=register_student,bg="#4CAF50", fg="white", ).grid(row=0, column=1, pady=10)
    tk.Button(main_window, text="Mark Attendance", width=20, command=mark_attendance,bg="#2196F3", fg="white", ).grid(row=1, column=0, pady=10)
    tk.Button(main_window, text="Remove a student", width=20, command=remove_student,bg="#f44336", fg="white", ).grid(row=1, column=2, pady=10)
    tk.Button(main_window, text="Display", width=20, command=show_attendance,bg="#FF9800", fg="white", ).grid(row=2, column=1, pady=10)
    main_window.mainloop()
def show_attendance():
    attendance_window = tk.Toplevel()
    attendance_window.title("Attendance Records")
    attendance_window.geometry("800x600")
    attendance_window.configure(bg="#f0f0f0")
    present_frame = tk.Frame(attendance_window, bg="#d4edda")
    present_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    absent_frame = tk.Frame(attendance_window, bg="#f8d7da")
    absent_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    present_label = tk.Label(present_frame, text="Present Students")
    present_label.pack(pady=10)
    absent_label = tk.Label(absent_frame, text="Absent Students")
    absent_label.pack(pady=10)
    present_tree = ttk.Treeview(present_frame, columns=("Roll Number", "Name"), show="headings")
    present_tree.heading("Roll Number", text="Roll Number")
    present_tree.heading("Name", text="Name")
    present_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    absent_tree = ttk.Treeview(absent_frame, columns=("Roll Number", "Name"), show="headings")
    absent_tree.heading("Roll Number", text="Roll Number")
    absent_tree.heading("Name", text="Name")
    absent_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    try:
        df = pd.read_csv('students.csv')
        for _, row in df.iterrows():
            roll_number = row['UID']
            name = row['Student Name']
            status = row[2]
            if status.lower() == 'p':
                present_tree.insert("", tk.END, values=(roll_number, name))
            elif status.lower() == 'a':
                absent_tree.insert("", tk.END, values=(roll_number, name))
    except FileNotFoundError:
        messagebox.showerror("Error", "The attendance.csv file was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def register_student():
    register_window = tk.Toplevel(main_window)
    register_window.title("Register a Student")
    tk.Label(register_window, text="Student Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    name_entry = tk.Entry(register_window )
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(register_window, text="UID:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

    uid_entry = tk.Entry(register_window,  )
    uid_entry.grid(row=1, column=1, padx=10, pady=10)

    def save_student():
        name = name_entry.get()
        uid = uid_entry.get()
        if name and uid:
            if os.path.exists(CSV_FILE):
                df = pd.read_csv(CSV_FILE, dtype={'Student Name': str, 'UID': str})
            else:
                df = pd.DataFrame(columns=['Student Name', 'UID'], dtype=str)

            if uid in df['UID'].values:
                messagebox.showerror("Error", "UID already exists")
            else:
                new_student = pd.DataFrame({'Student Name': [name], 'UID': [uid]}, dtype=str)
                df = pd.concat([df, new_student], ignore_index=True)
                df.to_csv(CSV_FILE, index=False)
                messagebox.showinfo("Success", "Student Registered Successfully")
                register_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in both fields")

    save_button = tk.Button(register_window, text="Save", bg="#4CAF50", fg="white",  width=15,command=save_student)
    save_button.grid(row=2, column=1, pady=20)
def mark_attendance():
    attendance_window = tk.Toplevel(main_window)
    attendance_window.title("Mark Attendance")

    if os.path.exists(CSV_FILE):
        global df
        df = pd.read_csv(CSV_FILE, dtype={'Student Name': str, 'UID': str})
    else:
        messagebox.showerror("Error", "No student records found.")
        attendance_window.destroy()
        return
    if df.empty:
        messagebox.showerror("Error", "No student records found.")
        attendance_window.destroy()
        return
    current_date = datetime.now().strftime("%Y-%m-%d")
    if current_date not in df.columns:
        df[current_date] = ""  
    tk.Label(attendance_window, text="Student").grid(row=0, column=0, padx=10)
    tk.Label(attendance_window, text="Present").grid(row=0, column=1)
    tk.Label(attendance_window, text="Absent").grid(row=0, column=2)
    attendance_vars = []
    for index, row in df.iterrows():
        tk.Label(attendance_window, text=row['Student Name'],padx=10).grid(row=index + 1, column=0)

        var = tk.StringVar(value=row[current_date] if row[current_date] else None)
        attendance_vars.append(var)

        tk.Radiobutton(attendance_window, text="", variable=var, value="P").grid(row=index + 1, column=1)
        tk.Radiobutton(attendance_window, text="", variable=var, value="A").grid(row=index + 1, column=2)

        var.set(row[current_date])

    def save_attendance():
        for index, var in enumerate(attendance_vars):
            df.at[index, current_date] = var.get()  

        df.to_csv(CSV_FILE, index=False)
        messagebox.showinfo("Success", "Attendance Saved Successfully")
        attendance_window.destroy()

    tk.Button(attendance_window, text="Save",  command=save_attendance).grid(row=len(df) + 1, column=0, columnspan=3, pady=10)

def remove_student():
    remove_window = tk.Toplevel(main_window)
    remove_window.title("Remove Student")

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE, dtype={'Student Name': str, 'UID': str})
    else:
        messagebox.showerror("Error", "No student records found.")
        remove_window.destroy()
        return

    if df.empty:
        messagebox.showerror("Error", "No student records found.")
        remove_window.destroy()
        return

    for index, row in df.iterrows():
        tk.Label(remove_window, text=row['Student Name']).grid(row=index, column=0)
        tk.Button(remove_window, text="Remove",
                  command=lambda index=index: remove_student_from_list(index)).grid(row=index, column=1)

    def remove_student_from_list(index):
        df.drop(index=index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(CSV_FILE, index=False)
        messagebox.showinfo("Success", "Student Removed Successfully")
        remove_window.destroy()
        remove_student()

    remove_window.mainloop()

login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(login_window,  )
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_window, show="*", )
password_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(login_window, text="Login", bg="#4CAF50", fg="white", command=login).grid(row=2, columnspan=2, pady=10)
login_window.mainloop()

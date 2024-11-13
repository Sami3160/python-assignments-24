import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance System")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Student Attendance System", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Class Entry
        class_label = tk.Label(self.root, text="Class:", font=("Helvetica", 14), bg="#f0f0f0")
        class_label.pack(pady=5)
        self.class_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.class_entry.pack(pady=5)

        # Date Entry
        date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):", font=("Helvetica", 14), bg="#f0f0f0")
        date_label.pack(pady=5)
        self.date_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.date_entry.pack(pady=5)

        # Start Attendance Button
        start_button = tk.Button(self.root, text="Start Attendance", font=("Helvetica", 14), command=self.start_attendance)
        start_button.pack(pady=20)

        # Roll Number Entry
        roll_label = tk.Label(self.root, text="Roll Number:", font=("Helvetica", 14), bg="#f0f0f0")
        roll_label.pack(pady=5)
        self.roll_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.roll_entry.pack(pady=5)
        self.roll_entry.config(state=tk.DISABLED)

        # Submit Roll Number Button
        submit_button = tk.Button(self.root, text="Submit Roll Number", font=("Helvetica", 14), command=self.submit_roll_number)
        submit_button.pack(pady=20)
        submit_button.config(state=tk.DISABLED)

        # Attendance List
        self.attendance_listbox = tk.Listbox(self.root, font=("Helvetica", 12), width=80, height=10)
        self.attendance_listbox.pack(pady=10)

        self.submit_button = submit_button

    def start_attendance(self):
        student_class = self.class_entry.get()
        date = self.date_entry.get()

        if not student_class or not date:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date format. Use YYYY-MM-DD")
            return

        self.class_entry.config(state=tk.DISABLED)
        self.date_entry.config(state=tk.DISABLED)
        self.roll_entry.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.NORMAL)

    def submit_roll_number(self):
        roll_number = self.roll_entry.get()

        if not roll_number:
            messagebox.showwarning("Input Error", "Please enter a roll number")
            return

        # Here you would typically look up the student's name based on the roll number
        # For simplicity, we'll just use a placeholder name
        student_name = f"Student {roll_number}"

        attendance_record = f"Class: {self.class_entry.get()} - Date: {self.date_entry.get()} - Roll Number: {roll_number} - Name: {student_name} - Status: Present"
        self.attendance_listbox.insert(tk.END, attendance_record)

        self.roll_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

def sum_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("Result", f"The sum is: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

root = tk.Tk()
root.title("Sum of Two Numbers")

label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

sum_button = tk.Button(root, text="Sum", command=sum_numbers)
sum_button.pack()

root.mainloop()
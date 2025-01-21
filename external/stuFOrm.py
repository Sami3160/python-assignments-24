import tkinter as tk
from tkinter import messagebox

def show_welcome_window():
    # Hide the login window
    root.withdraw()

    # Create a new window for the welcome screen
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome")

    tk.Label(welcome_window, text="Welcome to the Student Management System!").pack(pady=20)
    tk.Button(welcome_window, text="Logout", command=lambda: logout(welcome_window)).pack(pady=10)

def logout(welcome_window):
    # Close the welcome window
    welcome_window.destroy()
    # Show the login window again
    root.deiconify()

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Simple check for demonstration purposes
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome!")
        show_welcome_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main login window
root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
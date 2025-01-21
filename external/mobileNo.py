import tkinter as tk
import  re
def checkNum():
    mobile=entry.get()
    pattern=r'^\+91[789]\d{9}$'
    if re.match(pattern, mobile):
        result.config(fg="green", text="Its valid")
    else:
        result.config(fg="red", text="Its not valid")        

root=tk.Tk()
root.title("Mobile on validate")
label1=tk.Label(root,text="Enter mobile number")
label1.grid(column=0, row=0, columnspan=3, pady=5)
entry=tk.Entry(root)
entry.grid(column=0, row=1, columnspan=3, pady=5)
button=tk.Button(root, text="Check", command=lambda:checkNum())
button.grid(row=2,column=0, columnspan=3,pady=10)
result=tk.Label(root, text='Result')
result.grid(column=0,row=4)


root.mainloop()
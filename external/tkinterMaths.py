import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("my app")

def handleClick(opr):
    if(opr=="add"):
        res=int(entry1.get())+int(entry2.get())
    elif opr=="sub":
        res=int(entry1.get())-int(entry2.get())
    elif opr=="mul":
        res=int(entry1.get())*int(entry2.get())
    else:
        res=int(entry1.get())/int(entry2.get())
    result.config(text=f"Result is {res}")
    
    

label1=tk.Label(root, text="enter no1 ")
label1.grid(row=0, column=0)
entry1=tk.Entry(root)
entry1.grid(row=0, column=1)
label2=tk.Label(root, text="enter no1 ")
label2.grid(row=1, column=0)
entry2=tk.Entry(root)
entry2.grid(row=1, column=1)
result=tk.Label(root, text="enter no1 ")
result.grid(row=2, column=0, columnspan=2)

add=tk.Button(root,command=lambda:handleClick("add"), text="add")
add.grid(row=3, column=0)

sub=tk.Button(root,command=lambda:handleClick("sub"), text="sub")
sub.grid(row=3, column=1)

mul=tk.Button(root,command=lambda:handleClick("mul"), text="mul")
mul.grid(row=4, column=0)

div=tk.Button(root,command=lambda:handleClick("div"), text="div")
div.grid(row=4, column=1)

root.mainloop()
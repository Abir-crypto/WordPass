import tkinter as tk
import random
import string
from CreateNewPass import *
import Password

def hogamara():
    newWindow(root)


root = tk.Tk()
root.title("WordPass")
root.geometry("600x400")
root.resizable(False, False)


user_input = tk.StringVar()
thePassword = tk.StringVar()


def takeUserInput():
    name = user_input.get()
    password = Password.find_password(name.lower())
    thePassword.set(password)


canvas = tk.Canvas(root, height=600, width=800, bg="#009999")
canvas.pack()

frame1 = tk.Frame(root, bg="#004d4d")
frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

kisherPassword = tk.Entry(frame1, font=("Roboto", 14), textvariable=user_input)
kisherPassword.place(relx=0.05, rely=0.3, relheight=0.1, relwidth=0.5)

btn = tk.Button(frame1, text="Get Password", bg="black", fg="white", font=("Helvetica", 12), command=takeUserInput)
btn.place(relheight=0.1, relwidth=0.35, relx=0.6, rely=0.3)

aiNePassword = tk.Entry(frame1, font=("Roboto", 14), textvariable=thePassword, bg="#00b33c", fg="black")
aiNePassword.place(relx=0.05, rely=0.5, relheight=0.1, relwidth=0.9)

newpass = tk.Button(frame1, text="Create New Password",command=hogamara, bg="black", fg="white")
newpass.place(relx=0.5, rely=0.8, relheight=0.1, relwidth=0.5, anchor='n')

root.mainloop()

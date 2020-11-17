import tkinter as tk
import random
import string
import Password


def newWindow(mainroot):
    subroot = tk.Toplevel(mainroot)
    subroot.title("Create New Password")
    subroot.resizable(False, False)

    user_input = tk.StringVar()
    thePassword = tk.StringVar()

    def takeUserInput():
        name = user_input.get()
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(16))
        print(result_str)
        Password.add_password(name, result_str)
        thePassword.set(result_str)

    canvas = tk.Canvas(subroot, height=600, width=800, bg="#009999")
    canvas.pack()

    frame1 = tk.Frame(subroot, bg="#004d4d")
    frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    kisherPassword = tk.Entry(frame1, font=("Roboto", 20), textvariable=user_input)
    kisherPassword.place(anchor="n", relx=0.5, rely=0.1, relheight=0.1, relwidth=0.8)

    btn = tk.Button(frame1, text="Generate Password", bg="black", fg="white", font=("Helvetica", 18), command=takeUserInput)
    btn.place(relheight=0.1, relwidth=0.4, anchor='n', relx=0.3, rely=0.45)

    aiNePassword = tk.Entry(frame1, font=("Roboto", 20), textvariable=thePassword, bg="#00b33c", fg="black")
    aiNePassword.place(anchor="n", relx=0.5, rely=0.6, relheight=0.1, relwidth=0.8)

    close = tk.Button(frame1, text="Done", bg="black", fg="white", font=("Helvetica", 18), command=subroot.destroy)
    close.place(relheight=0.1, relwidth=0.4, anchor='n', relx=0.3, rely=0.8)

    subroot.mainloop()




from tkinter import *
from tkinter import messagebox
import re

# Main window
root = Tk()
root.title("Main Window")
root.geometry("300x200")

#Def func
def openpasswordchecr():
    def checkpasswordstrn():
        password = password_entry.get()

        if len(password) < 6:
            strength = "Weak: Password too short"
            result_label.config(text=strength, fg="red")
        elif re.search('[0-9]', password) is None:
            strength = "Weak: Add at least one number"
            result_label.config(text=strength, fg="orange")
        elif re.search('[A-Z]', password) is None:
            strength = "Medium: Add at least one uppercase letter"
            result_label.config(text=strength, fg="yellow")
        elif re.search('[@$!%*?&#]', password) is None:
            strength = "Strong: Consider adding special characters"
            result_label.config(text=strength, fg="blue")
        else:
            strength = "Very Strong"
            result_label.config(text=strength, fg="green")

    top = Toplevel(root)
    top.title("Password Strength Checker")
    top.geometry("400x250")

    Label(top, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
    password_entry = Entry(top, width=30, show="*")
    password_entry.pack(pady=5)

    check_button = Button(top, text="Check Strength", command=checkpasswordstrn)
    check_button.pack(pady=10)

    result_label = Label(top, text="", font=("Arial", 12))
    result_label.pack(pady=10)


Label(root, text="Password Strength Checker App", font=("Arial", 14)).pack(pady=20)

open_button = Button(root, text="Open Password Checker", command=openpasswordchecr)
open_button.pack(pady=10)

root.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Main window
rw = Tk()
rw.title("Denomination Calculator")
rw.configure(bg='light grey')
rw.geometry("800x600")

# Adding image
try:
    upload = Image.open("cal2.jpg")
    upload = upload.resize(300, 200)
    image = ImageTk.PhotoImage(upload)
    label = Label(rw, image=image, bg='light green')
    label.place(x=400, y=500)

except Exception as e:
    messagebox.showerror("Error Message", f"No image found {e}")

greet = Label(rw, text="Welcome to the Denomination Calculator", bg='light green')
greet.place(relx=0.5, y=50, anchor=CENTER)

def conf():
    messagebox.showinfo("Confirm", "Do you want to proceed?")
    TopWin()

button1 = Button(rw, text="Press here to start", command=conf, bg='white', fg='black')
button1.place(x=350, y=500)

# Top window
def TopWin():
    top = Toplevel(rw)
    top.title("Denomination Calculator")
    top.configure(bg='light grey')
    top.geometry("600x600")

    label2 = Label(top, text="Enter number here", bg='light grey')
    entry = Entry(top)
    label3 = Label(top, text="Number of notes per category", bg='light grey')

    l1 = Label(top, text="1000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            amount = int(entry.get())
            if amount < 0:
                raise ValueError("Negative numbers are not allowed")

            note1000 = amount // 1000
            amount %= 1000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note1000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error Alert", "No negative numbers, please input a positive number")

    btn = Button(top, text="Solve", command=calculator, bg='white', fg='black')

    label2.place(x=150, y=50)
    entry.place(x=300, y=50)
    btn.place(x=250, y=100)

    l1.place(x=150, y=150)
    t1.place(x=300, y=150)
    l2.place(x=150, y=200)
    t2.place(x=300, y=200)
    l3.place(x=150, y=250)
    t3.place(x=300, y=250)

rw.mainloop()

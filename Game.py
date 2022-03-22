import random
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("GESS THE NUMBER")
n1 = IntVar()
n2 = IntVar()
gess = IntVar()

def button():
    global a
    global rt
    global b1
    if number ==gess.get():
        rt.set("u done " + str(a) + " attempts -- U ARE DONE")
        b1.place_forget()
    elif a>10:
        rt.set("you are out of attempt-go new game")
        b1.place_forget()
    elif number>gess.get():
        rt.set("u done " + str(a) + " attempts --GO higher")
        a+=1

    elif number<gess.get():
        rt.set("u done " + str(a) + " attempts --GO lower")
        a += 1
#re1 = Label(root, textvariable=rt, foreground='green',font="times 17 bold")
#re1.place(x=200, y=270, anchor="center")
def gen():
    global a
    a=1
    global number
    number= random.randint(n1.get(),n2.get())
def new():
    global b1
    b1= Button(root, text="check the number", font=('Algeriean', 16), foreground='black', command=button)
    b1.place(x=200, y=150, anchor="center")

f = ('Algeriean', 16)
l1 = Label(root, text="Start number", font=f, foreground='red')
l1.grid(row=0, column=0)
e1 = Entry(root, textvariable=n1, width=35)
e1.grid(row=0, column=1)

l2 = Label(root, text="End number", font=f, foreground='red')
l2.grid(row=1, column=0)
e2 = Entry(root, textvariable=n2, width=35)
e2.grid(row=1, column=1)

l3 = Label(root, text="Enter your gess", font=f, foreground='blue')
l3.place(x=200, y=100, anchor="center")
e3 = Entry(root, textvariable=gess, width=35)
e3.place(x=200, y=80, anchor="center")

b1 = Button(root, text="check the number", font=('Algeriean', 16), foreground='black', command=button)
b1.place(x=200, y=150, anchor="center")

b2 = Button(root, text="generate number", font=f, foreground='black', command=gen)
b2.place(x=100, y=200, anchor="center")

b3 = Button(root, text="QUIT THE GAME", font=f, foreground='black', command=root.destroy)
b3.place(x=200, y=300, anchor="center")

b4 = Button(root, text="play new game", font=f, foreground='black', command=new)

b4.place(x=300, y=200, anchor="center")

rt = StringVar()
rt.set("u have 10 attempts")
re1 = Label(root, textvariable=rt, foreground='green', font="times 17 bold")
re1.place(x=200, y=250, anchor="center")


root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.geometry("700x700")
root.title("Random Password Generator")

def fn1():
    global entry1
    entry1 = Entry(root, width=10, fg='black', bg='orange')
    entry1.pack(pady=10)

def fn2():
    global entry2
    entry2 = Entry(root, width=10, fg='black', bg='orange')
    entry2.pack(pady=10)

def fn3():
    global entry3
    entry3 = Entry(root, width=10, fg='black', bg='orange')
    entry3.pack(pady=10)

def fn4():
    global entry1, entry2, entry3
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    n1 = float(a)
    n2 = float(b)
    n3 = float(c)
    numbers_label = Label(root, text="")
    numbers_label.pack()
    if n1 == (n2 + n3):
        symbols=['!','@','#','$','*','&','%']
        random_s=[random.choice(symbols)for _ in range(int(n3))]
        random_numbers = [random.randint(0, 9) for _ in range(int(n2))]
        passward=random_s+random_numbers    
        random.shuffle(passward)
        numbers_label.config(text=" ".join(map(str, passward)))

label = Label(root, text="Welcome to Password Generator", font=("Protest Riot", 20))
label.pack(pady=60)

button1 = Button(root, text="Enter the length for password", font=("Times New Roman", 14), bg='yellow', command=fn1)
button1.pack(pady=20)

button2 = Button(root, text="Enter the desired numbers in password", font=("Times New Roman", 14), bg='yellow', command=fn2)
button2.pack(pady=20)

button3 = Button(root, text="Enter the desired symbols in password", font=("Times New Roman", 14), bg='yellow', command=fn3)
button3.pack(pady=20)

button4 = Button(root, text="Generate", font=("Times New Roman", 14), bg='yellow', command=fn4)
button4.pack()

root.mainloop()

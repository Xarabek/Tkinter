from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.config(bg="green")
root.geometry("285x650")

entry = Entry(root, width=40, borderwidth=10, bg="yellow")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_clicked(number):
    current_pos = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, str(current_pos) + str(number))


def button_clear():
    entry.delete(0, END)


def Addition():
    first_number = entry.get()
    global int_of_first_number, X
    X = 'addition'
    int_of_first_number = int(first_number)
    entry.delete(0, END)


def Subtraction():
    first_number = entry.get()
    global int_of_first_number, X
    X = 'subtraction'
    int_of_first_number = int(first_number)
    entry.delete(0, END)


def Multiplication():
    first_number = entry.get()
    global int_of_first_number, X
    X = 'multiplication'
    int_of_first_number = int(first_number)
    entry.delete(0, END)


def Division():
    first_number = entry.get()
    global int_of_first_number, X
    X = 'division'
    int_of_first_number = int(first_number)
    entry.delete(0, END)


def power():
    first_number = entry.get()
    global int_of_first_number, X
    X = 'power'
    int_of_first_number = int(first_number)
    entry.delete(0, END)


# getting the second number and showing result of calculation
def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if X == 'addition':
        entry.insert(0, int_of_first_number + int(second_number))
    elif X == 'subtraction':
        entry.insert(0, int_of_first_number - int(second_number))
    elif X == 'multiplication':
        entry.insert(0, int_of_first_number * int(second_number))
    elif X == 'division':
        entry.insert(0, int_of_first_number / int(second_number))
    elif X == 'power':
        entry.insert(0, int_of_first_number ** int(second_number))


# buttons
button_0 = Button(root, text="0", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(0))
button_1 = Button(root, text="1", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(1))
button_2 = Button(root, text="2", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(2))
button_3 = Button(root, text="3", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(3))
button_4 = Button(root, text="4", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(4))
button_5 = Button(root, text="5", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(5))
button_6 = Button(root, text="6", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(6))
button_7 = Button(root, text="7", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(7))
button_8 = Button(root, text="8", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(8))
button_9 = Button(root, text="9", padx=30, pady=30, bg="black", fg="white", command=lambda: button_clicked(9))

# actions
button_add = Button(root, text="+", padx=30, pady=30, bg="black", fg="white", command=Addition)
button_subtract = Button(root, text="-", padx=31.4, bg="black", fg="white", pady=30, command=Subtraction)
button_multiply = Button(root, text="x", padx=32.4, bg="black", fg="white", pady=30, command=Multiplication)
button_divide = Button(root, text="/", padx=30, bg="black", fg="white", pady=30, command=Division)
button_power = Button(root, text="powering", padx=10.5, bg="black", fg="white", pady=30, command=power)
button_clear = Button(root, text="Clear", bg="black", fg="white", padx=67, pady=30, command=button_clear)
button_equal = Button(root, text="=", bg="black", fg="white", padx=76.5, pady=30, command=button_equal)


button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_power.grid(row=7, column=1)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()

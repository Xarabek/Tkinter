from tkinter import *
import datetime

root = Tk()
root.title("Age Calculator")

label = Label(root, text="enter your date of birth: ")
label.grid(row=0, column=0)

dateentered1 = StringVar()
datefield = Entry(root, width=15, textvariable=dateentered1)
datefield.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

reminder = Label(root, text="the format of the date: DD-MM-YYYY", fg="red")
reminder.grid(row=1, column=2)


def time_lived():
    # get entered date!
    date_entered = datefield.get()
    parsed_date_entered = date_entered.split("-")
    # turning the date into int
    for i in range(0, len(parsed_date_entered)):
        parsed_date_entered[i] = int(parsed_date_entered[i])
    # turning it into "more common" format of date (Days-months-years)
    year, month, day = parsed_date_entered[2], parsed_date_entered[1], parsed_date_entered[0]
    past_date = datetime.date(year=year, month=month, day=day)
    current_date = datetime.datetime.now()
    now_date = current_date.date()
    delta = now_date - past_date
    # calculation "stuff"
    days = delta.days
    seconds = days * 86400
    weeks = days // 7
    years = days // 365

    time_label = Label(root, text="you lived:\n {} seconds,\n {} days,\n {} weeks,\n {} years.".format(seconds, days, weeks, years))
    time_label.grid(row=3, column=0)


submit_button = Button(root, text="submit", command=time_lived)
submit_button.grid(row=0, column=4, padx=5)

root.mainloop()

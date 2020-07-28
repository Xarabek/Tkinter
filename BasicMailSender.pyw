import smtplib
import ssl
from tkinter import *
root = Tk()
root.title("Mail Sender with python :D")
root.geometry("250x210")

# sender info
label_sender_mail = Label(root, text='your mail: ')
label_sender_mail.grid(row=0, column=0, sticky=E)

sender = StringVar()
enter_send_from = Entry(root, width=15, textvariable=sender)
enter_send_from.grid(row=0, column=1)

label_sender_password = StringVar()
enter_sender_pass = Label(root, text='enter password: ')
enter_sender_pass.grid(row=1, column=0, sticky=E)


sender_password = StringVar()
password = Entry(root, width=15, textvariable=sender_password)
password.grid(row=1, column=1)

# reciever data field and label
label_send_to = Label(root, text="email for: ")
label_send_to.grid(row=2, column=0, sticky=E)

receiver = StringVar()
enter_send_to = Entry(root, width=15, textvariable=receiver)
enter_send_to.grid(row=2, column=1)

# subject data field and label
subject_label = Label(root, text="subject: ")
subject_label.grid(row=3, column=0, sticky=E)

subject = StringVar()
subject_field = Entry(root, width=15, textvariable=subject)
subject_field.grid(row=3, column=1)

# text data field and label
text_label = Label(root, text="text: ")
text_label.grid(row=4, column=0, sticky=E)

text_field = Text(root, width=15, height=5)
text_field.grid(row=4, column=1)

# button for sending stuff!


def send_mail():
    sender = enter_send_from.get()
    password_of_sender = password.get()
    reciever_of_mail = enter_send_to.get()
    subject = subject_field.get()
    text = text_field.get("1.0", END)
    print(sender, password_of_sender, reciever_of_mail, subject, text)
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = sender
    receiver_email = reciever_of_mail
    password_later = password_of_sender
    message = """\
    Subject: {}

    {}.""".format(subject, text)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password_later)
        server.sendmail(sender_email, receiver_email, message)

send_button = Button(root, text="Send!", command=send_mail)
send_button.grid(row=5, column=1, padx=5, pady=5)





root.mainloop()
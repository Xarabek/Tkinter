import requests
from bs4 import BeautifulSoup
from tkinter import *
import re

# main window
root = Tk()
root.title("allegro crawler! :D")


def get_product():
    global full
    products = []
    session = requests.session()
    # read from "search bar"
    look = entry.get()
    # clear the results if someone clicks the button again and is looking for different thing
    answer.delete(1.0, END)

    # getting the code from "allegro" and parsing it
    endpoint = "https://allegro.pl/listing?string={}".format(look)
    response = session.get(endpoint)
    soup = BeautifulSoup(response.text, 'lxml')
    prices = soup.findAll("span", {"class": "_9c44d_1zemI"})
    titles = soup.findAll("h2", {"class": "_9c44d_LUA1k"})
    links = soup.findAll("h2", {"class": "_9c44d_LUA1k"})

    for title, price, link in zip(titles, prices, links):
        regex = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
        x = re.findall(regex, str(link))
        filter_object = filter(lambda a: '/oferta/' in a, x)
        for i in list(filter_object):
            x = str(title.text + "\n" + "~~~~ " + price.text + "~~~~ " + "\n" + i + "\n")
            products.append(x)

    return products


def get_me(event=None):
    x = list(get_product())
    for thing in range(len(x)):
        answer.insert(INSERT, x[thing] + '\n')


topframe = Frame(root)
label = Label(topframe, text="what are you looking for: ", fg="green")
label.pack()
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text="search!", command=get_me)
button.pack()

topframe.pack(side=TOP)

bottomframe = Frame(root)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer = Text(bottomframe, width=50, height=20, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()
root.bind('<Return>', get_me)

root.mainloop()

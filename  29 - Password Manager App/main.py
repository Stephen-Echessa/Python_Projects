from tkinter import *
from tkinter import messagebox
import random


#   PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '(', ')', '$', '#', '@', '%', '^', '*']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    total_letters = [random.choice(letters) for n in range(nr_letters)]
    total_symbols = [random.choice(symbols) for n in range(nr_symbols)]
    total_numbers = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = total_letters + total_numbers + total_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(index=0, string=password)


#   SAVE PASSWORD
def add_credentials():
    print(len(password_entry.get()))
    if password_entry.get() != "" and website_entry.get() != "":
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: \n"
                                                                          f"Email: {email_entry.get()} \n"
                                                                          f"Password: {password_entry.get()}\n"
                                                                          f"Is it okay to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")


window = Tk()
window.title("Password Manager")
window.config(pady=30, padx=20)

canvas = Canvas(width=400, height=150)
my_image = PhotoImage(file="Transparent-Black_Small.png")
canvas.create_image(200, 75, image=my_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=58)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=58)
email_entry.insert(0, string="stevechesa@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=40)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=49, command=add_credentials)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

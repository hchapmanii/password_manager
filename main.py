from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

HEIGHT = 200
WIDTH = 200
FONT = ("Courier", 12, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Alternate solution without List Comprehension but through For Loops
    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    nr_letter = [choice(letters) for lts in range(randint(8, 10))]
    nr_symbol = [choice(symbols) for s in range(randint(2, 4))]
    nr_number = [choice(numbers) for n in range(randint(2, 4))]

    password_generated = nr_letter + nr_symbol + nr_number
    shuffle(password_generated)
    password = "".join(password_generated)

    # Alternate solution without .Join() but through For Loops
    # password = ""
    # for char in password_generated:
    #     password += char

    # print(f"Your password is: {password}")

    gen_pass = StringVar()
    gen_pass.set(password)
    password_entry.config(textvariable=gen_pass)

    # Alternate solution without StringVar()
    # password_entry.insert(0, password)

    pyperclip.copy(gen_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Get Entry Text inputted from User
    web_text = website_entry.get()
    email_text = email_user_entry.get()
    password_text = password_entry.get()
    print(len(web_text))
    print(len(password_text))

    if email_text == "":
        messagebox.showinfo(title="Website Missing", message="Please enter website.")
    elif email_text == "":
        messagebox.showinfo(title="Email Missing", message="Please enter email.")
    elif password_text == "":
        messagebox.showinfo(title="Password Missing", message="Please enter password.")
    else:
        is_ok = messagebox.askokcancel(title="Confirm Information", message=f"These are the details entered: \nWebsite:"
                                                                            f"{web_text} \n Email: {email_text} "
                                                                            f"\nPassword: {password_text} "
                                                                            f"\nPlease Confirm by 'OK'.")
        if is_ok:
            # Add data to the data,txt file
            f = open("data.txt", "a")
            f.write(f"\n{web_text} | {email_text} | {password_text}")
            f.close()

            # Clear the Entry fields and insert example info
            website_entry.delete(0, END)
            email_user_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
            email_user_entry.insert(0, "xxxxxxx@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=HEIGHT, width=WIDTH)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=lock_img)
canvas.grid(column=1, row=0, columnspan=2)

# BUTTONS --------------------------------------------------------------------#

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# FIELDS ---------------------------------------------------------------------#
website_entry = Entry(width=42)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_entry = Entry(width=42)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "xxxxxxx@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# LABELS-----------------------------------------------------------------------#

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Dialogs and Popups ----------------------------------------------------------#


window.mainloop()

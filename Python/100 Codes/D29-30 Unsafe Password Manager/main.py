import tkinter as tk
import tkinter.messagebox as msg
import random as r
import json

disclaimer = msg.askquestion(
    title=f'Disclaimer',
    message=f"For your information, every password you enter here is stored as plain text in a .txt file saved in this app's directory."
    f"\nYOU should assume full responsibility for the safety of your data."
    f"\n\nDo you wish to proceed?"
    )
if disclaimer == 'no':
    exit()

font = ('DM Mono', 10, 'normal')
password_length = 25
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_characters = ['!', '@', '#', '$', '%', '^', '^', '&', '*', '-', '_', '+', '=', ',', '<', '>', '.', ':', ';', '/', '\\', '~', '?']
special_characters_brackets = ['(', ')', '[', ']', '{', '}', '<', '>']
special_characters_quotes = ['"', "'", '`']


# ---------- generate password ---------- #
def password_generator():  # opens a menu to select which characters to use
    try:
        x = button_generate_password.winfo_rootx()
        y = button_generate_password.winfo_rooty()
        popup.tk_popup(x, y, 0)
    finally:
        popup.grab_release()


def generate_password(*args): # generates a random password from chosen characters
    password = ''
    characters = []
    for i in range(len(args)):
        characters.extend(args[i])
    password = ''.join([r.choice(characters) for i in range(password_length)])
    input_password.delete(0, 'end')
    input_password.insert(0, password)


def generate_alpha(): generate_password(alphabet)
def generate_digits(): generate_password(alphabet, digits)
def generate_special(): generate_password(alphabet, digits, special_characters)
def generate_special_brackets(): generate_password(alphabet, digits, special_characters, special_characters_brackets)
def generate_all(): generate_password(alphabet, digits, special_characters, special_characters_brackets, special_characters_quotes)


# ---------- save password ---------- #
def save_password():
    URL = input_URL.get().strip()
    username = input_username.get().strip()
    password = input_password.get().strip()

    for i in URL, username, password:  # check if any entry is missing
        if i == '':
            msg.showinfo(title='Field missing', message='Please fill in all the fields.')
            return

    entry = {
        URL: {
            'username': username,
            'password': password
        }
    }

    confirm_save = msg.askokcancel(title=f'Confirm entry add', message=f'The details entered are:\nURL:\t\t{URL}\nUsername/email:\t{username}\nPassword:\t{password}\n\nSave?')
    if confirm_save:  # clear entries
        try:
            with open('data.json', 'r') as file: # read data if there's any
                data = json.load(file)
        except FileNotFoundError:  # if file doesn't exist
            open('data.json', 'x')
            data = {}
        except json.JSONDecodeError:  # if file is empty
            data = {}
        finally:  # clear input fields
            with open('data.json', 'w') as file:  # store to file while keeping old data
                data.update(entry)
                json.dump(data, file, indent=4)
            input_URL.delete(0, 'end')
            input_username.delete(0, 'end')
            input_password.delete(0, 'end')


# ---------- read passwords ---------- #
def entry_search():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        open('data.json', 'x')
    except json.JSONDecodeError:  # if file is empty
        msg.showinfo(title='No Entries', message=f'There are no entries yet')
    else:
        URL = input_URL.get().strip().lower()
        if entries := [key for key in data if URL in key.lower()]:  # find all matching entries
            for i in range(len(entries)):
                entry = entries[i]
                msg.showinfo(title=f'Entry Lookup ({i+1}/{len(entries)} found)', message=f'The details saved are:\nURL:\t\t{entry}\nUsername/email:\t{data[entry]['username']}\nPassword:\t{data[entry]['password']}')
        else:
            msg.showinfo(title=f'Entry Lookup', message=f'Entry not found\nMaybe a typo?')

# ---------- UI setup ---------- #
window = tk.Tk()
window.config(padx=10, pady=5)
window.title("(NOT) Safe Keeper")

# app logo
logo = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_png = tk.PhotoImage(file='logo.png')
logo.create_image(100, 100, image=logo_png)
logo.grid(column=0, row=0, rowspan=20)

# text labels
label_URL = tk.Label(text='URL:', font=font)
label_username = tk.Label(text='Username/email:', font=font)
label_password = tk.Label(text='Password:', font=font)
label_URL.grid(column=1, row=0)
label_username.grid(column=1, row=1)
label_password.grid(column=1, row=2)

# input entries
input_URL = tk.Entry(font=font, width=31)
input_username = tk.Entry(font=font, width=35)
input_password = tk.Entry(font=font, width=31)
input_URL.grid(column=2, row=0)
input_username.grid(column=2, row=1, columnspan=2)
input_password.grid(column=2, row=2)

# buttons
button_search_data = tk.Button(text='🔍', font=font, command=entry_search)
button_generate_password = tk.Button(text='✨', font=font, command=password_generator)
button_submit = tk.Button(text='Save', font=font, command=save_password, width=35)
button_search_data.grid(column=3, row=0)
button_generate_password.grid(column=3, row=2)
button_submit.grid(column=2, row=3, columnspan=2)

# password generator menu
popup = tk.Menu(window, tearoff=0)
popup.add_command(label="Alphabet only", command=generate_alpha)
popup.add_command(label="Alphabet + digits", command=generate_digits)
popup.add_command(label="Alphabet + digits + special characters", command=generate_special)
popup.add_command(label="Alphabet + digits + special characters + brackets", command=generate_special_brackets)
popup.add_command(label="Alphabet + digits + special characters + brackets + quotes", command=generate_all)


window.mainloop()

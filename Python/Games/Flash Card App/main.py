import tkinter as tk
import random as r
import pandas as p
import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"


# ===== Back alley =====
rolled = {}
try:
    to_learn = p.read_csv('data/unknown_words.csv').to_dict(orient='records')
except FileNotFoundError:
    # open('data/unknown_words.csv', 'x')
    to_learn = p.read_csv('data/french_words.csv').to_dict(orient='records')
except pandas.errors.EmptyDataError:
    to_learn = {}  # it means you've learned all the words


def card_turn():
    if len(to_learn) == 0: return
    background.itemconfig(flashcard, image=img_flashcard_back)
    for i in button_no, button_turn, button_yes:
        i.config(background='#91c2af', activebackground='#80b19e')
    background.itemconfig(title, text='English')
    background.itemconfig(word, text=rolled['English'])


def roll():
    # choose a new word from the list of not known words
    if len(to_learn) == 0:
        background.itemconfig(title, text='Congratulations!')
        background.itemconfig(word, text="You learned all the words!", font=('DM Mono', 32, 'bold'))
        background.create_text(400, 308, text='(delete data\\unknown_words.csv to reset)', font=('DM Mono', 20, 'bold'))
        window.mainloop()
        return
    global rolled
    rolled = r.choice(to_learn)
    background.itemconfig(flashcard, image=img_flashcard_front)
    for i in button_no, button_turn, button_yes:
        i.config(background='#ffffff', activebackground='#eeeeee')
    background.itemconfig(title, text='French')
    background.itemconfig(word, text=rolled['French'])


def know():
    # update the list of words left to learn
    global to_learn
    if len(to_learn) == 0: return
    to_learn.remove(rolled)
    p.DataFrame(to_learn).to_csv('data/unknown_words.csv', index=False)
    roll()



# ===== UI =====
window = tk.Tk()
window.config(padx=22, pady=11, background=BACKGROUND_COLOR)
window.minsize(height=526, width=835)
window.maxsize(height=546, width=835)
window.title('One of the least efficient ways to learn')

# assets
img_flashcard_front = tk.PhotoImage(file='images/card_front.png')
img_flashcard_back = tk.PhotoImage(file='images/card_back.png')
img_check = tk.PhotoImage(file='images/right.png')
img_x = tk.PhotoImage(file='images/wrong.png')

# flashcard
background = tk.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
flashcard = background.create_image(400, 263, image=img_flashcard_front)
title = background.create_text(400, 175, text='title', font=('DM Mono', 32, 'italic'))
word = background.create_text(400, 263, text='word', font=('DM Mono', 64, 'bold'))
background.grid(column=0, row=0, rowspan=6, columnspan=3)

# buttons
button_no = tk.Button(text='❎', font=('DM Mono', 60, 'bold'), command=roll, highlightthickness=0, border=0, background='#ffffff')
button_turn = tk.Button(text='💫', font=('DM Mono', 60, 'bold'), command=card_turn, highlightthickness=0, border=0, background='#ffffff')
button_yes = tk.Button(text='✅', font=('DM Mono', 60, 'bold'), command=know, highlightthickness=0, border=0, background='#ffffff')
button_no.grid(column=0, row=5)
button_turn.grid(column=1, row=5)
button_yes.grid(column=2, row=5)

if len(to_learn) == 0:
    background.itemconfig(title, text='Congratulations!')
    background.itemconfig(word, text="You learned all the words!", font=('DM Mono', 32, 'bold'))
roll()

window.mainloop()
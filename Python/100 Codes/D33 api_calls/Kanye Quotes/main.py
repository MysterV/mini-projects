from tkinter import *
import requests

def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    quote = response.json()['quote']
    print(quote)
    quote = "You basically can say anything to someone on an email or text as long as you put LOL at the end."
    font_size = max(4, int(30-0.06*len(quote)))
    canvas.itemconfig(quote_text, text=quote, font=('Arial', font_size, 'bold'))



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, border=0)
kanye_button.grid(row=1, column=0)



window.mainloop()
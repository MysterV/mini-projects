import tkinter as tk
import time

app = tk.Tk()
app.title('Unit converter')
app.minsize(width=220, height=80)
app.config(padx=10, pady=10)


def km_to_mile():
    km = float(textbox.get())
    mile = round(km / 1.60934, 4)
    output.config(text=f'{mile} miles')


def mile_to_km():
    miles = float(textbox.get())
    km = round(miles * 1.60934, 4)
    output.config(text=f'{km} km')


textbox = tk.Entry()
textbox.grid(column=0, row=0)

output = tk.Label(text='0', font=('Arial', 14, 'bold'))
output.grid(column=1, row=0)

button1 = tk.Button(text='km to mile', font=('Arial', 14, 'normal'), command=km_to_mile)
button1.grid(column=0, row=1)

button2 = tk.Button(text='mile to km', font=('Arial', 14, 'normal'), command=mile_to_km)
button2.grid(column=1, row=1)


app.mainloop()

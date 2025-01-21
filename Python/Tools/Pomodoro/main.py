import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "DM Mono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ----- TIMER MECHANISM ----- #
time_remaining = 0
focus = True
session = 0
paused = False
reset = False
timer_running = 'timer_countdown'


def timer_reset():
    global time_remaining, session, focus, reset
    timer.itemconfig(timer_text, text='00:00', font=(FONT_NAME, 35, 'bold'))
    window.after_cancel(timer_running)
    time_remaining = 0
    session = 0
    pause = False
    button_start.config(text='Start')
    label.config(text='Timer')


def timer_skip():
    global time_remaining, paused
    window.after_cancel(timer_running)
    time_remaining = 0
    paused = False
    timer_countdown()


def timer_start():
    global time_remaining, focus, session, paused
    session += 1
    # pause
    if time_remaining > 0 and not paused:
        paused = True
        window.after_cancel(timer_running)
        button_start.config(text='Start')
        return
    # unpause
    elif time_remaining > 0 and paused:
        paused = False
    # long break
    elif session >= 8:
        session = 0
        time_remaining = LONG_BREAK_MIN * 60
        label.config(text=f'Long Break')
    # short break
    elif session % 2 == 0:
        time_remaining = SHORT_BREAK_MIN * 60
        label.config(text=f'Break {session//2}/4')
    # work
    else:
        time_remaining = WORK_MIN * 60
        label.config(text=f'Work {session//2+1}/4')

    button_start.config(text='Stop')
    timer_countdown()


def timer_countdown():
    global time_remaining, timer, focus, timer_running
    timer.itemconfig(
        timer_text,
        text=f'{str(time_remaining//60).zfill(2)}:{str(time_remaining%60).zfill(2)}',
        font=(FONT_NAME, 35, 'bold'))

    if time_remaining > 0:
        time_remaining -= 1
        timer_running = window.after(1000, timer_countdown)
    else:
        timer.itemconfig(timer_text, text="Time's up!", font=(FONT_NAME, 24, 'bold'))


# ----- UI ----- #


window = tk.Tk()
window.config(padx=15, pady=10, bg=YELLOW)
window.title('Pomodoro')

label = tk.Label(text='Timer', font=(FONT_NAME, 25, 'bold'), bg=YELLOW, fg=PINK)
label.grid(column=2, row=1)

timer = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_img = tk.PhotoImage(file='tomato.png')
timer.create_image(100, 112, image=timer_img)
timer_text = timer.create_text(100, 135, text='00:00', fill='#ffffff', font=(FONT_NAME, 35, 'bold'))
timer.grid(column=2, row=2)

button_start = tk.Button(text='Start', bg=GREEN, font=(FONT_NAME, 15, 'bold'), command=timer_start)
button_start.grid(column=1, row=3)

button_skip = tk.Button(text='Skip', bg=GREEN, font=(FONT_NAME, 15, 'bold'), command=timer_skip)
button_skip.grid(column=2, row=3)

button_reset = tk.Button(text='Reset', bg=RED, font=(FONT_NAME, 15, 'bold'), command=timer_reset)
button_reset.grid(column=3, row=3)

window.mainloop()
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"

fg = GREEN
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    window.after_cancel(timer)
    tick_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1
    print(reps)

    if reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        if reps % 2 == 0:
            tick_label.config(text=TICK)
        else:
            tick_label.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

timer_label = Label(text="Timer", fg=fg, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=208, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 112, image=tomato_img)
timer_text = canvas.create_text(104, 125, fill="white", text="00:00", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(fg=fg, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
tick_label.grid(column=1, row=3)

window.mainloop()

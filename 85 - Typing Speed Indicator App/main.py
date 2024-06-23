import math
import random
from tkinter import *

words = ['change', 'food', 'magma', 'canon', 'event', 'shine', 'press', 'eren',
         'move', 'unconditionally', 'brixton', 'mikasa', 'lean', 'mixed', 'swang',
         'consume', 'consumption', 'closure', 'drop', 'ride', 'colossal', 'sheesh',
         'swang', 'glock', 'uzi', 'verse', 'across', 'stick', 'breeze', 'listing', 
         'molly', 'sponge', 'bob', 'fillings', 'iron', 'copper', 'brown', 'white',
         'purp', 'yellow']

class Window(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Typing Speed Indicator App')
        self.geometry('500x500')
        self.sv = StringVar()
        self.minutes = 1
        self.frame = Frame(self)
        self.frame.grid(row=0, column=0)
        self.display_words()
        
    def display_words(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.canvas = Canvas(self.frame, width=200, height=100, bg="khaki")
        self.timer_text = self.canvas.create_text(100, 50, fill='white', text='00:00', font='Courier 18 bold')
        self.canvas.grid(row=0, column=0)

        random.shuffle(words)

        self.joined_words = (' '.join(words))

        self.all_words = Label(self.frame, text=self.joined_words, font='Arial 10 bold', wraplength=450)
        self.all_words.grid(row=1, column=0, padx=5, pady=5)
        self.sv.trace('w', callback=self.show_color_change)

        self.start = Button(self.frame, text='Start', bg='lightblue', padx=5, pady=5, fg='white', 
                        command=self.start_timer, font='Courier 15 bold')
        self.start.grid(row=2, column=0, padx=5, pady=5)


    def start_timer(self):
        self.start.destroy()
        self.count_down(self.minutes * 60)

        self.word_input_box = Entry(self.frame,font='Arial 14', textvariable=self.sv)
        self.word_input_box.delete(0, END)
        self.word_input_box.grid(row=2, column=0, padx=5, pady=5)

    def show_color_change(self, *args):
        word_input = self.sv.get()
        if word_input in self.joined_words:
            self.all_words.config(fg='green')
        else:
            self.all_words.config(fg='red')

    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec = int(count % 60)
        if count_sec in range(0, 10):
            count_sec = f"0{int(count_sec)}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.after(1000, self.count_down, count - 1)
        else:
            typed_words = self.word_input_box.get()
            typed_list = typed_words.split(' ')
            score = 0
            for i in range(0, len(typed_list)):
                if typed_list[i] == words[i]:
                    score += 1

            self.word_input_box.config(state='readonly')
            self.results = Label(self.frame, text=f"You have a speed of {score} words per minute", fg='grey',
            font='Arial 15 bold').grid(row=3, column=0, padx=5, pady=5)

            self.restart = Button(self.frame,text='Restart', font='Courier 15', bg='blue', fg='white',
                    command=self.display_words).grid(row=4, column=0, padx=5, pady=5)


if __name__ == '__main__':
    app = Window()
    app.mainloop()
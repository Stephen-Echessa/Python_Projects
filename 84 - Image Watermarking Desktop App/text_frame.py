from tkinter import *
import tkinter
from PIL import ImageFont
from PIL import ImageDraw


class TextFrame(Frame):
    def __init__(self, window, resize_img):
        super().__init__()
        self.window = window
        self.resize_img = resize_img
        self.text_sv = StringVar()
        self.size_sv = IntVar()
        self.color_sv = StringVar()
        self.watermark = Label(self)
        
        Label(self, text='Text Properties', font='Courier 22 bold').grid(row=0)
        Label(self, text='Text', font='Arial 12 bold').grid(row=1, padx=5, pady=5)
        self.text_sv.trace('w', callback=self.display_watermark) 
        text_input = Entry(self, textvariable=self.text_sv,)
        text_input.insert(END, 'Enter any Text')
        text_input.grid(row=2,pady=5, padx=10)    
            
        Label(self, text='Size',font='Arial 12 bold').grid(row=3, padx=5, pady=5)
        self.size_sv.trace('w', callback=self.display_watermark) 
        size_input = Entry(self, textvariable=self.size_sv)
        size_input.delete(0, END)
        size_input.insert(END, 20)
        size_input.grid(row=4,pady=5, padx=10)  
              
        Label(self, text='Color', font='Arial 12 bold').grid(row=5)
        self.color_sv.trace('w', callback=self.display_watermark) 
        color_input = Entry(self, textvariable=self.color_sv)
        color_input.insert(END, 'black')
        color_input.grid(row=6,pady=5, padx=10)        
        
        def submit_text_watermark():
            text = text_input.get()
            color = color_input.get()
            try:
                size = int(size_input.get())
                if size > 100:
                    size = 100
                elif size <= 0:
                    size = 20
                width, height = self.resize_img.size
                draw = ImageDraw.Draw(self.resize_img)
                font = ImageFont.truetype('arial.ttf', size)
                draw.text((width / 20, height / 20), text=text, 
                          font=font, fill=color)
                self.resize_img.show() 
                self.resize_img.save('images/text_watermark.jpg')
                window.destroy()
                print('Text has been added as watermark') 
            except ValueError:
                tkinter.messagebox.showinfo(title='Text Properties', message='Invalid input.')
        
        
        submit_button = Button(self, text='Add Text Watermark',
                               command=submit_text_watermark)
        submit_button.grid(row=7,pady=5, padx=10)
    
    
    def display_watermark(self, *args):
        text_value = self.text_sv.get()
        color_value = self.color_sv.get()
        try:
            size_value = self.size_sv.get()
            if size_value > 100:
                size_value = 100
            elif size_value == '':
                size_value = 0
            self.watermark.config(text=text_value, font=f'Arial {size_value}',
                                  fg=color_value)
            self.watermark.grid(row=8, padx=10, pady=10)
        except TclError:
            pass 
from email import message
from tkinter import *
import tkinter
from PIL import ImageTk


class LogoFrame(Frame):
    def __init__(self, window, logo_img, resize_img):
        super().__init__()
        self.window = window
        self.logo_img = logo_img
        self.resize_img = resize_img
        self.width_sv = IntVar()
        self.height_sv = IntVar()
        self.watermark = Label(self)
        
        Label(self, text='Logo Properties', font='Courier 22 bold').grid(row=0)
        Label(self, text='Width', font='Arial 12 bold').grid(row=1, padx=5, pady=5)
        self.width_sv.trace('w', callback=self.display_watermark) 
        width_input = Entry(self, textvariable=self.width_sv,)
        width_input.delete(0, END)
        width_input.insert(END, 20)
        width_input.grid(row=2,pady=5, padx=10)    
            
        Label(self, text='Height',font='Arial 12 bold').grid(row=3, padx=5, pady=5)
        self.height_sv.trace('w', callback=self.display_watermark) 
        height_input = Entry(self, textvariable=self.height_sv)
        height_input.delete(0, END)
        height_input.insert(END, 20)
        height_input.grid(row=4,pady=5, padx=10) 
        
        def submit_text_watermark():
            try:
                width = int(width_input.get())
                height = int(height_input.get())
                if width > 300:
                    width = 300
                elif width <= 0:
                    width = 20
                if height> 300:
                    height = 300
                elif height <= 0:
                    height = 20
                resize_logo = self.logo_img.resize((int(width), int(height)))

                self.resize_img.paste(resize_logo.convert('RGBA'), (5, 5),
                                      resize_logo.convert('RGBA'))
                self.resize_img.show()
                self.resize_img.save('images/logo_watermark.jpg')
                self.window.destroy()
                print('Logo has been added as watermark') 
            except ValueError:
                tkinter.messagebox.showinfo(title='Logo Properties', message='Invalid input.')
        
      
        submit_button = Button(self, text='Add Logo Watermark',
                               command=submit_text_watermark)
        submit_button.grid(row=5,pady=5, padx=10)
    
    def display_watermark(self, *args):
        global show_logo
        try:
            width_value = self.width_sv.get()
            height_value = self.height_sv.get()
            if width_value > 300:
                width_value = 300
            elif width_value == '':
                width_value = 20
            if height_value > 300:
                height_value = 300
            elif height_value == '':
                height_value = 20
                
            resize_logo = self.logo_img.resize((int(width_value), int(height_value)))
            show_logo = ImageTk.PhotoImage(image=resize_logo)

            canvas = Canvas(self, width=600, height=450)
            canvas.create_image(300, 225, image=show_logo, anchor='center')
            canvas.grid(row=6)
        except TclError:
            pass
        except ValueError:
            pass
              
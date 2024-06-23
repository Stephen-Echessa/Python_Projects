from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

from text_frame import TextFrame
from logo_frame import LogoFrame


# Create window
class MainWindow(Tk):
    def __init__(self):
        super().__init__()        
        self.title(' Image Watermarker ')
        self.geometry('1080x900')

        close_button = Button(text='Close App', command=self.close_app)
        close_button.grid(row=0, column=0, pady=5, padx=5)
        image_button = Button(text='Upload Image', command=self.upload_image)
        image_button.grid(row=0, column=1, pady=5, padx=5)


    # Close application
    def close_app(self):
        print('Window closed')
        self.destroy()
                 
    
    # Call TextFrame class when Add Text button is clicked 
    def add_text(self):
        global text_prop_frame
        try:
            if logo_prop_frame:
                logo_prop_frame.destroy()
        except NameError:
            pass
            
        print('Adding Text')
        add_text_button.config(state='disabled')
        text_prop_frame = TextFrame(self, resize_img)
        text_prop_frame.grid(row=1, column=5, rowspan=2, padx=5)
        
        
    # Select png file to add as watermark for image
    def add_logo(self):
        global logo_prop_frame
        add_text_button.config(state='active')
        try:
            text_prop_frame.destroy()
        except NameError:
            pass
        print('Adding Logo')
        f_types = [('Png Files', '*.png')]
        
        try:
            filename = filedialog.askopenfilename(filetypes=f_types)
            logo_img = Image.open(filename)
            logo_prop_frame = LogoFrame(self, logo_img, resize_img)
            logo_prop_frame.grid(row=1, column=5, rowspan=2, padx=5)
        except AttributeError:
            pass
     
        
    def remove_watermark(self):
            add_text_button.config(state='active')
            try:
                text_prop_frame.destroy()
                logo_prop_frame.destroy()
            except NameError:
                pass 


    # Upload image function
    def upload_image(self):
        global resize_img, show_img, add_text_button
        f_types = [('Jpg Files', '*.jpg')]

        try:    
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            resize_img = img.resize((720, 540))
            show_img = ImageTk.PhotoImage(image=resize_img)

            frame = Frame(self, width=300, height=300)
            frame.grid(row=1, column=0, columnspan=5, padx=5)
            img_label = Label(frame, image=show_img)
            img_label.grid(pady=5, padx=5)

            add_logo_button = Button(text='Add Logo', command=self.add_logo)
            add_logo_button.grid(row=0, column=2, pady=5, padx=5)

            add_text_button = Button(text='Add Text', command=self.add_text)
            add_text_button.grid(row=0, column=3, pady=5, padx=5)

            remove_watermark_button = Button(text='Remove Watermark', command=self.remove_watermark)
            remove_watermark_button.grid(row=0, column=4, pady=5, padx=5)
        except AttributeError:
            pass
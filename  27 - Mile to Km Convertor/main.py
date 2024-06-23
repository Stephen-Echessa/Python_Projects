import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=150, width=300)
window.config(padx=20, pady=10)

my_entry = tkinter.Entry(width=5, borderwidth=1)
my_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 15))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

km_num_label = tkinter.Label(text=0, font=("Arial", 15))
km_num_label.grid(column=1, row=1)
km_num_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="Km", font=("Arial", 15))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)


def mile_to_km():
    km_num_label["text"] = round(float(my_entry.get()) * 1.609, 2)


my_button = tkinter.Button(text="Calculate", command=mile_to_km)
my_button.grid(column=1, row=2)

window.mainloop()

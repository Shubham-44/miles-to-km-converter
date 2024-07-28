from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    to_km = round(1.609 * miles, 2)
    km_result_label.config(text=to_km)


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(height=200, width=300)
window.config(padx=20, pady=20)

miles_input = Entry(width=10, font=("Arial", 20))
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 24))
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=("Arial", 24))
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 24))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", font=("Arial", 20), command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()

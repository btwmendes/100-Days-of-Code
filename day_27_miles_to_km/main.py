from tkinter import *
FONT = ("Arial", 24)

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    answer_label.config(text=km)


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#Labels
# Miles label
miles_label = Label(text="Miles", font=FONT)
# my_label.config(text="New Text")
miles_label.grid(column=2, row=0)
miles_label.config(padx=50, pady=50)

# is equal to label
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)
equal_label.config(padx=0, pady=0)

# km label
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=0, pady=0)

# answer label
answer_label = Label(text="0", font=FONT)
answer_label.grid(column=1, row=1)
answer_label.config(padx=0, pady=0)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


#Entry
input = Entry(width=10)
# print(input.get())
input.grid(column=1, row=0)






window.mainloop()
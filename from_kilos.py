from tkinter import *

# Create an empty Tkinter window
window=Tk()

# Name the window
window.title("Kg to Grams, Pounds, Ounces")

# Get user value from input box and multiply by 1000 to get kilograms
def kilos_to_grams():
    grams= float(e1_value.get()) * 1000
    t1.insert(END,grams)

# Get user value from input box and multiply by 2.20462 to get pounds
def kilos_to_pounds():
    pounds= float(e1_value.get()) * 2.20462
    t2.insert(END,pounds)

# Get user value from input box and multiply by 35.274 to get ounces
def kilos_to_ounces():
    ounces= float(e1_value.get()) * 35.274
    t3.insert(END,ounces)


# Create a special StringVar object
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0, column=2)

# Create a Label widget with "Kg" as label
e2=Label(window,text="Kg")
e2.grid(row=0,column=1)

# Create a button widget
# The functions are called when the button is pushed

b1=Button(window, text= "Convert", command=lambda: [kilos_to_grams(), kilos_to_pounds(), kilos_to_ounces()])
b1.grid(row=0, column=4,rowspan=3)

# Create three empty text boxes, t1, t2, and t3

t1=Text(window, height=1, width=15 )
t1.grid(row=1, column =1)

t2=Text(window, height=1, width=15)
t2.grid(row=1, column =2)

t3=Text(window, height=1, width=15)
t3.grid(row=1, column =3)


# This makes sure to keep the main window open
window.mainloop()
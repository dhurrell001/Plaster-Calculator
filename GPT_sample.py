from tkinter import *
from calculator_functions import *
import sqlite3
from tkinter import ttk

conn = sqlite3.connect(
    'C:\\Users\\dhurr\\Documents\\Python Plastering calculator Git\\Plaster-Calculator\\plasters.db')

# Your existing functions and code

# Create a function to switch to the shopping list page


def switch_to_shopping_list_page():
    calculation_frame.pack_forget()
    sms_frame.pack_forget()
    shopping_list_frame.pack()

# Create a function to switch to the calculation page


def switch_to_calculation_page():
    sms_frame.pack_forget()
    shopping_list_frame.pack_forget()
    calculation_frame.pack()

# Create a function to switch to the SMS page


def switch_to_sms_page():
    calculation_frame.pack_forget()
    shopping_list_frame.pack_forget()
    sms_frame.pack()

# ... your existing code ...


# Set up window size and other configurations
window = Tk()
# ... your existing window configurations ...

# Create frames for different pages
calculation_frame = Frame(window)
sms_frame = Frame(window)
shopping_list_frame = Frame(window)

# Add widgets for the calculation page
plaster_label.grid(column=0, row=2, padx=10, pady=10, in_=calculation_frame)
length_label.grid(column=0, row=3, padx=10, pady=10, in_=calculation_frame)
# ... and other widgets ...

# Add widgets for the SMS page
bags_needed_label.grid(column=0, row=2, padx=10, pady=10, in_=sms_frame)
# ... and other widgets ...

# Add widgets for the shopping list page
shopping_list_label = Label(
    shopping_list_frame, text='Shopping List', font=('ariel', 12))
shopping_list_label.pack()

# ... Add your shopping list items here ...

# Add a button to switch to the calculation page
switch_to_calculation_btn = Button(
    window, text="Switch to Calculation Page", command=switch_to_calculation_page)
switch_to_calculation_btn.grid(row=1, column=0, padx=5, pady=5)

# Add a button to switch to the SMS page
switch_to_sms_btn = Button(
    window, text="Switch to SMS Page", command=switch_to_sms_page)
switch_to_sms_btn.grid(row=1, column=1, padx=5, pady=5)

# Add a button to switch to the shopping list page
switch_to_shopping_list_btn = Button(
    window, text="Switch to Shopping List Page", command=switch_to_shopping_list_page)
switch_to_shopping_list_btn.grid(row=1, column=2, padx=5, pady=5)

# Initially show the calculation page
switch_to_calculation_page()

window.mainloop()

# ... your existing code ...

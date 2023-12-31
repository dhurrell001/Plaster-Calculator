from tkinter import *
from calculator_functions import *
import sqlite3
from tkinter import ttk

conn = sqlite3.connect('plasters.db')


def gather_information():

    # gather the data to pass to Calculate function in calculator_function
    # module
    plaster_name = selected_plaster.get()
    plaster_thickness = thickness_input.get()
    length = length_input.get()
    width = width_input.get()

    calculate(plaster_name, plaster_thickness, length,
              width, material_output, bags_needed_output, plaster_description_label)
    
# Function to update the dropdown options based on the selected plaster type
def update_dropdown_options(*args):
    plaster_type = radio_choice.get()  # Get the selected plaster type (1 for internal, 2 for external)
    options = get_dropdownmenu_options(plaster_type)  # Retrieve the dropdown options based on the plaster type
    print(options)
    #selected_plaster.set("Select plaster")  # Reset the selected plaster to the default value

    plaster_input['values'] = options  # Update the dropdown options

def on_selection(event):
    selected_plaster.set(plaster_input.get())

   



# create a table for objects if table does not already exist

conn.execute('''CREATE TABLE IF NOT EXISTS plasters (
                name TEXT,
                bag_size INTEGER,
                cover INTEGER,
                description TEXT,
                usage TEXT
                )''')

#add_plaster()
########################## GUI ####################################

# set up window size
window = Tk()
window.title('PLASTER CALCULATOR')
window.minsize(width=300, height=300)
window.maxsize(width=400, height=400)
window.config(padx=10, pady=10)
window.config(background='lightgrey')

background_image = PhotoImage(
    file="output-onlinepngtools.png")

# Create a label with the background image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create labels labels using the grid() method

plaster_label = Label(text='Plaster Type', background='white smoke',
                      font=('ariel', 12))
length_label = Label(text='length', background='white smoke',
                     font=('ariel', 12), borderwidth=0, relief='flat')
thickness_label = Label(text='Thickness in mm', background='white smoke',
                        font=('ariel', 12))
width_label = Label(text='Width', background='white smoke',
                    font=('ariel', 12))
total_material = Label(text='Total material in KG',
                       background='white smoke', font=('ariel', 12))
material_output = Label(background='white smoke', font=('ariel', 12))

bags_needed_label = Label(text='Bags required : ',
                          background='white smoke', font=('ariel', 12))
bags_needed_output = Label(text='',
                           background='white smoke', font=('ariel', 12))
plaster_description_label = Label(text='',
                                  background='white smoke', font=('ariel', 10), wraplength=200)

# Place labels using Grid

plaster_label.grid(column=0, row=1, padx=10, pady=10)
length_label.grid(column=0, row=2)
width_label.grid(column=0, row=3)
thickness_label.grid(column=0, row=4)
total_material.grid(column=0, row=5, padx=10, pady=10)
material_output.grid(column=1, row=5)
bags_needed_label.grid(column=0, row=6)
bags_needed_output.grid(column=1, row=6)
plaster_description_label.grid(column=0, row=8)


# text boxes

# create radio button to toggle between internal and external plasters in drop dowm menu

radio_choice = IntVar()
radio_choice.set(1)

plaster_choice_internal = Radiobutton(
    window, text='Internal', variable=radio_choice, value=1,command = update_dropdown_options)
plaster_choice_external = Radiobutton(
    window, text='External', variable=radio_choice, value=2,command=update_dropdown_options)

# place radio buttons

plaster_choice_internal.grid(column=0, row=9)
plaster_choice_external.grid(column=1, row=9)

# Create a validation function to check if the input is a float
validate_func = window.register(validate_float_input)


selected_plaster = StringVar()  # variable to hold option selected in dropdown menu
selected_plaster.set("Select plaster")  # Set the default selected plaster

# Add a trace to the selected_plaster variable to call the update_dropdown_options function when it changes
selected_plaster.trace("w", update_dropdown_options)

# Create the Combobox widget
plaster_input = ttk.Combobox(window, textvariable=selected_plaster, state='readonly')
# Bind the on_selection function to the <<ComboboxSelected>> event
plaster_input.bind("<<ComboboxSelected>>", on_selection)
update_dropdown_options()


# validate entry boxes. validation on 'key' stroke. send each keystroke to validate function
length_input = Entry(window, validate="key",
                     validatecommand=(validate_func, '%P'), width=6, background='white smoke')
width_input = Entry(window, validate="key",
                    validatecommand=(validate_func, '%P'), width=6, background='white smoke')
thickness_input = Entry(window, validate="key",
                        validatecommand=(validate_func, '%P'), width=6, background='white smoke')

#  input layout using grid

plaster_input.grid(column=1, row=1, padx=10, pady=10)
length_input.grid(column=1, row=2, padx=10, pady=10)
width_input.grid(column=1, row=3, padx=10, pady=10)
thickness_input.grid(column=1, row=4, padx=10, pady=10)


# button

button = Button(text='CONVERT', command=gather_information)


button.grid(column=1, row=7)

window.mainloop()

conn.close()

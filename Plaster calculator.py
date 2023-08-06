from tkinter import *
from calculator_functions import *
import sqlite3
from tkinter import ttk
from second_frame import SecondFrame

conn = sqlite3.connect(
    'C:\\Users\\dhurr\\Documents\\Python Plastering calculator Git\\Plaster-Calculator\\plasters.db')


def gather_information():

    # gather the data to pass to Calculate function in calculator_function
    # module
    plaster_name = selected_plaster.get()
    plaster_thickness = thickness_slider.get()
    length = length_slider.get()
    width = width_slider.get()

    calculate(plaster_name, plaster_thickness, length,
              width, material_output, bags_needed_output, plaster_description_label, shop_list)


def gather_sms_data():
    # collects the data that will be put into the smas message

    plaster_type = selected_plaster.get()
    # Get the content of the bags_needed_output label using cget. cget gets the current valur of widget
    bags = bags_needed_output.cget("text")

    send_sms(plaster_type, bags)

# Function to update the dropdown options based on the selected plaster type


def update_dropdown_options(*args):
    # Get the selected plaster type (1 for internal, 2 for external)
    plaster_type = radio_choice.get()
    # Retrieve the dropdown options based on the plaster type
    options = get_dropdownmenu_options(plaster_type)

    # selected_plaster.set("Select plaster")  # Reset the selected plaster to the default value

    plaster_input['values'] = options  # Update the dropdown options


def on_selection(event):
    selected_plaster.set(plaster_input.get())

# Create a function to switch to the shopping list page


def switch_to_shopping_list_page():
    calculator_frame.grid_forget()
    second_frame = SecondFrame(window)  # creates second frame object

    second_frame.grid(column=0, row=2, columnspan=5, padx=10, pady=10)
    second_frame.fill_list(shop_list.create_list())


# create a table for objects if table does not already exist
conn.execute('''CREATE TABLE IF NOT EXISTS plasters (
                name TEXT,
                bag_size INTEGER,
                cover INTEGER,
                description TEXT,
                usage TEXT
                )''')

# dd_plaster()
########################## GUI ####################################

# set up window size
window = Tk()
window.title('PLASTER CALCULATOR')
window.config(width=700, height=500)
window.minsize(width=300, height=300)
# window.maxsize(width=400, height=500)
window.config(padx=10, pady=10)
window.config(background='#EEEEEE')

# create frames
calculator_frame = Frame(window)


background_image = PhotoImage(
    file="Plaster-Calculator\plastering.png")
# Create a canvas with the same width as the image and some height
canvas_width = background_image.width()
canvas_height = 140
canvas = Canvas(window, width=canvas_width, height=canvas_height)
canvas.grid(column=0, row=0, columnspan=5, sticky='n', in_=calculator_frame)

# Calculate the coordinates to center the image on the canvas
x = (canvas_width - background_image.width()) // 2
y = 0

# Add the image to the canvas at the calculated coordinates
canvas.create_image(x, y, anchor=NW, image=background_image)
# create frames
# calculator_frame = Frame(window)
# second_frame = SecondFrame(window)  # creates second frame obje
# create a shopping list object to pas to calculate function
shop_list = shopping_list()

# Create a label with the background image
# background_label = Label(window, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create labels labels using the grid() method

plaster_label = Label(text='Plaster Type', background='#EEEEEE',
                      font=('ariel', 12))
length_label = Label(text='length', background='#EEEEEE',
                     font=('ariel', 12), borderwidth=0, relief='flat')
thickness_label = Label(text='Thickness in mm', background='#EEEEEE',
                        font=('ariel', 12))
width_label = Label(text='Width', background='#EEEEEE',
                    font=('ariel', 12))
total_material = Label(text='Total material in KG',
                       background='#EEEEEE', font=('ariel', 12))
material_output = Label(background='#EEEEEE', font=('ariel', 12), width=5)

bags_needed_label = Label(text='Bags required : ',
                          background='#EEEEEE', font=('ariel', 12))
bags_needed_output = Label(background='#EEEEEE', font=('ariel', 12), width=5)
plaster_description_label = Label(text='',
                                  background='#EEEEEE', font=('ariel', 10), wraplength=200)
length_slider = Scale(window, from_=0, to=50,
                      orient=HORIZONTAL, length=200, resolution=0.1)
length_slider.grid(column=1, row=3, columnspan=3,
                   padx=10, pady=10, in_=calculator_frame)
width_slider = Scale(window, from_=0, to=50,
                     orient=HORIZONTAL, length=200, resolution=0.1)
width_slider.grid(column=1, row=4, columnspan=3,
                  padx=10, pady=10, in_=calculator_frame)
thickness_slider = Scale(window, from_=0, to=25,
                         orient=HORIZONTAL, length=200, resolution=0.1)
thickness_slider.grid(column=1, row=5, columnspan=3,
                      padx=10, pady=10, in_=calculator_frame)


# Place labels using Grid

plaster_label.grid(column=0, row=2, padx=10, pady=10, in_=calculator_frame)
length_label.grid(column=0, row=3, padx=10, pady=10, in_=calculator_frame)
width_label.grid(column=0, row=4, in_=calculator_frame)
thickness_label.grid(column=0, row=5, in_=calculator_frame)
total_material.grid(column=0, row=7, in_=calculator_frame)
material_output.grid(column=1, row=7, in_=calculator_frame)
bags_needed_label.grid(column=2, row=7, padx=10, pady=10, in_=calculator_frame)
bags_needed_output.grid(column=3, row=7, in_=calculator_frame)
plaster_description_label.grid(
    column=0, row=9, columnspan=4, in_=calculator_frame)


# text boxes

# create radio button to toggle between internal and external plasters in drop dowm menu

radio_choice = IntVar()
radio_choice.set(1)

plaster_choice_internal = Radiobutton(
    window, text='Internal', variable=radio_choice, value=1, command=update_dropdown_options)
plaster_choice_external = Radiobutton(
    window, text='External', variable=radio_choice, value=2, command=update_dropdown_options)

# place radio buttons

plaster_choice_internal.grid(
    column=0, row=1, columnspan=2, in_=calculator_frame)
plaster_choice_external.grid(
    column=1, row=1, columnspan=2, in_=calculator_frame)

# Create a validation function to check if the input is a float
validate_func = window.register(validate_float_input)


selected_plaster = StringVar()  # variable to hold option selected in dropdown menu
selected_plaster.set("Select plaster")  # Set the default selected plaster

# Add a trace to the selected_plaster variable to call the update_dropdown_options function when it changes
selected_plaster.trace("w", update_dropdown_options)

# Create the Combobox widget
plaster_input = ttk.Combobox(
    window, textvariable=selected_plaster, state='readonly', width=20)
# Bind the on_selection function to the <<ComboboxSelected>> event
plaster_input.bind("<<ComboboxSelected>>", on_selection)
update_dropdown_options()


# validate entry boxes. validation on 'key' stroke. send each keystroke to validate function
# l#ength_input = Entry(window, validate="key",
#                    validatecommand=(validate_func, '%P'), width=6, background='white smoke')
width_input = Entry(window, validate="key",
                    validatecommand=(validate_func, '%P'), width=6, background='white smoke')
thickness_input = Entry(window, validate="key",
                        validatecommand=(validate_func, '%P'), width=6, background='white smoke')

#  input layout using grid

plaster_input.grid(column=1, row=2, columnspan=3,
                   padx=10, pady=10, in_=calculator_frame)
# length_input.grid(column=1, row=2, padx=10, pady=10)
# width_input.grid(column=1, row=3, padx=10, pady=10)
# thickness_input.grid(column=1, row=4, padx=10, pady=10)


# button

button = Button(text='CONVERT', width=15, bg='#068FFF', fg='white smoke',
                command=gather_information)


button.grid(column=0, row=8, columnspan=2,
            padx=10, pady=10, in_=calculator_frame)

sms_button = Button(text='SMS Results', width=15,
                    bg='#068FFF', fg='white smoke', command=gather_sms_data)
sms_button.grid(column=1, row=8, columnspan=2,
                padx=10, pady=10, in_=calculator_frame)

list_button = Button(text='Shopping', width=20,
                     bg='#068FFF', fg='white smoke', command=switch_to_shopping_list_page)
list_button.grid(column=0, row=9, columnspan=2,
                 padx=10, pady=10, in_=calculator_frame)


calculator_frame.grid(column=2, row=2,  padx=10, pady=10)


window.mainloop()

conn.close()

from tkinter import *
import sqlite3

conn = sqlite3.connect('plasters.db')


class Plaster():

    def __init__(self, name, bag_size, cover, description) -> None:
        # cover = kg per mm thickness per metre square

        self.name = name
        self.bag_size = bag_size
        self.cover = cover
        self.description = description

    def material_needed(self, area, thickness):
        return (area * self.cover) * thickness


def add_plaster():

    name = input('Please enter name of plaster : ')
    size = int(input('Please enter weight of bags in KG : '))
    coverage = int(
        input('Please enter cover rate (kg per mm per square metre) : '))
    decsription = input('Please enter a brief description of the product')
    plaster_object = Plaster(name, size, coverage, decsription)

    # load exisitng object to database. Check to make sure object does not already exist as record.
    cursor = conn.cursor()

    # Check if the record already exists before inserting
    cursor.execute('SELECT name FROM plasters WHERE name=?',
                   (plaster_object.name,))
    if cursor.fetchone() is None:
        conn.execute('INSERT INTO plasters VALUES (?, ?, ?,?)',
                     (plaster_object.name, plaster_object.bag_size, plaster_object.cover, plaster_object.description))
        print('New plaster added to database.')
    else:
        print('Plaster already exists in database.')

    # commit changes
    conn.commit()


def get_dropdownmenu_options():
    # select all plaster names from database and store in a list for
    # dropdown menu options
    cursor = conn.cursor()
    options = []
    names = cursor.execute('SELECT name FROM plasters')
    for name in names:
        # Extract the first element(plaster name) from the tuple returned from query
        options.append(name[0])

    return options


def calculate():
    plaster_name = selected_plaster.get()  # get data from input box
    plaster_thickness = thickness_input.get()
    plaster = get_material(plaster_name)

    if plaster:
        area = int(length_input.get()) * int(width_input.get())
        total_needed = plaster.material_needed(area, int(plaster_thickness))
        material_output.config(text=total_needed)

        bags_required = calculate_bags_needed(plaster, total_needed)
        bags_needed_output.config(text=bags_required)

    else:
        print('Plaster not found')


def calculate_bags_needed(plaster_object, total_needed_in_kg):

    return total_needed_in_kg / plaster_object.bag_size


def get_material(material_name):

    cursor = conn.execute(
        'SELECT name, bag_size, cover,description FROM plasters WHERE name=?', (material_name,))
    object = cursor.fetchone()
    if object:
        name, bag_size, cover, description = object
        plaster = Plaster(name, bag_size, cover, description)
        return plaster
    else:
        print('Material not found')


def validate_float_input(text):
    # tries to convert text from entry box into a float. return false to if invalid
    if text == "":
        return True  # Allow empty input (deleting)
    try:
        float(text)
        return True
    except ValueError:
        return False

# create a table for objects if table does not already exist


conn.execute('''CREATE TABLE IF NOT EXISTS plasters (
                name TEXT,
                bag_size INTEGER,
                cover INTEGER,
                description TEXT
                )''')

# add_plaster()
########################## GUI ####################################

# set up window size
window = Tk()
window.title('PLASTER CALCULATOR')
window.minsize(width=300, height=300)
window.maxsize(width=400, height=400)
window.config(padx=10, pady=10)
window.config(background='lightgrey')

background_image = PhotoImage(
    file="Plaster-Calculator\\output-onlinepngtools.png")

# Create a label with the background image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create labels labels using the grid() method

plaster_label = Label(text='Plaster Type', background='white smoke',
                      font=('ariel', 12))
length_label = Label(text='length', background='white smoke',
                     font=('ariel', 12))
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

plaster_label.grid(column=0, row=1, padx=10, pady=10)
length_label.grid(column=0, row=2)
width_label.grid(column=0, row=3)
thickness_label.grid(column=0, row=4)
total_material.grid(column=0, row=5, padx=10, pady=10)
material_output.grid(column=1, row=5)
bags_needed_label.grid(column=0, row=6)
bags_needed_output.grid(column=1, row=6)


# text boxes
# Create a validation function to check if the input is a float
validate_func = window.register(validate_float_input)


selected_plaster = StringVar()
selected_plaster.set("Select plaster")  # Set the default selected plaster

plaster_input = OptionMenu(window, selected_plaster,
                           *get_dropdownmenu_options())

length_input = Entry(window, validate="key",
                     validatecommand=(validate_func, '%P'), width=6, background='white smoke')
width_input = Entry(window, validate="key",
                    validatecommand=(validate_func, '%P'), width=6, background='white smoke')
thickness_input = Entry(window, validate="key",
                        validatecommand=(validate_func, '%P'), width=6, background='white smoke')


plaster_input.grid(column=1, row=1, padx=10, pady=10)
length_input.grid(column=1, row=2, padx=10, pady=10)
width_input.grid(column=1, row=3, padx=10, pady=10)
thickness_input.grid(column=1, row=4, padx=10, pady=10)


# button

button = Button(text='CONVERT', command=calculate)
print(selected_plaster)


button.grid(column=1, row=7)

window.mainloop()

conn.close()

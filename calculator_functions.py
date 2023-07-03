
import sqlite3

conn = sqlite3.connect('plasters.db')


class Plaster():

    def __init__(self, name, bag_size, cover, description, usage) -> None:
        # cover = kg per mm thickness per metre square

        self.name = name
        self.bag_size = bag_size
        self.cover = cover
        self.description = description
        self.usage = usage

    def material_needed(self, area, thickness):
        return (area * self.cover) * thickness


def add_plaster():

    name = input('Please enter name of plaster : ')
    size = int(input('Please enter weight of bags in KG : '))
    coverage = int(
        input('Please enter cover rate (kg per mm per square metre) : '))
    decsription = input('Please enter a brief description of the product')
    usage = input('Please enter if for INTernal or EXTernal :')
    plaster_object = Plaster(name, size, coverage, decsription, usage)

    # load exisitng object to database. Check to make sure object does not already exist as record.
    cursor = conn.cursor()

    # Check if the record already exists before inserting
    cursor.execute('SELECT name FROM plasters WHERE name=?',
                   (plaster_object.name,))
    if cursor.fetchone() is None:       # fetches first row in query results
        conn.execute('INSERT INTO plasters VALUES (?, ?, ?,?,?)',
                     (plaster_object.name, plaster_object.bag_size, plaster_object.cover, plaster_object.description, plaster_object.usage))
        print('New plaster added to database.')
    else:
        print('Plaster already exists in database.')

    # commit changes to data base
    conn.commit()


def get_dropdownmenu_options(plaster_type):

    # select all plaster names from database and store in a list for
    # dropdown menu options

    cursor = conn.cursor()
    options = []
    print(plaster_type)
    if plaster_type == 1:
        names = cursor.execute(
            'SELECT name FROM plasters WHERE usage = "INT"')
        for name in names:
            # Extract the first element(plaster name) from the tuple returned from query
            options.append(name[0])
    else:
        names = cursor.execute(
            'SELECT name FROM plasters WHERE usage = "EXT"')
        for name in names:
            # Extract the first element(plaster name) from the tuple returned from query
            options.append(name[0])

    return options


def calculate(plaster_name, plaster_thickness, length_input, width_input, material_output, bags_needed_output, plaster_description_label):
    plaster = get_material(plaster_name)

    if plaster:
        area = int(length_input) * int(width_input)
        total_needed = plaster.material_needed(area, int(plaster_thickness))
        material_output.config(text=total_needed)

        bags_required = calculate_bags_needed(plaster, total_needed)
        bags_needed_output.config(text=bags_required)
        plaster_description_label.config(text=plaster.description)

    else:
        print('Plaster not found')


def calculate_bags_needed(plaster_object, total_needed_in_kg):
    # calulates how many bag of plaster are needed NOTE: need to use ceiling to round up.

    return total_needed_in_kg / plaster_object.bag_size


def get_material(material_name):

    # get material record fron DB and return created Plaster object

    cursor = conn.execute(
        'SELECT name, bag_size, cover,description FROM plasters WHERE name=?', (material_name,))
    object = cursor.fetchone()
    if object:
        name, bag_size, cover, description, usage = object
        plaster = Plaster(name, bag_size, cover, description, usage)
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

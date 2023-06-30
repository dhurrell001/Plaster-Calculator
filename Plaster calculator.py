from tkinter import *
class Plaster():

    def __init__(self,name,bag_size,cover) -> None:
        #cover = kg per mm thickness per metre square

        self.name = name
        self.bag_size = bag_size
        self.cover = cover

    def material_needed(self,area,thickness):
        return (area * self.cover) * thickness
    
plaster = Plaster('multi',25,1)
cement = Plaster('cement',25,10)
materials_list = [plaster,cement]

def calculate():
    plaster = get_material(materials_list,plaster_input.get())
    area = int(length_input.get())*int(width_input.get())
    
    total_needed = plaster.material_needed(area,10)
    material_output.config(text = total_needed)


def get_material(materials_list,material_name):
    for product in materials_list:
        if material_name == product.name:
            return product
    print('Material not found')
    

#set up window size
window = Tk()
window.title('PLASTER CALCULATOR')
window.minsize(width=400, height=400)
window.config(padx=20 , pady=20)
window.config(background='lightgrey')

background_image = PhotoImage(file="output-onlinepngtools.png")

# Create a label with the background image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#create labels labels using the grid() method

paster_label = Label(text= 'Plaster Type',background='white', font=('ariel',12,'bold'))
length_label = Label(text= 'length',background='white', font=('ariel',12,'bold'))
width_label = Label(text= 'Width',background='white', font=('ariel',12,'bold'))
total_material = Label( text ='Total material in KG',background='white',font=('ariel',12,'bold'))
material_output = Label( background='white',font=('ariel',12,'bold'))

paster_label.grid(column=0,row=1)
length_label.grid(column=0, row=2)
width_label.grid(column=0, row=3)
total_material.grid(column=0, row=4, padx=10, pady=10)
material_output.grid(column=1, row=4)


#text boxes

plaster_input = Entry(background='white',width=6)
length_input = Entry(background='white',width=6)
width_input = Entry(background='white',width=6)
#total_input = Entry(background='white',width=6)

plaster_input.grid(column=1, row=1, padx=10, pady=10)
length_input.grid(column=1, row=2, padx=10, pady=10)
width_input.grid(column=1, row=3, padx=10, pady=10)
#total_input.grid(column=1, row=3)





#button 

button = Button(text='CONVERT', command= calculate)


button.grid(column=1, row=5)

window.mainloop()
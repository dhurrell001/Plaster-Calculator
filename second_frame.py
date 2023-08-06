from tkinter import ttk
import tkinter as tk


class SecondFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create labels, buttons, or other widgets for the second frame
        self.label = ttk.Label(self, text="This is the Second Frame")
        self.title_label = ttk.Label(text='SHOPPING LIST', background='#EEEEEE',
                                     font=('ariel', 12))
        self.label.grid(column=1, row=2, padx=10, pady=10)
        self.title_label.grid(column=0, row=0)

        # Add other widgets and functionality as needed
        # ...
    def fill_list(self, items):

        self.label.config(text=items)

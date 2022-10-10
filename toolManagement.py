#!/usr/bin/python3

import tkinter
from tkinter import ttk


class ToolStrip(tkinter.Frame):

    def __init__(self, t_nr, t_type, t_len, t_rad, max_len, max_rad, speed, pressure):
        super().__init__()

        # variables
        self.t_nr = t_nr
        self.t_type = tkinter.StringVar(self)
        self.t_type.set(t_type)
        self.t_len = tkinter.DoubleVar(self)
        self.t_len.set(t_len)
        self.t_rad = tkinter.DoubleVar(self)
        self.t_rad.set(t_rad)
        self.max_len = tkinter.DoubleVar(self)
        self.max_len.set(max_len)
        self.max_rad = tkinter.DoubleVar(self)
        self.max_rad.set(max_rad)
        self.speed = tkinter.IntVar(self)
        self.speed.set(speed)
        self.pressure = tkinter.IntVar(self)
        self.pressure.set(pressure)

        #styles
        style = ttk.Style()
        #style.configure('GO.TButton', font=('Sans', '12', 'bold'), foreground='green')
        #style.configure('EXIT.TButton', foreground='red')
        #style.configure('OUT.TLabel', width=13, background='white',font=('Sans', '12', 'bold'))  # style of output values
        style.configure('DIM.TEntry', width=7)

        # widgets
        self.nr_label = ttk.Label(self, text=str(self.t_nr))
        sequences = ['FRE', 'VRT', 'ZAV', 'VYS', 'KUL', 'ZFR']
        self.type_entry = tkinter.OptionMenu(self, self.t_type, *sequences)
        self.len_entry = ttk.Entry(self, textvariable=self.t_len, width=7, justify='right', style='DIM.TEntry')
        self.rad_entry = ttk.Entry(self, textvariable=self.t_rad, style='DIM.TEntry')
        self.max_len_entry = ttk.Entry(self, textvariable=self.max_len, style='DIM.TEntry')
        self.max_rad_entry = ttk.Entry(self, textvariable=self.max_rad, style='DIM.TEntry')
        self.speed_entry = ttk.Entry(self, textvariable=self.speed, style='DIM.TEntry')
        self.pressure_entry = ttk.Entry(self, textvariable=self.pressure, style='DIM.TEntry')

        #geometry
        self.nr_label.grid(column=0, row=0)
        self.type_entry.grid(column=1, row=0)
        self.len_entry.grid(column=2, row=0)
        self.rad_entry.grid(column=3, row=0)
        self.max_len_entry.grid(column=4, row=0)
        self.max_rad_entry.grid(column=5, row=0)
        self.speed_entry.grid(column=6, row=0)
        self.pressure_entry.grid(column=7, row=0)


class ToolManag(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(False, False)  # not resizable main window
        self.title('GROB G350 Tool Management')  # name of app

        # init variables, styles, widgets and geometry
        self.create_variables()
        self.create_styles()
        self.create_widgets()
        self.create_geometry()

    def create_variables(self):
        self.tool_list = list()

    def create_styles(self):
        pass

    def create_widgets(self):
        self.strip = ToolStrip(1, 'FRE', 120.3, 7.998, 150, 31.5, 16000, 40)

    def create_geometry(self):
        self.strip.pack()


if __name__ == '__main__':
    app = ToolManag()
    app.mainloop()
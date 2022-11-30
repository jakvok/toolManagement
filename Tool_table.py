#!/usr/bin/python3

import tkinter
from tkinter import ttk
import Tool


class Label_strip(tkinter.Frame):

    def __init__(self):
        super().__init__()
        
        #widgets
        self.t_nr = ttk.Label(self, text='T', justify='center', font=('Sans', '8', 'bold'), width=2)
        self.t_type = ttk.Label(self, text='Tool type', justify='center', width=17)
        self.t_len = ttk.Label(self, text='lenght', justify='center', width=10)
        self.t_rad = ttk.Label(self, text='radius', justify='center', width=10)
        self.max_len = ttk.Label(self, text='max len', justify='center', width=10)
        self.max_rad = ttk.Label(self, text='max rad', justify='center', width=10)
        self.speed = ttk.Label(self, text='max speed', justify='center', width=10)
        self.pressure = ttk.Label(self, text='press', justify='center', width=5)
        self.t_check = ttk.Label(self, text='t-check', justify='center', width=7)
        self.t_sister = ttk.Label(self, text='sisters', justify='center', width=7)
        
        #geometry
        self.t_nr.grid(column=0, row=0, padx=(7, 7))
        self.t_type.grid(column=1, row=0, padx=5)
        self.t_len.grid(column=2, row=0, padx=5)
        self.t_rad.grid(column=3, row=0, padx=5)
        self.max_len.grid(column=4, row=0, padx=5)
        self.max_rad.grid(column=5, row=0, padx=5)
        self.speed.grid(column=6, row=0, padx=5)
        self.pressure.grid(column=7, row=0, padx=5)
        self.t_check.grid(column=8, row=0, padx=5)
        self.t_sister.grid(column=9, row=0, padx=(5, 2))
        
        

class Tool_strip(tkinter.Frame):

    def __init__(self, t_nr, t_type, t_len, t_rad, max_len, max_rad, speed, pressure, t_check, sisters=1):
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
        self.t_check = tkinter.BooleanVar(self)
        self.t_check.set(t_check)
        self.sisters = tkinter.IntVar(self)
        self.sisters.set(sisters)

        #styles
        style = ttk.Style()
        #style.configure('GO.TButton', font=('Sans', '12', 'bold'), foreground='green')
        #style.configure('EXIT.TButton', foreground='red')
        style.configure('Tool.TLabel', width=2,font=('Sans', '8', 'bold'))
        style.configure('Dim.TEntry', width=7, justify='right')

        # widgets
        self.nr_label = ttk.Label(self, text=str(self.t_nr), style='Tool.TLabel')

        sequences = list()
        for i in Tool.Tool_type:
            sequences.append(i.name)
        
        self.type_entry = tkinter.OptionMenu(self,  self.t_type, *sequences)
        self.type_entry.config(width=10)
        self.len_entry = ttk.Entry(self, textvariable=self.t_len, width=10, justify='right', style='Dim.TEntry')
        self.rad_entry = ttk.Entry(self, textvariable=self.t_rad, width=10, justify='right', style='Dim.TEntry')
        self.max_len_entry = ttk.Entry(self, textvariable=self.max_len, width=10, justify='right', style='Dim.TEntry')
        self.max_rad_entry = ttk.Entry(self, textvariable=self.max_rad, width=10, justify='right', style='Dim.TEntry')
        self.speed_entry = ttk.Entry(self, textvariable=self.speed, width=10, justify='right', style='Dim.TEntry')
        self.pressure_entry = ttk.Entry(self, textvariable=self.pressure, width=5, justify='right', style='Dim.TEntry')
        self.tool_check = ttk.Checkbutton(self, variable=self.t_check, width=10)
        self.sisters_entry = ttk.Entry(self, textvariable=self.sisters, width=3, justify='right')

        #geometry
        self.nr_label.grid(column=0, row=0, padx=(17, 7))
        self.type_entry.grid(column=1, row=0)
        self.len_entry.grid(column=2, row=0, padx=5)
        self.rad_entry.grid(column=3, row=0, padx=5)
        self.max_len_entry.grid(column=4, row=0, padx=5)
        self.max_rad_entry.grid(column=5, row=0, padx=5)
        self.speed_entry.grid(column=6, row=0, padx=5)
        self.pressure_entry.grid(column=7, row=0, padx=5)
        self.tool_check.grid(column=8, row=0, padx=(20, 20))
        self.sisters_entry.grid(column=8, row=0, padx=(30, 2))



class Tool_table:
    
    def __init__(self, toollist):
        self.toollist = toollist
        
    def edit(self):
        root = tkinter.Tk()
        root.resizable(False, False)  # not resizable main window
        root.title('GROB G350 Tool list')  # name of app

        def go_back():
            for n in range(len(self.toollist)):
                self.toollist[n].typ = Tool.Tool_type[root.strip[n].t_type.get()]
                self.toollist[n].lenght = root.strip[n].t_len.get()
                self.toollist[n].radius = root.strip[n].t_rad.get()
                self.toollist[n].max_lenght = root.strip[n].max_len.get()
                self.toollist[n].max_rad = root.strip[n].max_rad.get()
                self.toollist[n].max_speed = root.strip[n].speed.get()
                self.toollist[n].pressure = root.strip[n].pressure.get()
                self.toollist[n].tool_check = root.strip[n].t_check.get()
                self.toollist[n].sister = root.strip[n].sisters.get()
            
            root.destroy()
            
        # widgets
        root.button_exit = ttk.Button(root, text='EXIT', command=go_back)
        
        root.strip = list()
        for t in self.toollist:
            root.strip.append(Tool_strip(t.name, t.typ.name, t.lenght, t.radius, t.max_lenght, t.max_rad,  t.max_speed, t.pressure, t.tool_check, t.sister))
        
        # geometry
        Label_strip().grid(column=1, row=0)
        
        for n in range(len(root.strip)):
            root.strip[n].grid(column=1, row=n+1)
            
        root.button_exit.grid(column=1, row=n+2, pady=5)
        
        # 
        
            
        root.mainloop()

        return self.toollist
                
                

if __name__ == '__main__':
    pass
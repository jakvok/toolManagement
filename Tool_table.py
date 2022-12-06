#!/usr/bin/python3

import tkinter
from tkinter import ttk
import Tool


class Tool_table(tkinter.Tk):
    
    def __init__(self, toollist):
        super().__init__()
        self.toollist = toollist 

        self.resizable(False, False)  # not resizable main window
        self.title('GROB G350 Tool list')  # name of app
        
        #styles
        paddings = {'padx': 5, 'pady': 5}
        style = ttk.Style(self)
        style.configure('DIM.TEntry', background='green', justify='right')

        
        
        # Tool variables
        self.t_name = []
        self.t_type = []
        self.t_len = []
        self.t_rad = []
        self.t_max_len = []
        self.t_max_rad = []
        self.t_speed = []
        self.t_pressure = []
        self.t_check = []
        self.t_sister = []
        for t in self.toollist:
            self.t_name.append(t.name)
            self.t_type.append(tkinter.StringVar(self))
            self.t_type[-1].set(t.typ.name)
            self.t_len.append(tkinter.DoubleVar(self))
            self.t_len[-1].set(t.lenght)
            self.t_rad.append(tkinter.DoubleVar(self))
            self.t_rad[-1].set(t.radius)
            self.t_max_len.append(tkinter.DoubleVar(self))
            self.t_max_len[-1].set(t.max_lenght)
            self.t_max_rad.append(tkinter.DoubleVar(self))
            self.t_max_rad[-1].set(t.max_rad)
            self.t_speed.append(tkinter.IntVar(self))
            self.t_speed[-1].set(t.max_speed)
            self.t_pressure.append(tkinter.IntVar(self))
            self.t_pressure[-1].set(t.pressure)
            self.t_check.append(tkinter.BooleanVar(self))
            self.t_check[-1].set(t.tool_check)
            self.t_sister.append(tkinter.IntVar(self))   
            self.t_sister[-1].set(t.sister)
        
        # Labels widgets
        self.label_name = ttk.Label(self, text='T', justify='center', font=('Sans', '8', 'bold'))
        self.label_type = ttk.Label(self, text='Tool type', justify='center')
        self.label_len = ttk.Label(self, text='lenght', justify='center')
        self.label_rad = ttk.Label(self, text='radius', justify='center')
        self.label_max_len = ttk.Label(self, text='max len', justify='center')
        self.label_max_rad = ttk.Label(self, text='max rad', justify='center')
        self.label_speed = ttk.Label(self, text='max speed', justify='center')
        self.label_pressure = ttk.Label(self, text='press', justify='center')
        self.label_check = ttk.Label(self, text='t-check', justify='center')
        self.label_sister = ttk.Label(self, text='sisters', justify='center')

        # Tool widgets
        self.w_name = []
        self.w_type = []
        self.w_len = []
        self.w_rad = []
        self.w_max_len = []
        self.w_max_rad = []
        self.w_speed = []
        self.w_pressure = []
        self.w_check = []
        self.w_sister = []
        sequences = list()
        for i in Tool.Tool_type:
            sequences.append(i.name)
        for n in range(len(self.toollist)):
            self.w_name.append(ttk.Label(self, text=str(self.t_name[n])))
            self.w_type.append(ttk.OptionMenu(self,  self.t_type[n], self.t_type[n].get(), *sequences))
            self.w_type[-1].configure(width=12)
            self.w_len.append(ttk.Entry(self, textvariable=self.t_len[n], style='DIM.TEntry'))
            self.w_len[-1].configure(width=7)
            self.w_len[-1].configure(justify='right')
            self.w_rad.append(ttk.Entry(self, textvariable=self.t_rad[n], style='DIM.TEntry'))
            self.w_rad[-1].configure(width=7)
            self.w_rad[-1].configure(justify='right')
            self.w_max_len.append(ttk.Entry(self, textvariable=self.t_max_len[n], style='DIM.TEntry'))
            self.w_max_len[-1].configure(width=7)
            self.w_max_len[-1].configure(justify='right')
            self.w_max_rad.append(ttk.Entry(self, textvariable=self.t_max_rad[n], style='DIM.TEntry'))
            self.w_max_rad[-1].configure(width=7)
            self.w_max_rad[-1].configure(justify='right')
            self.w_speed.append(ttk.Entry(self, textvariable=self.t_speed[n]))
            self.w_speed[-1].configure(width=7)
            self.w_speed[-1].configure(justify='right')
            self.w_pressure.append(ttk.Entry(self, textvariable=self.t_pressure[n]))
            self.w_pressure[-1].configure(width=5)
            self.w_pressure[-1].configure(justify='right')
            self.w_check.append(tkinter.Checkbutton(self, text='', variable=self.t_check[n]))
            self.w_check[-1].configure(width=6)
            self.w_sister.append(ttk.Entry(self, textvariable=self.t_sister[n]))
            self.w_sister[-1].configure(width=5)
            self.w_sister[-1].configure(justify='right')
        
        # Button widget
        self.button_exit = ttk.Button(self, text='EXIT', command=self.go_back)
        
        # Labels geometry
        self.label_name.grid(column=0, row=0, **paddings)
        self.label_type.grid(column=1, row=0, **paddings)
        self.label_len.grid(column=2, row=0, **paddings)
        self.label_rad.grid(column=3, row=0, **paddings)
        self.label_max_len.grid(column=4, row=0, **paddings)
        self.label_max_rad.grid(column=5, row=0, **paddings)
        self.label_speed.grid(column=6, row=0, **paddings)
        self.label_pressure.grid(column=7, row=0, **paddings)
        self.label_check.grid(column=8, row=0, **paddings)
        self.label_sister.grid(column=9, row=0, **paddings)

        # Tools geometry
        for n in range(len(self.toollist)):
            self.w_name[n].grid(column=0, row=n+1, **paddings)
            self.w_type[n].grid(column=1, row=n+1, **paddings)
            self.w_len[n].grid(column=2, row=n+1, **paddings)
            self.w_rad[n].grid(column=3, row=n+1, **paddings)
            self.w_max_len[n].grid(column=4, row=n+1, **paddings)
            self.w_max_rad[n].grid(column=5, row=n+1, **paddings)
            self.w_speed[n].grid(column=6, row=n+1, **paddings)
            self.w_pressure[n].grid(column=7, row=n+1, **paddings)
            self.w_check[n].grid(column=8, row=n+1, **paddings)
            self.w_sister[n].grid(column=9, row=n+1, **paddings)        

        # Exit button geometry
        self.button_exit.grid(column=4, columnspan=2, row=n+2, **paddings)
            
        self.mainloop()
        

    def go_back(self):
        
        for n in range(len(self.toollist)):
            self.toollist[n].typ = Tool.Tool_type[self.t_type[n].get()]
            self.toollist[n].lenght = self.t_len[n].get()
            self.toollist[n].radius = self.t_rad[n].get()
            self.toollist[n].max_lenght = self.t_max_len[n].get()
            self.toollist[n].max_rad = self.t_max_rad[n].get()
            self.toollist[n].max_speed = self.t_speed[n].get()
            self.toollist[n].pressure = self.t_pressure[n].get()
            self.toollist[n].tool_check = self.t_check[n].get()
            self.toollist[n].sister = self.t_sister[n].get()                

        self.destroy()
    
    

if __name__ == '__main__':
    pass
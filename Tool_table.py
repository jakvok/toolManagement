#!/usr/bin/python3

import tkinter
from tkinter import ttk, messagebox
import Tool


class Tool_table(tkinter.Tk):
    """
    Class represents a tool table of milling machine Grob with Sinumerik 840D control system.
    Tool table shows given list of Tool instances and values of their attributes.
    The values (Tool's attributes) are free to edit.
    The changed values are saved into Tool instances in tool list.
    """
    
    def __init__(self, toollist):
        super().__init__()
        self.toollist = toollist    # list of Tool instances

        self.resizable(False, False)  # not resizable main window
        self.title('GROB G350 Tool list')  # name of app
        
        #styles
        paddings = {'padx': 5, 'pady': 5}
        style = ttk.Style(self)
        style.configure('DIM.TEntry', background='green', justify='right')

        
        # Tool variables
        self.t_names = []        # list of tkinter variables - tool names
        self.t_types = []        # list of tkinter variables - tool types
        self.t_lens = []         # list of tkinter variables - tool lenghts
        self.t_rads = []         # list of tkinter variables - tool radiuses
        self.t_max_lens = []     # list of tkinter variables - tool max. lenghts
        self.t_max_rads = []     # list of tkinter variables - tool max. radiuses
        self.t_speeds = []       # list of tkinter variables - tool max. speed
        self.t_pressures = []    # list of tkinter variables - tool ic pressure
        self.t_checks = []       # list of tkinter variables - tool check
        self.t_sisters = []      # list of tkinter variables - tool sister nr.
        # fill lists by tkinter variables due to tool list values
        for t in self.toollist:
            self.t_names.append(t.name)
            self.t_types.append(tkinter.StringVar(self))
            self.t_types[-1].set(t.typ.name) # set value to the just append list member
            self.t_lens.append(tkinter.DoubleVar(self))
            self.t_lens[-1].set(t.lenght)
            self.t_rads.append(tkinter.DoubleVar(self))
            self.t_rads[-1].set(t.radius)
            self.t_max_lens.append(tkinter.DoubleVar(self))
            self.t_max_lens[-1].set(t.max_lenght)
            self.t_max_rads.append(tkinter.DoubleVar(self))
            self.t_max_rads[-1].set(t.max_rad)
            self.t_speeds.append(tkinter.IntVar(self))
            self.t_speeds[-1].set(t.max_speed)
            self.t_pressures.append(tkinter.IntVar(self))
            self.t_pressures[-1].set(t.pressure)
            self.t_checks.append(tkinter.BooleanVar(self))
            self.t_checks[-1].set(t.tool_check)
            self.t_sisters.append(tkinter.IntVar(self))   
            self.t_sisters[-1].set(t.sister)
        
        # Labels widgets; widgwts fot the first row in table
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

        # commands for number input validation handling
        vcmd_lens = (self.register(self.check_lens), '%P', '%W')
        ivcmd_lens = (self.register(self.bad_lens), '%W')
        vcmd_rads = (self.register(self.check_rads), '%P', '%W')
        ivcmd_rads = (self.register(self.bad_rads), '%W')
        vcmd_speeds = (self.register(self.check_speeds), '%P', '%W')
        ivcmd_speeds = (self.register(self.bad_speeds), '%W')
        vcmd_pressures = (self.register(self.check_pressures), '%P', '%W')
        ivcmd_pressures = (self.register(self.bad_pressures), '%W')
        vcmd_sisters = (self.register(self.check_sisters), '%P', '%W')
        ivcmd_sisters = (self.register(self.bad_sisters), '%W')

        # Tool widgets; widgets to show tool's attributes and their values
        self.w_names = []      # list of widgets - tool names
        self.w_types = []      # list of widgets - tool types
        self.w_lens = []       # list of widgets - tool lenghts
        self.w_rads = []       # list of widgets - tool radiuses
        self.w_max_lens = []   # list of widgets - tool max. lenghts
        self.w_max_rads = []   # list of widgets - tool max. radiuses
        self.w_speeds = []     # list of widgets - tool max. speeds
        self.w_pressures = []  # list of widgets - tool ic pressure
        self.w_checks = []     # list of widgets - tool check
        self.w_sisters = []    # list of widgets - tool sister nr.
        # create sequence list for OptionMenu widget
        sequences = list()
        for i in Tool.Tool_type:
            sequences.append(i.name)
        # create widgets for each tool in tool list
        for n in range(len(self.toollist)):
            self.w_names.append(ttk.Label(self, text=str(self.t_names[n])))
            self.w_types.append(ttk.OptionMenu(self,  self.t_types[n], self.t_types[n].get(), *sequences))
            self.w_types[-1].configure(width=12)
            self.w_lens.append(ttk.Entry(self, textvariable=self.t_lens[n], style='DIM.TEntry'))
            self.w_lens[-1].configure(width=7)
            self.w_lens[-1].configure(justify='right')
            self.w_lens[-1].configure(validate='focusout', validatecommand=vcmd_lens, invalidcommand=ivcmd_lens)
            self.w_rads.append(ttk.Entry(self, textvariable=self.t_rads[n], style='DIM.TEntry'))
            self.w_rads[-1].configure(width=7)
            self.w_rads[-1].configure(justify='right')
            self.w_rads[-1].configure(validate='focusout', validatecommand=vcmd_rads, invalidcommand=ivcmd_rads)
            self.w_max_lens.append(ttk.Entry(self, textvariable=self.t_max_lens[n], style='DIM.TEntry'))
            self.w_max_lens[-1].configure(width=7)
            self.w_max_lens[-1].configure(justify='right')
            self.w_max_lens[-1].configure(validate='focusout', validatecommand=vcmd_lens, invalidcommand=ivcmd_lens)
            self.w_max_rads.append(ttk.Entry(self, textvariable=self.t_max_rads[n], style='DIM.TEntry'))
            self.w_max_rads[-1].configure(width=7)
            self.w_max_rads[-1].configure(justify='right')
            self.w_max_rads[-1].configure(validate='focusout', validatecommand=vcmd_rads, invalidcommand=ivcmd_rads)
            self.w_speeds.append(ttk.Entry(self, textvariable=self.t_speeds[n]))
            self.w_speeds[-1].configure(width=7)
            self.w_speeds[-1].configure(justify='right')
            self.w_speeds[-1].configure(validate='focusout', validatecommand=vcmd_speeds, invalidcommand=ivcmd_speeds)
            self.w_pressures.append(ttk.Entry(self, textvariable=self.t_pressures[n]))
            self.w_pressures[-1].configure(width=5)
            self.w_pressures[-1].configure(justify='right')
            self.w_pressures[-1].configure(validate='focusout', validatecommand=vcmd_pressures, invalidcommand=ivcmd_pressures)
            self.w_checks.append(tkinter.Checkbutton(self, text='', variable=self.t_checks[n]))
            self.w_checks[-1].configure(width=6)
            self.w_sisters.append(ttk.Entry(self, textvariable=self.t_sisters[n]))
            self.w_sisters[-1].configure(width=5)
            self.w_sisters[-1].configure(justify='right')
            self.w_sisters[-1].configure(validate='focusout', validatecommand=vcmd_sisters, invalidcommand=ivcmd_sisters)
        
        # Button widget for exit editing
        self.button_exit = ttk.Button(self, text='EXIT', command=self.go_back)
        
        # Label widgets geometry
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

        # Tool widgets geometry
        for n in range(len(self.toollist)):
            self.w_names[n].grid(column=0, row=n+1, **paddings)
            self.w_types[n].grid(column=1, row=n+1, **paddings)
            self.w_lens[n].grid(column=2, row=n+1, **paddings)
            self.w_rads[n].grid(column=3, row=n+1, **paddings)
            self.w_max_lens[n].grid(column=4, row=n+1, **paddings)
            self.w_max_rads[n].grid(column=5, row=n+1, **paddings)
            self.w_speeds[n].grid(column=6, row=n+1, **paddings)
            self.w_pressures[n].grid(column=7, row=n+1, **paddings)
            self.w_checks[n].grid(column=8, row=n+1, **paddings)
            self.w_sisters[n].grid(column=9, row=n+1, **paddings)        

        # Exit button geometry
        self.button_exit.grid(column=4, columnspan=2, row=len(self.toollist)+2, **paddings)
            
        self.mainloop()
        

    def go_back(self):
        """
        Function saves edited values from tkinter variables into attribute toollist
        and quit editing
        """
        for n in range(len(self.toollist)):
            self.toollist[n].typ = Tool.Tool_type[self.t_types[n].get()]
            self.toollist[n].lenght = self.t_lens[n].get()
            self.toollist[n].radius = self.t_rads[n].get()
            self.toollist[n].max_lenght = self.t_max_lens[n].get()
            self.toollist[n].max_rad = self.t_max_rads[n].get()
            self.toollist[n].max_speed = self.t_speeds[n].get()
            self.toollist[n].pressure = self.t_pressures[n].get()
            self.toollist[n].tool_check = self.t_checks[n].get()
            self.toollist[n].sister = self.t_sisters[n].get()                

        self.quit()
    

    def __value_check(self, value, check_value, widg):
        """
        Function check if entry input is in range and returns True if so.
        If not, returns False and paint value to red
        Parameters
        ----------
        value :
            value get from widget.
        check_value :
            value to check.
        widg :
            current widget.
        Returns
        -------
        bool
            if value is in range 0 to check_value
        """
        try:
            x = float(value)
            # when value out of range, raise exception
            if x < 0 or check_value < x or value == '':
                raise ValueError
            return True
        except ValueError:
            # paints value to red
            self.nametowidget(widg)['foreground'] = 'red'
            return False
        
    
    def __value_out_of_range(self, replace_value, widg):
        """
        Function replace widget content by replace_value and paint it black.
        Parameters
        ----------
        widg :
            widget to replace bad value
        replace_value :
            value to replace
        Returns
        -------
        None.
        """
        # error message
        messagebox.showerror('Value Error', 'Input value out of range!')
        # delete involved string chars from index 0 to the last srting index
        self.nametowidget(widg).delete(0, len(self.nametowidget(widg).get()))
        # insert default value
        self.nametowidget(widg).insert(0, replace_value)
        # set color to black
        self.nametowidget(widg)['foreground'] = 'black'


    def check_lens(self, value, widg):
        """
        function check if entry input is in range and returns True if so.
        If not, returns False and paint value to red
        """
        return self.__value_check(value, Tool.Tool.max_tl, widg)


    def bad_lens(self, widg):
        """
        When entry input is not valid, shows error message box and change entry value to default
        """
        self.__value_out_of_range(Tool.Tool.max_tl, widg)
        

    def check_rads(self, value, widg):
        """
        function check if entry input is in range and returns True if so.
        If not, returns False and paint value to red
        """
        return self.__value_check(value, Tool.Tool.max_tr, widg)


    def bad_rads(self, widg):
        """
        When entry input is not valid, shows error message box and change entry value to default
        """
        self.__value_out_of_range(31.5, widg)
        

    def check_speeds(self, value, widg):
        """
        function check if entry input is in range and returns True if so.
        If not, returns False and paint value to red
        """
        return self.__value_check(value, Tool.Tool.max_ts, widg)


    def bad_speeds(self, widg):
        """
        When entry input is not valid, shows error message box and change entry value to default
        """
        self.__value_out_of_range(Tool.Tool.max_ts, widg)
        

    def check_pressures(self, value, widg):
        """
        function check if entry input is in range and returns True if so.
        If not, returns False and paint value to red
        """
        return self.__value_check(value, Tool.Tool.t_press, widg)


    def bad_pressures(self, widg):
        """
        When entry input is not valid, shows error message box and change entry value to default
        """
        self.__value_out_of_range(Tool.Tool.t_press, widg)
        

    def check_sisters(self, value, widg):
        """
        function try to convert entry input to int and returns True if entry input is in range.
        If not, returns False and paint value to red
        """
        try:
            x = int(value)
            # when value out of range, raise exception
            if x < 1 or Tool.Tool.max_sister_tool_nr < x or value == '':
                raise ValueError
            # delete involved string chars from index 0 to the last srting index
            #self.nametowidget(widg).delete(0, len(self.nametowidget(widg).get()))
            #self.nametowidget(widg).insert(0, x)
            return True
        except ValueError:
            # paints value to red
            self.nametowidget(widg)['foreground'] = 'red'
            return False


    def bad_sisters(self, widg):
        """
        When entry input is not valid, shows error message box and change entry value to default
        """
        self.__value_out_of_range(1, widg)



if __name__ == '__main__':
    pass
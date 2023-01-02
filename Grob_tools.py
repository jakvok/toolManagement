# -*- coding: utf-8 -*-
#!/usr/bin/python3


import Tool
import T_container
import Tool_table
import os


class Grob_tools:
    """
    Class represents a list of tools in Sinumerik 840D CNC control system.
    The instance can found all tools contained in NC program and save them in
    attribute <toollist> as instances of class <Tool>.
    The instance can edit all tool parameters through instance of class <Tool_table>.
    The instance can generate NC program, which set up all found and edited tools
    and needed values in tool turret in CNC machine.
    """
    
    def __init__(self):
        self.toollist = []      # storage of tools
        self._input_file = ''    # NC file from what tools are given
        self._output_file = ''    # NC file where output NC program is postprocessed
        
        
    def load_tools(self, filename):
        """
        Method loads from given NC file all contained tools and save them into list attribute <toollist>
        as instance of clase <Tool>.

        Parameters
        ----------
        filename : string
            path to source NC file.

        Returns
        -------
        None.

        """
        self._input_file = filename
        # setup default output file path
        self._output_file = os.path.join(os.path.split(filename)[0], '.'.join(str(os.path.split(filename)[1]).split('.')[:-1])) + '_tools.MPF'
        
        
        lines = []    # container for input file lines, each list member = one line
        scanned_tools = []    # list of found tools in format of T_container instances
        
        # open input file and fill <lines> by file's lines
        try:
            with open(self._input_file, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    lines.append(line.strip())
        except FileNotFoundError as e:
            print(e)
        
        # go thru <lines> and find every line with toolchanghe 'T... M6'
        tools_pos = []  # list of lines with found toolchanges and it's numbers [line_number, line_content]
        for n in range(len(lines)-1):
            if lines[n].startswith('T') and lines[n+1] == 'M6' and '=' not in lines[n]:
                tools_pos.append([lines[n], n])
        
        # for each found toolchange positions find all available tool parameters from <lines>
        for k in tools_pos:
            m = T_container.T_container(lines, k[1])    # find tool param
            if m.name: scanned_tools.append(m)  # if tool name found, add tool into list
        
        # sort all found tools by name
        scanned_tools.sort(key=lambda x: int(x.name))
        
        # delete duplicit tools
        n = 0
        while 1:
            if n >= len(scanned_tools)-1: break
            if scanned_tools[n].name == scanned_tools[n+1].name:
                # save information about internal cooling
                if scanned_tools[n].pressure >= scanned_tools[n+1].pressure:
                    del scanned_tools[n+1]
                else:
                    del scanned_tools[n]
                continue
            n += 1
        
        # add <Tool> instances with found parameters into toollist attribute
        for t in scanned_tools:
            self.toollist.append(Tool.Tool(t.name, typ=t.typ, pressure=t.pressure, tool_check=t.tool_check, sister=t.sister))
        
        
    def prt_toollist(self):
        """
        Method sends summary of attribute <toollist> to standard output

        Returns
        -------
        None.

        """
        
        for n in self.toollist:
            print(n)

        
    def post_standalone(self, filename=''):
        """
        Method creates NC program based on tools in attribute <toollist> and sates it 
        into output file.
        The output NC program set up all tools in CNC machine. 

        Parameters
        ----------
        filename : string, optional
            The path to output NC file. The default is ''.

        Returns
        -------
        None.

        """
        
        # if output filename is not given and filename has been stored in attribute, set it as attribute content
        if not filename and self._output_file:
            filename = self._output_file
        
        # set free pockett number for sister tool
        pocketts = []
        for x in self.toollist: # extract all pockett numbers from toollist
            pocketts.append(x.pockett)
        free_pockett = max(pocketts) + 2    # find the biggest one and set free pockett
        
        # adding sister tools into attribute <toollist>
        tools = []  # help toollist with sistertools 
        for tool in self.toollist:
            if tool.sister > 1:     # for each tool from <toollist>, which has set sister tool
                # append sister tool 1 with original pockett nr. into help toollist
                tools.append(Tool.Tool(tool.name, tool.typ, tool.lenght, tool.radius, tool.max_speed, tool.pressure, tool.tool_check, sister=1, pockett=tool.pockett))
                # append sister tools 2, 3, ... with free pockett nr. into help toollist
                for n in range(1, tool.sister):
                    tools.append(Tool.Tool(tool.name, tool.typ, tool.lenght, tool.radius, tool.max_speed, tool.pressure, tool.tool_check, sister=n+1, pockett=free_pockett))
                    free_pockett += 2 # increase free pockett nr.
            else: tools.append(tool) # if tool has no other sister tool, append just the tool
        self.toollist = tools # update attribute <toollist> with sister tools
        
        # NC output file header
        output = '''
DEF INT TOOL_NAME
DEF INT SISTER
DEF INT POCKETT
DEF INT TOOL_NR
DEF INT EDGE\n
;TOOL MAGAZIN ZEROPOINT,VERSION=1.01,TYPE=GC,TOOL=1,MAGAZIN=1,NPV=0,BNPV=0,CHAN=1 "IS_METRIC"=1, "IS_OPT_DNO"=0, IS_CREATE_TOOL_T_NR=0
METRIC
CHANDATA(1)\n
'''
        # for each tool call NC postprocess and add it into NC output        
        for n in self.toollist:
            output += n.postprocess()
        
        # add NC output footer
        output += 'M30\n'
        
        # write NC output to file
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(output)
        else:
            raise FileNotFoundError('Tools not loaded yet.')


    def edit_tools(self):
        """
        Method enable manual editing parameters of loaded tools

        Returns
        -------
        None.

        """
        x = Tool_table.Tool_table(self.toollist) # raise editing window
        self.toollist = x.toollist # update attribute <toollist> with edited parameters



if __name__ == '__main__':
    # testing
    x = Grob_tools()
    x.load_tools('0033_SONDA.MPF')
    x.edit_tools()
    x.post_standalone()
    x.prt_toollist()
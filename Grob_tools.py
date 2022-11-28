# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Wed Nov  9 10:10:42 2022

@author: vokac
"""

import Tool
import Tool_scanner
import Tool_table
import os


class Grob_tools:
    
    def __init__(self):
        self.toollist = []
        self._input_file = ''
        self._output_file = ''
        
        
    def load_tools(self, filename):
        self._input_file = filename
        self._output_file = os.path.join(os.path.split(filename)[0], '.'.join(str(os.path.split(filename)[1]).split('.')[:-1])) + '_tools.MPF'
        
        sc = Tool_scanner.Tool_scan()
        scanned_tools = sc.scan(self._input_file)

        for t in scanned_tools:
            self.toollist.append(Tool.Tool(t.name, t.typ, 0, 0, 16000, t.pressure, t.tool_check))
        
        
    def prt_toollist(self):
        for n in self.toollist:
            print(n)

        
    def post_standalone(self, filename=''):
        if not filename and self._output_file:
            filename = self._output_file
        
        output = '''
DEF INT TOOL_NR
DEF INT EDGE\n
DEF INT POCKETT\n
;TOOL MAGAZIN ZEROPOINT,VERSION=1.01,TYPE=GC,TOOL=1,MAGAZIN=1,NPV=0,BNPV=0,CHAN=1 "IS_METRIC"=1, "IS_OPT_DNO"=0, IS_CREATE_TOOL_T_NR=0
METRIC
CHANDATA(1)\n
'''
        for n in self.toollist:
            output += n.postprocess()
            
        output += 'M30\n'
        
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(output)
        else:
            raise FileNotFoundError('Tools not loaded yet.')


    def edit_tools(self):
        x = Tool_table.Tool_table(self.toollist)
        self.toollist = x.edit()
        



if __name__ == '__main__':
    x = Grob_tools()
    x.load_tools('0057.MPF')
    x.edit_tools()
    x.prt_toollist()
    x.post_standalone()
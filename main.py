# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
App creates instance of Grob_tools and loads list of tools from NC prog given as
an argument in command line.
Runs editing values of found toolset and postprocess new NC programm for Sinumerik
control system. The output NC program set up all tools and needed values
in CNC machine.
"""

import Grob_tools
import sys


if __name__ == '__main__':
    print('''
+----------------------------+
| Grob G-350 tool management |
|       v1.2 11-2022         |
+----------------------------+

''')
    if len(sys.argv) > 1:
        print('Creating tool list instance...')
        x = Grob_tools.Grob_tools()
        x.load_tools(sys.argv[1])
        print(f'Tools from {sys.argv[1]} loaded.')
        print('Edit tool parameters...')
        x.edit_tools()
        x.prt_toollist()
        x.post_standalone()
    else:
        print('No file executed.\nDrag & drop MPF file onto script icon.')
        input()

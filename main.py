# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Fri Nov 11 12:50:02 2022

@author: vokac
"""

import Grob_tools
import sys


if __name__ == '__main__':
    print('''
+----------------------------+
| Grob G-350 tool management |
|       v1.0 11-2022         |
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
        input('Press any key to exit...')
    else:
        print('No file executed.\nDrag & drop MPF file onto script icon.')
        input()

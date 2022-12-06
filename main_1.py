# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:50:07 2022

@author: vokac
"""

import Toollist

if __name__ == '__main__':

    x = Toollist.Toollist('4007.nc')
    x.postprocess()
    x.print_log()
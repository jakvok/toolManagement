# -*- coding: utf-8 -*-
#!/usr/bin/python3

import math
from enum import Enum


class Tool_type(Enum):
    """
    The enumeration stores values to determine tool type.
    """
    MILL = 120
    FACE = 140
    DRILL = 200
    PREDRILL = 220
    TAP = 240
    BALLMILL = 110
    THREAD_MILL = 145
    REAMER = 250    


class Tool:
    """
    Class represents machining tool of milling machine Grob G-350.
    Class stores all tool data and can generate nc code represents the tool
    in Sinumeric 840D language.
    """
    
    # fixed tool dimensions, Grob G-350 with 60 tool turret positions
    _max_tr = 170/2     # max. tool radius
    _max_tl = 350       # max. tool lenght
    _max_speed = 16000  # max. tool speed allowed [rev/min]
    _holder_rad = 31.5  # tool holder radius
    _pressure = 40      # max. internal cooling pressure
    _max_sister_tool_nr = 10    # max count of sister tools


    def __init__(self, name=str(), typ=120, lenght=0, radius=0, max_speed=_max_speed, pressure=_pressure, tool_check=False, sister=1):
        
        # tool name
        if len(str(name)) <= 32:
            self._name = str(name)
        else:
            raise ValueError('Tool name is tool long, max lenght = 32 chars.')
            
        self.typ = typ    # tool type
        self.lenght = lenght    # tool lenght
        self.radius = radius    # tool radius
        self.max_speed = max_speed    # max tool speed allowed
        self.pressure = pressure    # internal coolant pressure
        self.tool_check = tool_check    # set if tool check active
        self.sister = sister


    def __str__(self):
        return 'Tool parameters:\nname: {0}\n{1} {2}\nlenght: {3}\nradius: {4}\nmax. lenght: {5}\nmax. radius: {6}\nmax. speed: {7}\ncoolant pressure: {8}\ntool check: {9}\nsister nr: {10}\n'.format(self._name, self._typ, self._typ.value, self._lenght, self._radius, self._max_lenght, self._max_rad, self._max_speed, self._pressure, self._tool_check, self._sister)


    # tool name
    @property
    def name(self):
        return self._name


    # tool type
    @property
    def typ(self):
        return self._typ
    
    @typ.setter
    def typ(self, value):
        try:            
            self._typ = Tool_type(value)
        except ValueError as e:
            raise ValueError(e)
            

    # tool lenght
    @property        
    def lenght(self):
        return self._lenght

    @lenght.setter
    def lenght(self, value):
        if value >= 0 and value <= Tool._max_tl:
            self._lenght = value
            if value == 0:
                self._max_lenght = Tool._max_tl
            else:
                self._max_lenght = min([math.ceil(value/10)*10+10, Tool._max_tl])            
        else:
            raise ValueError('Tool lenght must be in range 0-{0}.'.format(Tool._max_tl))


    # tool radius
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value >= 0 and value <= Tool._max_tr:
            self._radius = value
            self._max_rad = max([min([math.ceil(value)+1, Tool._max_tr]), Tool._holder_rad])
        else:
            raise ValueError('Tool radius must be in range 0-{0}.'.format(Tool._max_tr))
    

    # max tool lenght
    @property
    def max_lenght(self):
        return self._max_lenght
    
    @max_lenght.setter
    def max_lenght(self, value):
        if value >= self._lenght and value <= Tool._max_tl:
            self._max_lenght = value
        else:
            raise ValueError('Max. lenght out of range [{0}-{1}]'.format(self._lenght, Tool._max_tl))


    # max tool radius
    @property
    def max_rad(self):
        return self._max_rad

    @max_rad.setter
    def max_rad(self, value):
        if value >= max([self._radius, Tool._holder_rad]) and value <= Tool._max_tr:
            self._max_rad = value
        else:
            raise ValueError('Max. radius out of range [{0}-{1}]'.format(max([self._radius, Tool._holder_rad]), Tool._max_tr))


    # max tool speed allowed
    @property
    def max_speed(self):
        return self._max_speed
    
    @max_speed.setter
    def max_speed(self, value):
        if value > 0 and value <= Tool._max_speed:
            self._max_speed = value
        else:
            raise ValueError('Must be: 16000 > Max. tool speed > 0.')


    # internal coolant pressure
    @property
    def pressure(self):
        return self._pressure
    
    @pressure.setter
    def pressure(self, value):
        if value >= 0 and value <= Tool._pressure:
            self._pressure = value
        else:
            raise ValueError('Internal coolant pressure must be in range 0-{0}'.format(Tool._pressure))
            
    
    # set if tool check active
    @property
    def tool_check(self):
        return self._tool_check
    
    @tool_check.setter
    def tool_check(self, value):
        if isinstance(value, bool):
            self._tool_check = value
        else:
            raise ValueError('Tool check must be bool value. True/False.')


    @property
    def sister(self):
        return self._sister

    @sister.setter
    def sister(self, value):
        if isinstance(value, int):
            if int(value) in range(1,Tool._max_sister_tool_nr + 1):
                self._sister = value
            else:
                raise ValueError('Sister tool number must be in range 1 to {0}.'.format(Tool._max_sister_tool_nr))
        else:
            raise ValueError('Sister tool number must be integer.')


    def postprocess(self):
        """
        Returns tool's representation in Sinumeric 840D code. 
        """
        output = f'''
;{self._typ}
POCKETT={self._name}
TOOL_NR=POCKETT+750
$TC_TP1[TOOL_NR]={self._sister}    ;sister nr.
$TC_TP2[TOOL_NR]=""<<POCKETT
$TC_TP3[TOOL_NR]=1
$TC_TP4[TOOL_NR]=1
$TC_TP5[TOOL_NR]=1
$TC_TP6[TOOL_NR]=1
$TC_TP7[TOOL_NR]=1
$TC_TP8[TOOL_NR]=131
;$A_TOOLMN[TOOL_NR]=1
;$A_TOOLMLN[TOOL_NR]=POCKETT
;$P_TOOLND[TOOL_NR]=1    ;D1, D2, D...
;$A_MYMN[TOOL_NR]=1
;$A_MYMLN[TOOL_NR]=POCKETT
$TC_TPC1[TOOL_NR]={int(self._tool_check)}    ;tool check
$TC_TPC2[TOOL_NR]={self._pressure}    ;ic pressure
$TC_TPC4[TOOL_NR]={self._max_speed}    ;max speed
$TC_TPC5[TOOL_NR]=0
$TC_TPC6[TOOL_NR]=0
$TC_TPC21[TOOL_NR]={self._max_lenght}   ;max lenght
$TC_TPC22[TOOL_NR]={self._max_rad}    ;max rad
$TC_TPC27[TOOL_NR]=1
EDGE=1   ; D nr.
$TC_DP1[TOOL_NR,EDGE]={self._typ.value}    ;typ
$TC_DP2[TOOL_NR,EDGE]=9
$TC_DP3[TOOL_NR,EDGE]={self._lenght}    ;lenght
$TC_DP6[TOOL_NR,EDGE]={self._radius}    ;radius
$TC_DP12[TOOL_NR,EDGE]=0    ;lenght offset
$TC_DP15[TOOL_NR,EDGE]=0    ;radius offset
$TC_DP25[TOOL_NR,EDGE]=256
$TC_MPP6[1,POCKETT]=TOOL_NR\n
'''
        return output


if __name__ == '__main__':
    x=Tool(1, 120, 145, 6.955, 15000, 40, True, 2)
    print(x)
    x.max_rad = 32
    x.max_lenght = 147
    print(x.postprocess())
    #with open('tool.MPF', 'w', encoding='utf-8') as f:
    #   f.write(x.postprocess())







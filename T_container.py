#!/usr/bin/python3


class T_container:
    """
    Instance of the class represents the tool and some it's parameters which are possible to extract from given NC file.
    
    input: 
        - list <lines>: all lines of NC file; each list element = one NC file line
        - int <pos>: index in <lines>, where toolchange located
    
    """
    def __init__(self, lines, pos):
        
        # extract tool name (the number) from reference line with tool change. The number is following T letter.
        name = ''
        for ch in lines[pos][1:]:
            if ch.isdigit(): 
                name += ch
            else:
                break

        self.name = name
        # set default values
        self.typ = 120
        self.pressure = 0
        self.tool_check = False
        self.sister = 1

        # go downward thru lines, find keywords and set parameters
        n = pos
        while True:
            # set internal cooling pressure at 40bars if M7 found
            if lines[n].endswith('M7') or 'M7 ' in lines[n]:
                self.pressure = 40
            # increase sister tool number if SETPIECE found
            if 'SETPIECE(' in lines[n]:
                self.sister += 1
            # set tool type to drill if drilling cycles found
            if 'CYCLE81(' in lines[n] or 'CYCLE83(' in lines[n]:
                self.typ = 200
            # set tool type to tap if tapping cycle found
            if 'CYCLE84(' in lines[n]:
                self.typ = 240
            # set tool type to reamer if reaming cycle found
            if 'CYCLE85(' in lines[n]:
                self.typ = 250
            # protection against empty toolchange at the end of the nc prog
            if 'M30' in lines[n]:
                self.name = None
                break
            # ends parsing at end of tool section
            if lines[n].endswith('M5') or 'M5 ' in lines[n]:
                break
            n += 1
        
        # go upward thru lines, find keywords and set parameters
        n = pos
        while True:
            # find line with N letter at the beginning
            if lines[n].startswith('N'):
                # set tool type to thread mill
                if 'ZAVIT' in lines[n] and 'FR' in lines[n]:
                    self.typ = 145
                # set tool type to face mill
                elif 'CELNI' in lines[n]:
                    self.typ = 140
                # set tool type to pre drill
                elif 'NAVRT' in lines[n]:
                    self.typ = 220
                # set tool type to ball mill
                elif 'KULO' in lines[n] or 'KOUL' in lines[n]:
                    self.typ = 110
                # set tool type to deburring tool
                elif 'SRAZ' in lines[n] or 'ODHROT' in lines[n]:
                    self.typ = 120
                else:
                    pass
                break
            n -= 1

            # turn on tool check if tool is holemaking tool
            if self.typ in [200, 220, 240, 250]:
                self.tool_check = True

    def __str__(self):
        """
        Text representation of tool container

        Returns
        -------
        TYPE   string
        """
        return 'name:{0} typ:{1} pressure: {2} tool_check: {3} sisterNr: {4}'.format(self.name, self.typ, self.pressure, self.tool_check, self.sister)


        
if __name__ == '__main__':
    pass
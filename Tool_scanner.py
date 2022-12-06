# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Thu Nov 10 07:52:23 2022

@author: vokac
"""
class T_container:
    
    def __init__(self, lines, pos):
        
        name = ''
        for ch in lines[pos][1:]:
            if ch.isdigit(): 
                name += ch
            else:
                break

        self.name = name
        self.typ = 120
        self.pressure = 0
        self.tool_check = False
        self.sister = 1

        n = pos
        while True:
            if lines[n].endswith('M7') or 'M7 ' in lines[n]:
                self.pressure = 40
            if 'SETPIECE(' in lines[n]:
                self.sister += 1
            if 'CYCLE81(' in lines[n] or 'CYCLE83(' in lines[n]:
                self.typ = 200
            if 'CYCLE84(' in lines[n]:
                self.typ = 240
            if 'CYCLE85(' in lines[n]:
                self.typ = 250
            if lines[n].endswith('M5') or 'M5 ' in lines[n]:
                break
            n += 1
        
        n = pos
        while True:
            if lines[n].startswith('N'):
                if 'ZAVIT' in lines[n] and 'FR' in lines[n]:
                    self.typ = 145
                elif 'CELNI' in lines[n]:
                    self.typ = 140
                elif 'NAVRT' in lines[n]:
                    self.typ = 220
                elif 'KULO' in lines[n] or 'KOUL' in lines[n]:
                    self.typ = 110
                elif 'SRAZ' in lines[n] or 'ODHROT' in lines[n]:
                    self.typ = 120
                else:
                    pass
                break
            n -= 1

            if self.typ in [200, 220, 240, 250]:
                self.tool_check = True

    def __str__(self):
        return 'name:{0} typ:{1} pressure: {2} tool_check: {3} sisterNr: {4}'.format(self.name, self.typ, self.pressure, self.tool_check, self.sister)


class Tool_scan:
    
    def __init__(self):
        
        self._lines = []
        self._tools = []
        
        
    def scan(self, filename):
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    self._lines.append(line.strip())
        except FileNotFoundError as e:
            print(e)
          
        tools_pos = []
        for n in range(len(self._lines)-1):
            if self._lines[n].startswith('T') and self._lines[n+1] == 'M6' and '=' not in self._lines[n]:
                tools_pos.append([self._lines[n], n])
        
        #for k in tools_pos:
        #    print('{0}: {1}'.format(k[0], k[1]))
        
        for k in tools_pos:
            self._tools.append(T_container(self._lines, k[1]))
        
        self._tools.sort(key=lambda x: int(x.name))
        
        n = 0
        while 1:
            if n >= len(self._tools)-1: break
            if self._tools[n].name == self._tools[n+1].name:
                if self._tools[n].pressure >= self._tools[n+1].pressure:
                    del self._tools[n+1]
                else:
                    del self._tools[n]
                continue
            n += 1

        return self._tools

        
if __name__ == '__main__':
    x = Tool_scan()
    tools = x.scan('0057.MPF')
    for n in tools:
        print(n)
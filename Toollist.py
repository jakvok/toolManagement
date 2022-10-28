# -*- coding: utf-8 -*-
#!/usr/bin/python3

import sys


class Toollist:
    """
    Created on Thu Oct 27 11:32:49 2022
    
    @author: vokac
    """
    @staticmethod
    def pick_PR_params(line):
        p = '0'
        r = '0'
        for n in range(len(line)):
            if line[n] == 'P':
                x = 1
                while line[n+x].isdigit() or line[n+x] == '.': 
                        p += line[n+x]
                        x += 1
            if line[n] == 'R':
                x = 1
                while line[n+x].isdigit() or line[n+x] == '.': 
                        r += line[n+x]
                        x += 1
        return int(p), float(r)
        
    
    def __init__(self, filename=None):
        self.__dimms = dict()
        self.__err_log = []
        self.__output_file = ''
        if filename:
            self.load_nc(filename)
            
            
    def load_nc(self, filename):
        self.__output_file = filename + '_grob.MPF'
        try:
            with open(filename,'r',encoding='utf-8') as f:
                for line in f.readlines():
                    if 'L10' in line:
                        params = Toollist.pick_PR_params(line)
                        if params[0] not in self.__dimms.keys():
                            self.__dimms[params[0]] = [params[1],0.0]
                        else:
                            self.__dimms[params[0]][0] = params[1]
                    elif 'L12' in line:
                        params = Toollist.pick_PR_params(line)
                        if params[0] not in self.__dimms.keys():
                            self.__dimms[params[0]] = [0.0,params[1]]
                        else:
                            self.__dimms[params[0]][1] = params[1]
                    else:
                        pass
            for key in self.__dimms.keys():
                if self.__dimms[key][0] == 0.0:
                    self.__err_log.append('Tool {0} has {1} lenght!!!'.format(key, self.__dimms[key][0]))
        except FileNotFoundError:
            self.__err_log.append('File <{}> not found.'.format(filename))
            

    def save_nc(self):
        try:
            with open(self.__output_file, 'w', encoding='utf-8') as f:
                for item in self.__err_log:
                    f.write('; {}\n'.format(item))
                
                for key in self.__dimms.keys():
                    f.write('T{} L{} R{}\n'.format(key, self.__dimms[key][0], self.__dimms[key][1]))
        except:
            print('Saveing failed.')


    def postprocess(self):
        output = '; nastrojove korekce NHX -> GROB\n'
        for item in self.__err_log:
            output += '; {}\n'.format(item)
        output += '\nDEF REAL TOOL_NR\nDEF STRING[31] TOOL_NAME\n\n'

        for key in self.__dimms.keys():
            output += '; nastroj T{0}\nTOOL_NAME=\"{0}\"\nTOOL_NR=GETT(TOOL_NAME,1) ; sestra=1\n'.format(key)
            output += '$TC_DP3[TOOL_NR,1]={0} ; delka, brit=1\n'.format(self.__dimms[key][0])
            if self.__dimms[key][1] > 0.0:
                output += '$TC_DP6[TOOL_NR,1]={0} ; radius, brit=1\n'.format(self.__dimms[key][1])
            output += '\n'
        output += 'M30\n'

        try:
            with open(self.__output_file, 'w', encoding='utf-8') as f:
                f.write(output)
        except Exception as e:
            print('Saveing failed.')
            print(e)


    def print_log(self):
        for i in self.__err_log:
            print('{}\n'.format(i))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        x = Toollist(sys.argv[1])
        x.postprocess()
        x.print_log()
        #input()
    else:
        print('No file executed.')
        input()


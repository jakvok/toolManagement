# -*- coding: utf-8 -*-
#!/usr/bin/python3

import sys, math, os


class Toollist:
    """
    Represents list of tools and their dimmensions. Values are extracted from NHX machine cnc program and
    can be converted into cnc program readable for other machine Grob G-350.
    
    @author: vokac
    """
    @staticmethod
    def pick_PR_params(line):
        """
        Extract int & float values from string. Values follows addresses 'P' and 'R' in the string.
        example: pick_PR_params('G10L10P3R113.125')= 3, 113.125
        Input: string
        Output: tuple p, r
        """
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
        # dictionary which contains tool dimmensions; key=tool name, value=[tool lenght, tool radius]
        self.__dimms = dict()
        # list of error logs
        self.__err_log = ['Error log:\n']
        # output file path
        self.__output_file = ''
        if filename:
            self.load_nc(filename) # fill __dimms dict by values from NHX nc file
            
            
    def load_nc(self, filename):
        """
        Fills __dimms dict by values from NHX nc file. Gets each tool's lenght and radius.
        Input: NHX nc file name (path)
        Returns: None
        """

        # set output file path and new name, replace '.' in filename by '_' and give a new extension
        self.__output_file = os.path.join(os.path.split(filename)[0], os.path.split(filename)[1].replace('.', '_') + '_grob.MPF')
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    # Extract tool lenght follows after L10 word in line and put it into the __dimm dict
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
        except Exception as e:
            self.__err_log.append('Save into <{0}> file failed.'.format(self.__output_file))
            self.__err_log.append(e)


    def postprocess(self):
        """
        Reads __dimm dict of tools dimmension values and creates converted nc file from that
        Input: None
        Output: None
        """
        output = '; nastrojove korekce NHX -> GROB\n'
        if len(self.__err_log) > 1:
            for item in self.__err_log:
                output += '; {}\n'.format(item)
        output += '\nDEF REAL TOOL_NR\nDEF STRING[31] TOOL_NAME\n\n'

        for key in self.__dimms.keys():
            output += '; nastroj T{0}\nTOOL_NAME=\"{0}\"\nTOOL_NR=GETT(TOOL_NAME,1) ; sestra=1\n'.format(key)
            output += '$TC_DP3[TOOL_NR,1]={0} ; delka, brit=1\n'.format(self.__dimms[key][0])
            if self.__dimms[key][1] > 0.0:
                output += '$TC_DP6[TOOL_NR,1]={0} ; radius, brit=1\n'.format(self.__dimms[key][1])
            output += '$TC_TPC21[TOOL_NR]={0} ; max delka\n'.format(math.ceil(self.__dimms[key][0]/10)*10+10)
            output += '$TC_TPC22[TOOL_NR]={0} ; max radius\n'.format(max([math.ceil(self.__dimms[key][1])+1, 31.5]))
            output += '\n'
        output += 'M30\n'
        
        try:
            with open(self.__output_file, 'w', encoding='utf-8') as f:
                f.write(output)
        except Exception as e:
            self.__err_log.append('Save into <{0}> file failed.'.format(self.__output_file))
            self.__err_log.append(e)


    def print_log(self):
        if len(self.__err_log) > 1:
            for i in self.__err_log:
                print('{}\n'.format(i))
            input()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        x = Toollist(sys.argv[1])
        x.postprocess()
        x.print_log()
    else:
        print('No file executed.\nDrag & drop NHX file onto script icon.')
        input()


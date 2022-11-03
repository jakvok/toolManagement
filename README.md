# Tool list convert utility

Tool dimensions can be set directly by cnc program, but each type of machine has it's own cnc code dialect.
Use case is, that device for tool measurement can output cnc program just in one type of cnc code dialect and it is needed to translate the code into other dialect. 
The script do that, converts Mori-Seiki NHX4000 machine (Fanuc) cnc prog to Grob G-350 machine (Siemens 840D) cnc prog. 

<br><br>
## linux
Python 3.10+, only standard modules required on linux.<br>
Make the script executable:
`$ chmod +x ./Toollist.py`,<br>
Give the source file as argument when execute:
`$ ./Toollist.py <file>`,<br>

<br><br>
## windows
The best way is use the standalone executable `Toollist_nhx-grob_vx.x.exe` and drag&drop the source file on it.
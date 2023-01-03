# TOOL LIST EXTRACT UTILITY

The script parse NC program, find all machining tools used in it, extracts technological data concerning each tool, then offers found data to edit and creates separate NC program used to load the data into NC machine tool turret management.
The CNC dialect is for Siemens SINUMERIK 840D control system.
<br><br>
The script handle this data:
- List of all machining tools and their T-numbers (names),
- tool lenghts,
- tool radiuses,
- tool max. allowed lenghts,
- tool max. allowed radiuses,
- tool max. allowed spindle speeds,
- tool internal cooling pressure,
- if tool is checked for break after machining
- number of sister tools for each one.


## Usage on windows 10

### requirements
- No special requirements, if using standalone executable,
- python 3.10+, if run the script from console.

### run script from standalone executable
Drag & drop NC file from where you wish to extract tool data onto script icon.<br>
After that editing dialog starts, where all found machining tool's data are possible to check/change.<br>
Hit `EXIT` button to postprocess found/edited tool data and create output NC program for machine tool management.

### run script from console
Go to work folder and run `python main.py <nc_file.MPF>`, where `nc_file.MPF` is path to NC file from where you wish to extract tool data.<br>
After that editing dialog starts, where all found machining tool's data are possible to check/change.<br>
Hit `EXIT` button to postprocess found/edited tool data and create output NC program for machine tool management.


## Usage on linux

### requirements
- python 3.10+

### run
Go to work folder and make the script executable: `$ chmod +x ./main.py`.<br>
Give the source NC file from where you wish to extract tool data as argument when execute:`$ ./main.py <nc_file.MPF>`.<br>
After that editing dialog starts, where all found machining tool's data are possible to check/change.<br>
Hit `EXIT` button to postprocess found/edited tool data and create output NC program for machine tool management.




# TOOL LIST CONVERT UTILITY

The script converts NC offset program from Mori-Seiki NHX4000 machine (Fanuc) dialect to Grob G-350 machine (Siemens Sinumerik 840D) cnc dialect. <br>
The use case is to get NC offset program for Sinumerik machine from Zoeller measuring machine, which can generate NC offset program only for Fanuc machine.<br>
The NC offset program is used to simply set tool offsets into cnc machine. It avoids human mistakes and improoves setting time.<br>

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
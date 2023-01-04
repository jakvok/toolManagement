# OVERVIEW
The goal of using both presented utilities is to avoid human mistakes and shorten the time of initial CNC machine setup when new production batch starts.<br>
Standard way to set up all tool data into CNC machine before start machining is to type them manually into machine's tool table. Script `TOOL LIST EXTRACT UTILITY` creates CNC program for CNC machine, which do that automaticaly. It set up tools in machine's tool stack (tool table) and load in tool data. Script extracts the tool data from CNC machining program.<br>
The next step is to load geometric dimmensions (lenghts and radiuses) of real prepared tools also into machine's tool table. Standard way is to use the Zoeller measuring machine to measure all tool dimms. Zoeller generates CNC code, which executed at CNC machine fills the dimms into machine's tool table.<br>
However Zoeller generates CNC code in Fanuc dialect, script `TOOL LIST CONVERT UTILITY` converts Fanuc CNC code to Siemens CNC code without Zoeller's postprocessor for Siemens needed.
<br><br>



# TOOL LIST EXTRACT UTILITY

The script parse CNC machining program, find all machining tools used in it, extracts technological data concerning each tool, then offers found data to edit and creates separate CNC program used to load the data into CNC machine tool turret management.
The output CNC dialect is for Siemens SINUMERIK 840D control system.
<br><br>
The script handle this data:
- List of all machining tools and their T-numbers (names),
- tool lenghts,
- tool radiuses,
- tool max. allowed lenghts,
- tool max. allowed radiuses,
- tool max. allowed spindle speeds,
- tool internal cooling pressure,
- if tool is checked for break after machining,
- number of sister tools for each one.


## Usage on windows 10

### Requirements
- No special requirements, if using standalone executable,
- python 3.10+, if run the script from console.

### Run script from standalone executable
Drag & drop CNC file from where you wish to extract tool data onto script `Grob_tools_vx.x.x.exe` icon.<br>
After that editing dialog starts, where all found machining tool data are possible to check/change.<br>
Hit `EXIT` button to postprocess found/edited tool data and create output CNC program for machine tool management.
The output CNC program is saved at the same folder as source CNC file, the name is `<old_nc_file_name>_tools.MPF`.

### Run script from console
Go to work folder and run `python main.py <nc_file.MPF>`, where `nc_file.MPF` is path to CNC file from where you wish to extract tool data.<br>
After that editing dialog starts, where all found machining tool data are possible to check/change.<br>
Hit `EXIT` button to postprocess found/edited tool data and create output CNC program for machine tool management.
The output CNC program is saved at the same folder as source CNC file, the name is `<old_nc_file_name>_tools.MPF`.


## Usage on linux

### Requirements
- python 3.10+

### Run
Go to work folder and make the script executable: `$ chmod +x ./main.py`.<br>
Give the source CNC file from where you wish to extract tool data as argument when execute:`$ ./main.py <nc_file.MPF>`.<br>
After that editing dialog starts, where all found machining tool data are possible to check/change.<br>
Hit `EXIT` button to postprocess found/edited tool data and create output CNC program for machine tool management.
The output CNC program is saved in the same folder as source CNC file, the name is `<source_file_name>_tools.MPF`.

## Examples
Example input CNC machining code file from which are tools data extracted is `Demo.MPF`.<br>
Example output CNC tool data code is `Demo_tools.MPF`.
<br><br>



# TOOL LIST CONVERT UTILITY

The script converts CNC offset program from Mori-Seiki NHX4000 machine (Fanuc) CNC code dialect to Grob G-350 machine (Siemens Sinumerik 840D) CNC code dialect. <br>
The use case is to get CNC offset program for Sinumerik machine from Zoeller measuring machine, which can generate CNC offset program only for Fanuc machine.<br>
The CNC offset program is used to simply set tool offsets into CNC machine. It avoids human mistakes and improoves setting time.<br>


## Usage on windows 10

### Requirements
- No special requirements, if using standalone executable,
- python 3.10+, if run the script from console,
- in source CNC offset file must be sister tool set as X*100 + T-number of parent tool:
<br>
    -T3   = parent tool<br>
    -T103 = sister tool 1<br>
    -T203 = sister tool 2<br>
    -...<br>
 
### Run script from standalone executable
Drag & drop CNC offset file you want to convert onto script `Toollist_nhx-grob_vx.x.exe` icon.<br>
The script makes conversion and saves converted CNC offset program in the same folder as source CNC file, the name is `<source_file_name>_nc_grob.MPF`.

### Run script from console
Go to work folder and run `python Toollist.py <nc_file.NC>`, where `nc_file.NC` is path to CNC offset file you want to convert.<br>
The script makes conversion and saves converted CNC offset program in the same folder as source CNC file, the name is `<source_file_name>_nc_grob.MPF`.


## Usage on linux

### Requirements
- python 3.10+,
- see source CNC file note in win usage section

### Run
Go to work folder and make the script executable `$ chmod +x ./Toollist.py`.<br>
Give the source CNC file which you want to convert as argument when execute `$ ./Toollist.py <nc_file.NC>`.<br>
The script makes conversion and saves converted CNC offset program in the same folder as source CNC file, the name is `<source_file_name>_nc_grob.MPF`.

## Examples
Example input CNC Fanuc code file with measured tool dimmensions is `Demo_Zoeller.nc`.<br>
Example output converted CNC Siemens code file is `Demo_Zoeller_nc_tools.MPF`.



# Grid-Tie measurement and datalogging with AC6802B AC source app note <br>
# Pre-requirements: <br>
1-	Python 3.6+: https://docs.python-guide.org/starting/install3/win/#install3-windows <br>
2-	Setup tools + pip: https://docs.python-guide.org/starting/install3/win/#install3-windows <br>
3-	Install pyVISA package: https://pyvisa.readthedocs.io/en/latest/introduction/getting.html <br>
4-	Connect Keysight AC6802B LAN directly to PC computer (not use any switch) <br>
5-	Find the IP address via the following steps: <br>
a.	[Menu] > System > IO > LAN > Setting <br>
b.	IP address is indicated in this page, and it should be start with “169” if you connect the LAN to the computer directly. <br> 
6-	Please make sure that the computer is NOT going into sleep mode or turn-off (because the LAN connectivity is required all over the measurement period) <br>
7-	Download and save the python program (“daanaa_cfv.py”) in the specific folder. <br>
# Run the program and measurement: <br>
1-	You can run the code by the following syntax on cmd in the folder you have save the program: <br>
python3 daanaa_cfv.py <br>
2-	It is required to enter the VISA address of the instrument. To turn the measurement on, the IP address found in step 5 (as x latter) with the following syntax is needed to be entered: <br>
TCPIP::xxx.xxx.xxx.xxx::inst0::INSTR <br>
3-	The AC source is running and every 10 second the data is logged, and csv files is getting filled. The number of data logged is indicated in cmd in the following format: <br>
[i] Data is logging... <br>
“i” is counting the number of data saved in csv files. <br>
4-	To terminate the program and turn off the AC source in the middle of the measurement and data logging, “Ctrl + c” would terminate the program. <br>

# Note 1:
if the program is terminated by any reason (including the LAN disconnection) there is two ways to turn the AC source off: <br>
I.	Push on/off hard switch on the AC source to turn it off. <br>
II.	Rerun the program (is there is stable LAN connecting between the computer and AC source) and terminate the program via “Ctrl +c” after 12 sec. <br>
# Note 2: 
rerunning the program is overwriting the csv file. To have the back-up of the previous file, you need to change the name of the file or copy it to the different folder. 

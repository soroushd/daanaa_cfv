# import module 
import pyvisa
import time
import csv
import os	


print('Daanaa Solar Panel Data Logger for Voltage, Current, and Power Measurements to csv file \n')

# connection address of the instrument
print('Enter VISA address of the instrument (e.g. TCPIP::169.254.163.185::inst0::INSTR)')
VisaAddress = input()

# initialize visa resource
rm = pyvisa.ResourceManager()

# open the resouce using the VISA address
AC6802B = rm.open_resource(VisaAddress)

# instrument identification
modelSerialnumber = AC6802B.query('*IDN?')
print (modelSerialnumber)

line = 0

AC6802B.write(':OUTPut:COUPling AC')
AC6802B.write(':SOURce:VOLTage:OFFSet 0')
AC6802B.write(':SOURce:FREQuency 60')
AC6802B.write(':SOURce:VOLTage:RANGe:AUTO 1')
AC6802B.write(':SOURce:VOLTage 240')
AC6802B.write('OUTPut %G' %(1))

#Check for Error
AC6802B.write('SYST:ERR?')
print(AC6802B.read())

time.sleep(1)

#-----------------------------------------------------
#retrieve output log to csv file 
#-----------------------------------------------------
#periodically retrieve voltage, current, and power measurements 
with open("Daanaa_Datalogger.csv", mode='w', newline='') as f:
	f_write = csv.writer(f)
    #create column headers on csv file 
	f_write.writerow(['Day','Time','Current_AC','Voltage_AC','Current_ACDC','Voltage_ACDC', 'PF_AC', 'ActivePower_AC', 'ReactivePower_AC', 'ApparentPower_AC','PF_ACDC', 'ActivePower_ACDC', 'ReactivePower_ACDC', 'ApparentPower_ACDC'])
	print('External Datalogger is initiated and running')
	try:		
		for i in range(0, 20000):
			temp_values = AC6802B.query_ascii_values(':MEASure:ALL?')
			f_write.writerow([time.strftime('%b %d %Y'), time.strftime('%H:%M:%S'), temp_values[1], temp_values[16], temp_values[2], temp_values[17], temp_values[10], temp_values[7], temp_values[9], temp_values[8], temp_values[14], temp_values[11], temp_values[13], temp_values[12]])
			time.sleep(10)
			line += 1
			print('[%i] Data is logging...' %(line))
	except KeyboardInterrupt:
		pass


AC6802B.write('OUTPut %G' %(0))

#Abort Elog 
AC6802B.write('ABOR:ALL')
print('External Datalogger Completed') 

# close
AC6802B.close()
rm.close()


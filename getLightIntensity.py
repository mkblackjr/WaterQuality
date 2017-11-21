# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:37:18 2017

@author: MAYA
"""
<<<<<<< HEAD
=======

>>>>>>> master
# Imports
import serial
import time
import threading
import csv

def get_L(L_list,num,arduino):
	freqs = arduino.readline().decode()
	if freqs != "":
		ret = ""
		for char in freqs:
			if char == "\n":
				break
			ret += char
		ret = float(ret.replace("L" + str(num) + " = ","").replace(" cd\r",""))
		L_list.append(ret)
		print(ret)
	
def getData(L1,L2,L3,L4,L5,stopProgram,start_time):
	title = ["Clean Water Light Intensity Test - 20171120 - Dark Room"]
	port = "COM17"
	baud_rate = 9600
	arduino = serial.Serial(port,baud_rate)
	time.sleep(2)
	
	while not stopProgram[0]:
		current_time = time.time() - start_time
		
		get_L(L1,1,arduino)
		get_L(L2,2,arduino)
		get_L(L3,3,arduino)
		get_L(L4,4,arduino)
		get_L(L5,5,arduino)
			
	L1.insert(0,"L1 (uW/cm^2)")
	L2.insert(0,"L2 (uW/cm^2)")
	L3.insert(0,"L3 (uW/cm^2)")
	L4.insert(0,"L4 (uW/cm^2)")
	L5.insert(0,"L5 (uW/cm^2)")
	data = [title,L1,L2,L3,L4,L5,["Duration = ",str(current_time) + "sec"]]
		
	with open('LightIntensityOutput.csv','w') as f:
		csv.writer(f).writerows(data)
	

if __name__ == "__main__":

	L1 = []; L2 = []; L3 = []; L4 = []; L5 = []
	stopProgram = [False,"extra"]
    
	if raw_input("Press Enter to Begin.\r\n") == "":
		start_time = time.time()
		data_thread = threading.Thread(target=getData,args=(L1,L2,L3,L4,L5,stopProgram,start_time,))
		data_thread.start()
		while raw_input("Type STOP to stop the program.\r\n") != "STOP":
			pass
		stopProgram[0] = True
		data_thread.join()
			
		
			
			

#LIBS
import serial, sys
from os import listdir
from time import sleep

BAUD_RATE = 115200

def establish_connection(port):
    
    try:
        filesForDevice = listdir('/dev/') # put all device files into list[]

        for line in filesForDevice: # run through all files
            line[:7] == port # looks specifically for USB port that encoder is plugged into
            devicePort = line # take whole line (includes suffix address e.g. ttyACM0
            connection = serial.Serial('/dev/' + str(devicePort), BAUD_RATE, timeout = 6, writeTimeout = 20) # assign
                
        return connection

    except: 
        print(port + ': No arduino connected')

def receiver(serial_obj): 
    if serial_obj.inWaiting():
        rec_temp = serial_obj.readline().decode('utf-8').upper().strip()
        return rec_temp
        
serial_obj_1 = establish_connection("ttyACM0")
serial_obj_2 = establish_connection("ttyACM1")
serial_obj_3 = establish_connection("ttyACM2")

sleep(5)

serial_obj_1.flushInput()
serial_obj_2.flushInput()
serial_obj_3.flushInput()

while True:
    
    with open("ATAG_CABLE_RESULTS_1.txt", "a") as f:
        line = receiver(serial_obj_1)
        if line:
            f.write(str(line))
            print(line)

    with open("ATAG_CABLE_RESULTS_2.txt", "a") as f:
        line = receiver(serial_obj_2)
        if line:
            f.write(str(line))
            print(line)
  
    with open("ATAG_CABLE_RESULTS_3.txt", "a") as f:
        line = receiver(serial_obj_3)
        if line:
            f.write(str(line))
            print(line)
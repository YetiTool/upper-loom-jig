import serial
from datetime import datetime

# Define the serial port and baud rate
SERIAL_PORT = '/dev/ttyACM0'  # Change this to match your Arduino's serial port
BAUD_RATE = 115200
RESULTS_FILE_PATH = '/home/pi/upper-loom-jig/RESULTS.txt'

current_time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

with open (RESULTS_FILE_PATH,'a') as f:
                f.write(f"START {current_time}\n")
                f.close()

# Establish serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    print("Serial connection established on port:", SERIAL_PORT)
except serial.SerialException as e:
    print("Failed to connect to Arduino:", e)
    exit()


with open (RESULTS_FILE_PATH,'a') as f:
                f.write(f"START {current_time}\n")
                f.close()
try:
    while True:
        if ser.in_waiting > 0:
            incoming_data = ser.readline().decode().strip()
            print("Received:", incoming_data)
            with open (RESULTS_FILE_PATH,'a') as f:
                f.write(incoming_data + "\n")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
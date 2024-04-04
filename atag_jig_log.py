import serial

# Define the serial port and baud rate
SERIAL_PORT = '/dev/ttyACM0'  # Change this to match your Arduino's serial port
BAUD_RATE = 115200

# Establish serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    print("Serial connection established on port:", SERIAL_PORT)
except serial.SerialException as e:
    print("Failed to connect to Arduino:", e)
    exit()

# Main loop to read and print serial messages
try:
    while True:
        if ser.in_waiting > 0:
            incoming_data = ser.readline().decode().strip()
            print("Received:", incoming_data)
            with open ('RESULTS.txt','a') as f:
                f.write(incoming_data"\n")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Close the serial connection
    ser.close()

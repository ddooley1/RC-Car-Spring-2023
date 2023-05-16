import serial

# Open a serial connection to the Sabertooth 2x25 motor driver
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

# Send the "Get Firmware Version" command (0x81) to the Sabertooth
ser.write(bytearray([0x80, 0x81, 0x00, 0x81]))

# Read the response from the Sabertooth
response = ser.read(4)

# Print the response
print("Response:", response)

# Close the serial connection
ser.close()
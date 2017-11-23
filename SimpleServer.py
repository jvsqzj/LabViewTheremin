import socket
from time import sleep
import serial
ser = serial.Serial('/dev/tty.usbmodem1d11', 9600) # Establish the connection on a specific port
counter = 32 # Below 32 everything in ASCII is gibberish


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8089))
server.listen(1)

while True:
    conn, addr = server.accept()
    cmnd = conn.recv(4)  # The default size of the command packet is 4 bytes
    print(cmnd)

    val = int(cmnd)
    if val in range(0,207):
        conn.sendall(b'G3')
        ser.write(str('G3')) # Convert the decimal number to ASCII then send it to the Arduino
    elif val in range(207,233):
        conn.sendall(b'A3')
        ser.write(str('A3')) # Convert the decimal number to ASCII then send it to the Arduino
    elif val in range(233,250):
        conn.sendall(b'B3')
        ser.write(str('B3'))
    elif val in range(250,277):
        conn.sendall(b'C4')
        ser.write(str('C4'))
    elif val in range(277,311):
        conn.sendall(b'D4')
        ser.write(str('D4'))
    elif val in range(311,339):
        conn.sendall(b'E4')
        ser.write(str('E4'))
    elif val in range(339,369):
        conn.sendall(b'E4')
        ser.write(str('E4'))


    counter +=1
    sleep(.1) # Delay for one tenth of a second
    if counter == 255:
        counter = 32


server.close()

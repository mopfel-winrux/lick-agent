import serial
import adafruit_thermal_printer
import socket
import os, os.path
import subprocess
import time
from collections import deque    


serial_name = "/dev/ttyUSB0"
baudrate=19200


sock_name = '/rumors/uart'
pier_path = '/home/amadeo/learn_hoon/tasseg-sophec-mopfel-winrux/'
vere_path = '/home/amadeo/learn_hoon/urbit-test'

sock_path = pier_path+'.urb/dev/'+sock_name


uart = serial.Serial(serial_name, baudrate=baudrate, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
printer = ThermalPrinter(uart)

#printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
#printer.size = adafruit_thermal_printer.SIZE_MEDIUM
#printer.justify = adafruit_thermal_printer.JUSTIFY_CENTER

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(sock_path)

while True:
    data = sock.recv(1024*2)
    print(data)
    p = subprocess.Popen([vere_path, 'eval' ,'-cn', '--loom' ,'25'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate(input=data)
    mark = stdout_data.decode().split(' ')[0][1:]
    noun = stdout_data.decode().split(' ')[1:]
    noun = ' '.join(noun)[:-2]

    if(mark=="%print"):
        print(mark)
        if(noun.startswith('0x')):
            print('hex')
            s= noun[2:]
            x = len(s)%4
            s = '0'*x +s
            test = '.'.join(s[i:i+4] for i in range(0, len(s), 4))
            test = test[x:]


            noun = bytes(f'`@ta`0x{test}', 'utf-8')
            print(noun)
            p = subprocess.Popen([vere_path, 'eval' , '--loom' ,'25'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            noun, junk = p.communicate(input=noun)
            noun=noun.decode()


        printer.print(noun)
        printer.feed(2)

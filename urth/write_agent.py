import socket
import os, os.path
import subprocess
import time
from collections import deque    

sock_name = 'uart'
pier_path = '/home/amadeo/learn_hoon/zod/'
vere_path = '/home/amadeo/learn_hoon/urbit-test'

sock_path = pier_path+'.urb/dev/'+sock_name

print(sock_path)


sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(sock_path)

while True:
    data = input("Send hoon to uart: ")
    print(data)
    p = subprocess.Popen([vere_path, 'eval' ,'-jn', '--loom' ,'25'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate(input=data.encode())

    print(stdout_data)
    sock.send(stdout_data)

sock.close()

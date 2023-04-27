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
    data = sock.recv(1024)
    print(data)
    p = subprocess.Popen([vere_path, 'eval' ,'-cn', '--loom' ,'25'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate(input=data)
    mark = stdout_data.decode().split(' ')[0][1:]
    noun = stdout_data.decode().split(' ')[1:]
    noun = ' '.join(noun)[:-2]
    print(f"stdout: {stdout_data}")
    print(f"mark: {mark}")
    print(f"noun: {noun}")



#data = bytes.fromhex('0e00000001003b9e34b932ba41e0632b7b630003');
#print(data)
#sock.send(data)

sock.close()

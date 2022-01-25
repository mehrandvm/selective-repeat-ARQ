# Receiver.py
import time, socket, sys
import random

print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = ip
name = "receiver"
port = 1234
print("Trying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s_name = s.recv(1024)
s_name = s_name.decode()

print(s_name, "has joined the chat room\n")

while True:

    k=s.recv(1024)
    k=k.decode()
    k=int(k)
    # print('k', k)
    i=0
    a=[]
    b=""
    message=""
    while i!=k:
       index = s.recv(1024)
       index = index.decode()
       index=int(index)
       message = s.recv(1024)
       message = message.decode()
       f=random.randint(0,4)
       if(f==0):
          b="ACK Lost"
          s.send(b.encode())
         
       else:
          b="ACK "+str(index)
          # print("byte received: ", message)
          s.send(b.encode())
          a.insert(index, message)
          i=i+1
          
       
    print("The a message received is :", a)
   

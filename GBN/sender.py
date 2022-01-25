# Sender.py
from cmath import log
from operator import sub
import time, socket, sys

def decimalToBinary(n):  
    return n.replace("0b", "")

def binarycode(s):
    a_byte_array = bytearray(s, "utf8")

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(decimalToBinary(binary_representation))

    #print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = "sender"
           
s.listen(1)
print("Waiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

print("connected to the receiver\nEnter x to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Enter Message: "))
    if message == "x":
        message = "connection closed!"
        conn.send(message.encode())
        print("\n")
        break
    message=binarycode(message)
    print("binary message is: ", message)
    f=str(len(message))
    conn.send(f.encode())
   
    i=0
    j=int(input("Enter the window size -> "))
    
   
    b=""
   
    j=j-1
    f=int(f)
    k=j

    while i!=f:
        substring = message[i:i+(j+1)]
        # print('substring',substring)
        for x in substring:  
            conn.send(x.encode())
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(0.1)
                print("Acknowledgement Received! The sliding window is in the range "+(str(i+1))+" to "+str(k+1)+" Now sending the next packet")
                i=i+1
                k=k+1
                time.sleep(0.1)
            else:
                time.sleep(0.1)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k+1)+" Now Resending the same packet")
                time.sleep(0.1)
                break
            
     

from os import system
import socket as soc
from tqdm import tqdm 
import time

_ = system('clear')
print ("\n Booting Up the Client App ... ")
for i in tqdm (range (100),
               desc="Loading…",
               ascii=False, ncols=75):
    time.sleep(0.02)

print(" Complete !!!")

HOST = '192.168.14.10'	# Host Address ( SERVER )
PORT = 4828		# Port Number

print ("\n Connect to the server port .... ")
_ = system('clear')

with soc.socket(soc.AF_INET, soc.SOCK_STREAM) as s:
	s.connect((HOST, PORT))			# Make a connection with server
	s.sendall(b'Yow Mother Fucker')	# Sent Data in Byte to Server
	data = s.recv(2000)			# Receive Data

print(' Received , ' + data.decode("utf-8"))	# Print out what inside data

#_= system('clear')

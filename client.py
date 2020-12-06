#from os import system
import socket as soc

HOST = '192.168.14.10'	# Host Address ( SERVER )
PORT = 37		# Port Number 

with soc.socket(soc.AF_INET, soc.SOCK_STREAM) as s:
	s.connect((HOST, PORT))			# Make a connection with server
	s.sendall(b'Yow Mother Fucker')	# Sent Data in Byte to Server
	data = s.recv(2000)			# Receive Data

print(' Received , ' + data.decode("utf-8"))	# Print out what inside data

#_= system('clear')

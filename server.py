import socket as Soc
import datetime

HOST = '192.168.14.10'  # Host Address
PORT = 4437               # Port Number

with Soc.socket(Soc.AF_INET, Soc.SOCK_STREAM) as serv:
        serv.bind((HOST, PORT))         # Binding
        serv.listen()                   # Listen how many device
        con, addr = serv.accept()       # Accept Client Con= IP , addr=random a>
        with con:
                print(' Connected by ',addr)
                while True:
                        data = con.recv(2000)   # Recv Data but in Byte
                        if not data:
                                break           # Error when data = null
                        con.sendall(data)       # Send Msg to client in Byte

		choice = con.recv(1024)
		choice = choice.decode()

		msg = datetime.datetime.now()	#Get Date And Time
		con.send(msg.encode())

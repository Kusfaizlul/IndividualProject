import sys
import time
import socket as Soc
import datetime
import pytz
from datetime import date
from os import system

def animation(msg):
        for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)


HOST = ''               # Host Address
PORT = 4828             # Port Number

with Soc.socket(Soc.AF_INET, Soc.SOCK_STREAM) as serv:
        serv.bind((HOST, PORT))         # Binding
        serv.listen()                   # Listen how many device

        _ = system('clear')
        opening = "\n \t\t\t\t  Waiting for connection ......... "
        animation(opening)

        con, addr = serv.accept()       # Accept Client Con= IP , addr=random a>
        with con:
                print('\n Connected by ',addr)
                menu = 1
                while True:
                        if menu == 1:
                                Cur_Time = datetime.datetime.now()              #Get Date And Time
                                Cur_Date = date.today()

                                Date = Cur_Date.strftime("%d/%m/%Y")            #dd/mm/yyyy
                                hrs = Cur_Time.hour
                                mnt = Cur_Time.minute
                                sec = Cur_Time.second

                                print (Date)
                                print (hrs)
                                print (mnt)
                                print (sec)

                                con.send(str(Date).encode())
                                con.send(str(hrs).encode())
                                con.send(str(mnt).encode())
                                con.send(str(sec).encode())

                                menu = 0

                                ch = con.recv(1024).decode()

                        if ch == '1':
                                i = '1'
                                while int(i) == 1:
                                        tz = con.recv(1024).decode()

                                        if tz == '1':
                                                tz_NY  = pytz.timezone('America/New_york')
                                                Tm_NY = datetime.datetime.now(tz_NY)
                                                time = Tm_NY.strftime('%H:%M:%S')
                                                con.send(str(time).encode())

                                        elif tz == '2':
                                                tz_L  = pytz.timezone('Europe/London')
                                                Tm_L = datetime.datetime.now(tz_L)
                                                time = Tm_NY.strftime('%H:%M:%S')
                                                con.send(str(time).encode())

                                        i = con.recv(1024).decode()
                                menu = 1

                        elif ch == '2':
                                #aboutus
                                menu = 1

                        else:
                                menu = 1

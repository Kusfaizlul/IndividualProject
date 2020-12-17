import sys
import time
import socket as Soc
import datetime
import pytz
from datetime import date
from os import system
from _thread import *

def animation(msg):
        for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)


def ping(msg):
        for char in msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)


def thread_client(con):
                menu = 1
                while True:
                        if menu == 1:
                                Cur_Time = datetime.datetime.now()              #Get Date And Time
                                Cur_Date = date.today()

                                Date = Cur_Date.strftime("%d/%m/%Y")            #dd/mm/yyyy
                                hrs = Cur_Time.strftime("%H")
                                mnt = Cur_Time.strftime("%M")
                                sec = Cur_Time.strftime("%S")

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
                        else:
                                menu = 1



HOST = ''               # Host Address
PORT = 4828             # Port Number

with Soc.socket(Soc.AF_INET, Soc.SOCK_STREAM) as serv:
        serv.bind((HOST, PORT))         # Binding
        serv.listen(5)                  # Listen how many device

        _ = system('clear')
        opening = "\n \t\t\t          Waiting for connection ......... "
        animation(opening)

        ThreatC = 0
        Laddr = []

        while True:
                client, addr = serv.accept()       # Accept Client Con= IP , addr=random
                Laddr.append(addr)

                numb = 1
                print ("\n\n\n\n\t\t\t\t\t Connection list")
                print ("\t\t\t\t ------------------------------")
                for x in Laddr:
                        msg = "\n\t\t\t\t " + str(numb) + ". "  + str(x)
                        ping(msg)
                        numb += 1
                print ("\n")
                start_new_thread(thread_client, (client, ))
                ThreatC += 1
                if ThreatC > 1:
                        msg = "\n\t\t\t\t Multi thread Mode is enable !! \n"
                        animation(msg)

                Thread = '\n\t\t\t\t Thread Number : ' +str(ThreatC)
                animation(Thread)

        Soc.close()



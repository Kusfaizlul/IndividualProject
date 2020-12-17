from os import system
import socket as soc
from tqdm import tqdm
import time
import sys

_ = system('clear')

print ("\n\t\t\t\t\t Booting Up the Client App ... \n")
for i in tqdm (range (100),
               desc="\t\t Loading…",
               ascii=False, ncols=75):
    time.sleep(0.02)

print(" Complete !!!")

def opening():
        Date = s.recv(10).decode()
        Hrs = s.recv(2).decode()
        Mnt = s.recv(2).decode()
        Sec = s.recv(2).decode()

        print ("\n\t\t           MAIN MENU WITH DATE AND TIME                 ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |\t    Date          |\t   "+ str(Date) +"       |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |\t    Hour          |\t       " + str(Hrs) + "           |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |\t   Minute         |\t       " + str(Mnt) + "           |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |\t   Second         |\t       " + str(Sec) + "           |  ")
        print ("\t\t ----------------------------------------------------  ")

        print ("\n\t\t\t    Please make your selction :")
        print ("\t\t\t    1. Time zone another country ")
        print ("\t\t\t    2. About Us")
        print ("\t\t\t    99. Exit")

def timezone():
        print ("\n\t\t                      TIME ZONE                        ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |\t \t1. America/New York                 |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |\t \t 2. Europe/London                   |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |\t \t  9. Main Menu                      |  ")
        print ("\t\t ----------------------------------------------------  ")
        pilihan = input("\n\t\t\t    Please make your selction : ")

        return pilihan

def aboutus():
        print ("\n\t\t                      ABOUT ME                         ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t | Name         |  Kusfaizlulfakhrullah Kusmawi     |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t | Student ID   |           2020985791              |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t | Github       |  https://github.com/Kusfaizlul    |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t | Linkedin     |      Kusfaizlul Fakhrullah        |  ")
        print ("\t\t ----------------------------------------------------  ")
        print ("\t\t |          This is Time Protocol Project           |  ")
        print ("\t\t |   Which is all about the Time Protocol Process   |  ")
        print ("\t\t ----------------------------------------------------  ")


HOST = '192.168.14.10'  # Host Address ( SERVER )
PORT = 4828             # Port Number

s = soc.socket()
s.connect((HOST,PORT))

print ("\n Connect to the server port .... ")
_ = system('clear')

while True:

        opening()
        choice = input("\t\t\t    Enter Your selection : ")

        s.send(choice.encode())

        if choice == '1':
                loop = 1

                while loop == 1:
                        _ = system('clear')
                        time = timezone()

                        s.send(time.encode())
                        if time == '1': # America / New York Time zone
                                temp = s.recv(1024)
                                print ("\n\t\t\t    Time in the New york : " + temp.decode())
                                input("\n\t\t\t    Press Enter to proceed .....")
                                _ = system('clear')


                        elif time == '2': # Europe / London
                                temp = s.recv(1024)
                                print ("\n\t\t\t    Time in the London   : " + temp.decode())
                                input("\n\t\t\t    Press Enter to proceed .....")
                                _ = system('clear')

                        elif time == '9':
                                loop = 0
                                input("\n\t\t    Press Enter to proceed to the main menu .....")
                                _ = system('clear')
                        else:
                                print ("\n\t\t\t   Invalid Input Please Try Again !! ")
                                input("\n\t\t\t    Press Enter to Proceed...")


                        s.send(str(loop).encode())

        elif choice == '2':
                _ = system('clear')
                aboutus()
                input("\n\t\t    Press Enter to proceed to the main menu .....")
                _ = system('clear')


        elif choice == '99':
                sys.exit("\t\t\t    Exiting the Program ... \n\n\n\n")

        else :
                print ("\n\t\t\t    Please Try Again !! ")
                input("\t\t\t    Press Enter to continue...")
                _ = system('clear')

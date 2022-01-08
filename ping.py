# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:51:29 2022

@author: Robinson Enedino
"""
import time
import os

#pasta = ".\\" 



def loopPing():
    # Open ip_list.txt file
    with  open( "ip_list.txt") as file:
        dump = file.read()
        dump = dump.splitlines()
        #print(dump)
    
    
    print("______________________________________________")
    # Ping for each ip address
    for ip in dump:
        res = os.popen(f"ping {ip} ").read()
        achouFalha = False
        strFalhaPing = ["Falha", "Host", "Request"]
        for palavra in strFalhaPing:
            if palavra in res:
                achouFalha = True
        
        if achouFalha:
            horario = time.strftime("%Y%m%d %H:%M %Ss ")
            f = open( "down_output.txt", "a")
            f.write(str(ip) + "\t is down " + horario  + "########" + "\n")
            print(str(ip) + "\t is down "  + horario + "########")
            f.close()
        else:
            horario = time.strftime("%Y%m%d %H:%M %Ss ")
            print(str(ip) + "\t is up " + horario)

while True:
        loopPing()
    
# -- network scanning and mapping tool --
# -- author : Ronin --

import subprocess 
from socket import *
import socket
import sys
import time
import timeit
import os
from pathlib import Path

def checkHost(host, mode, scanFile):
    cmd = "ping -c 1 " + host
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output  = output.communicate()[0]
    check = bytes("bytes from", "utf-8")
    scanFile = scanFile
    string1 = f"[ + LIVE + ] : {host}"
    if check in output and mode == "-o":
        file = open(scanFile, "a")
        file.write(string1 + "\n")
    elif mode == "-n" and scanFile == "n" and check in output:
        print(string1)

def checkPorts(host, portRange, scanFile, mode):
    portRange = int(portRange)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(1, portRange):
        sock.settimeout(20)
        result = sock.connect_ex((host, port))
        string = f"Port {port} : open"
        if mode == "-o" and result == 0:
            file = open(scanFile, "a")
            file.write(string + "\n")
        elif mode == "-n" and scanFile == "n" and result == 0:
                print(string)
                
def main():

    option = sys.argv[1]
    
    if option == "-hosts":
        fileWrite = sys.argv[2]
        fileName = sys.argv[3]
        if fileWrite == "-o":
            exists = Path(fileName)
            if exists.is_file():
                print("File already exists")
            else:
                print("Scanning for hosts...")
                for i in range(1, 26):
                    scanFile = fileName
                    mode = fileWrite
                    host = "192.168.1." + str(i)
                    checkHost(host, mode, scanFile)
        elif fileWrite == "-n" and fileName == "n":
            print("Scanning for hosts...")
            for i in range(1, 26):
                scanFile = fileName
                mode = fileWrite
                host = "192.168.1." + str(i)
                checkHost(host, mode, scanFile)
            
    if option == "--open":
        fileWrite = sys.argv[4]
        fileName = sys.argv[5]
        host = sys.argv[2]
        pRange = sys.argv[3]
        if fileWrite == "-o":
            exists = Path(fileName)
            if exists.is_file():
                print("File already exists")
            else:
                print("Scanning ports...")
                scanFile = fileName
                mode = fileWrite
                addr = host
                pRage = int(pRange)
                checkPorts(addr, pRange, scanFile, mode) 
        elif fileWrite == "-n" and fileName == "n":
            print("Scanning ports...")
            scanFile = fileName
            mode = fileWrite
            host = host
            pRange = int(pRange)
            checkPorts(host, pRange, scanFile, mode)

if __name__ == "__main__":
    main()

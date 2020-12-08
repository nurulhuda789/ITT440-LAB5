import socket
import sys
import json

s=socket.socket()
ip='192.168.43.81'
port=8080
fileName = input("File name: ")
file = open(fileName,'r')
sendData = json.dumps(fileName+"\n"+file.read())

s.connect((ip,port))
s.sendaall(bytes(sendData.encoding="utf-8"))

data = s.recv(1024)
print(data)

s.close()
file.close()

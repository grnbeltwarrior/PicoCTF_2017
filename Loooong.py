#! /usr/bin/python3
'''
  Automating the receive, sending and receiving from the loooong challenge. Possible to do without but learning is learning.
'''
import socket

def tcpConnect(ip, port):
        #Building the TCP socket.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        data = s.recv(1024).decode()
        print(data)

        #Parsing the data received.
        split = data.split("'")
        letter = split[1]
        times = split[3]
        single = split[5]
        
        #Build the string to send back.
        string = (str(letter) * int(times) + str(single) + "\n")
        
        #Sending the string.
        s.send(string.encode())
        
        #Receiving the flag in the response.
        data2 = s.recv(1024).decode()
        
        #Tear down the connection.
        s.close()
        print(data2)

#Get IP/system and port from user(me):
ip = input('Enter the IP or system name to connect to: ')
if ip is str:
        ip = socket.gethostbyname(ip)
port = input('Enter the Port to connect to: ')
port = int(port)

tcpConnect(ip, port)

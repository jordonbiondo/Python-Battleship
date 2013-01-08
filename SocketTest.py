import socket
import threading

host = ''
port = 50001
backlog = 5
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)
client, address = s.accept()


while 1:
    data = client.recv(size)
    if data:
        print data

        #if data:
        #     print "Got:", data
        #      client.send(data[::-1])
        


        

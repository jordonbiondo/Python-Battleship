import socket
import threading

host = '127.0.0.1'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
for i in range(100):
    s.send(raw_input())
    data = s.recv(size)
    print 'Received:', data

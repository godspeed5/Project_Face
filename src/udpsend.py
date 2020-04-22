import socket
UDP_IP = "192.168.1.6"
UDP_PORT = 8080
MESSAGE = "Hello, World!"
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
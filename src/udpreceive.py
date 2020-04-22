import socket
UDP_IP = "192.168.1.6"
UDP_PORT = 8080
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
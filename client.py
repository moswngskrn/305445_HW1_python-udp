import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "5"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

clientSocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
clientSocket.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data, server = clientSocket.recvfrom(1024)
print "fac("+MESSAGE+") =",data
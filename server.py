import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
def fac(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    else:
        return n*fac(n-1)
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "data:",data
    f = fac(int(data))
    sock.sendto(str(f),addr)

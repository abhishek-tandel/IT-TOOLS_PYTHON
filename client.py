import socket

# create a socket object

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name

host = socket.gethostname()
print host
port = 9999

# connection to hostname on the port.

s.connect((host, port))

# Recieve not more than 1024 bytes

msg = s.recv(1024)
s.close()
print msg.decade('ascii')

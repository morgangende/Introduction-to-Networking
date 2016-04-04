# Server program
import os
import sys
import socket

HOST = '' # Want the socket to be reachable by any address
PORT = int(sys.argv[1]) # Arbitrary non-reserved port

# Create and set-up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept() # Allow outside connections

print("Connected...")

# Receive the file size
conn.recv(4)

# Receive the file name and decode
byte_name = conn.recv(20)
filename = (byte_name.decode()).lstrip()

# Create the recv subdirectory if needed
if not os.path.exists('recv'):
    os.makedirs('recv')

# Receive the file data and write it to the new file
with open("recv/" + filename, 'wb') as file:
    byte = conn.recv(1)
    while byte:
        file.write(byte)
        byte = conn.recv(1)

conn.close() # Close the socket

print("Copy complete")

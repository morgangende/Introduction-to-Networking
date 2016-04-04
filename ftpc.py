# Client program
import os
import sys
import socket

HOST = str(sys.argv[1]) # IP address of the server
PORT = int(sys.argv[2]) # Port the server is using

# Create and set-up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Connected...")

filepath = str(sys.argv[3]) # The local file to be copied

# Encode the file size to 4 bytes
filesize = os.path.getsize(filepath)
byte_size = filesize.to_bytes(4, byteorder = 'little')

# Encode the file name to 20 bytes
filename = os.path.basename(filepath)
byte_name = filename.rjust(20).encode()

# Use the socket to send bytes
s.sendall(byte_size)
s.sendall(byte_name)

with open(filepath, 'rb') as file:
    byte = file.read(1)
    while byte:
        s.sendall(byte)
        byte = file.read(1)

s.close() # Close the socket

print("File sent")

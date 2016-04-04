CSE 3461 Lab 2
Morgan Gende
gende.1@osu.edu

Lab 2 copies a file from client to server and stores the file in subdirectory 'recv' on the server.  

*Sends the file size in a 4-byte packet, file name in a 20-byte backet, then sends bytes of the file in 1-byte packets over the network

*On server machine, run command 'python3 ftps.py <local-port>' where <local-port> is a non-reserved local port on the server

*On the client machine, run command 
'python3 ftpc.py <remote-IP> <remote-port> <local-file>' 
where <remote-IP> is the IP address of the server, <remote-port> is the previously selected port number on the server, and <local-file> is a local file that will be copied to the server

*This script was written for and tested on a Linux OS with Python 3 installed

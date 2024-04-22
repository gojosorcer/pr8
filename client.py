import socket

Server_ip = "localhost"
Server_host = 8002
FORMAT = "utf-8"
CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CS.connect((Server_ip, Server_host))

# Open the file in binary mode
with open(r"C:\\Users\\yashb\Downloads\\hello.txt", "rb") as file:
    data = file.read()

# Send the filename first
CS.send("hi.txt".encode(FORMAT))
msg = CS.recv(1024)
print(msg)


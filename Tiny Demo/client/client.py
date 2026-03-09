import socket

client = socket.socket()

client.connect(("localhost", 5000))

client.send("Hello Server".encode())

data = client.recv(1024)
print("Server says:", data.decode())

client.close()
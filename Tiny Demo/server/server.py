import socket  #used for network communication.

server = socket.socket()


server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server .accept()
print("Connected to:", addr)

data = conn.recv(1024)
print("Client says:", data.decode())

conn.send("Hello Client".encode())
conn.close()

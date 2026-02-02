import socket

server = socket.socket()
server.bind(('localhost', 12345))
server.listen(1)

print("Server waiting for connection...")
conn, addr = server.accept()
print("Connected to:", addr)

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'exit':
        break
    print("Client:", msg)
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
import socket

SERVER_HOST = ('127.0.0.1', 5000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_HOST)
server_socket.listen(5)

print(f"[SERVER] Listen on {SERVER_HOST[0]}:{SERVER_HOST[1]}")

message = """
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<html>
<body>
    <h1>Hello world</h1>
</body>
</html>
"""

while True:
    try:
        connection, client_address = server_socket.accept()
        print(f"[SERVER] Client Connected: {client_address}")
        connection.send(message.encode("UTF-8"))
        #connection.close()

    except KeyboardInterrupt:
        break

print("[SERVER] Stoped!")
server_socket.close()

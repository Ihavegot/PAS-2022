import socket

HOST = '127.0.0.1'
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"Server running on {HOST}:{PORT}")
    clientSocket, addr = s.accept()

    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        print(f"RECEVED: {data.decode('utf-8')}")

        clientSocket.sendall(data)

import socket

HOST = '127.0.0.1'
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Server running on {HOST}:{PORT}")

    while True:
        data, client = s.recvfrom(1024)
        print(f'Received: {data.decode("utf-8")}')

        s.sendto(str(socket.gethostbyaddr(data.decode("utf-8"))).encode(), client)

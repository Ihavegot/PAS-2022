import socket

HOST = '127.0.0.1'
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Server running on {HOST}:{PORT}")

    while True:
        data, client = s.recvfrom(1024)

        if len(data.decode('utf-8')) > 20:
            rcv = bytes(data.decode('utf-8')[:20], 'UTF-8')
            print(rcv.decode('utf-8'))
            s.sendto(str(len(rcv.decode('utf-8'))).encode(), client)
        else:
            rcv = bytes("{:<20}".format(data.decode('utf-8')), 'UTF-8')
            print(rcv.decode('utf-8'))
            s.sendto(str(len(rcv.decode('utf-8'))).encode(), client)

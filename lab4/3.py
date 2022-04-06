import socket

HOST = '212.182.24.236'
PORT = 2913

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(1)
    for i in range(666, 65535, 1000):
        s.sendto("PING".encode("UTF-8"), (HOST, i))
        try:
            data, address = s.recvfrom(4096)
            print(data.decode("UTF-8"))
            if data == "PONG":
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                    soc.connect((HOST, PORT))
                    receive = soc.recv(1024).decode("UTF-8")
                    print(receive)
        except Exception:
            print("Nothing on port " + str(i))

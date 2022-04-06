import socket


HOST = '127.0.0.1'
PORT = 2912

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        number = int(input("Type a Number: "))
        s.send(str(number).encode("UTF-8"))
        data = s.recv(1024).decode("UTF-8")
        print(data)
        if data == "You won! This is the right number!":
            break

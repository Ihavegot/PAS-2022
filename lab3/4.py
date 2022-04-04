import socket

HOST = '127.0.0.1'
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Server running on {HOST}:{PORT}")

    while True:
        numberone, clientone = s.recvfrom(1024)
        print(f'1. {numberone.decode("utf-8")}')

        sign, clienttwo = s.recvfrom(1024)
        print(f'2. {sign.decode("utf-8")}')

        numbertwo, clientthree = s.recvfrom(1024)
        print(f'3. {numbertwo.decode("utf-8")}')

        if sign.decode('utf-8') == '+':
            answer = int(numberone) + int(numbertwo)
            s.sendto(str(answer).encode('utf-8'), clientthree)

        elif sign.decode('utf-8') == '-':
            answer = int(numberone) - int(numbertwo)
            s.sendto(str(answer).encode('utf-8'), clientthree)

        elif sign.decode('utf-8') == '*':
            answer = int(numberone) * int(numbertwo)
            s.sendto(str(answer).encode('utf-8'), clientthree)

        elif sign.decode('utf-8') == '/':
            answer = int(numberone) / int(numbertwo)
            s.sendto(str(answer).encode('utf-8'), clientthree)
        else:
            answer = "Wrong operator"
            s.sendto(answer.encode('utf-8'), clientthree)


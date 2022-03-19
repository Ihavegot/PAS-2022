import socket

if __name__ == '__main__':
    host = '212.182.24.236'
    port = 2908
    mess = 'test message'

    if len(mess) > 20:
        messSend = mess[:20]
    else:
        messSend = "{:<20}".format(mess)

    bytesToSend = bytes(mess, 'utf-8')
    sendBytes = 0
    amountOfbytes = len(bytes(mess, 'utf-8'))
    recvData = ''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        if s.connect_ex((host, port)) == 0:
            print('Connected')
            while sendBytes != amountOfbytes:
                sendBytes += s.send(bytesToSend)

            while len(recvData) != amountOfbytes:
                recvData += s.recv(1024).decode()

            print(f'Answer: {recvData}')
        else:
            print('Connection error')

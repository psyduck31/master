import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 9090))


message = input('Введите что-нибудь: \n')
sock.send(message.encode())


print(sock.recv(1024).decode())


sock.close()
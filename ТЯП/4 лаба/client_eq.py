import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
user_message = input('Введите значения через пробел \n')


sock.send(user_message.encode())


print(sock.recv(1024).decode())
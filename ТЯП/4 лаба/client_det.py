import socket


user_message = ''
sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
for i in range(0,3):
	user_message += input(f'Введите {i+1}-ю строку: ') + ' '
sock.send(user_message.encode())


data = sock.recv(1024)
print(data.decode())


sock.close()
import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 9090))


while True:
	user_message = input('Вы: ')
	sock.send(user_message.encode())
	if user_message.upper() == "STOP":
		break
	answer = sock.recv(1024).decode()
	print("Сервер: ", answer)

sock.close()
import socket


sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()
last_message = 'Поступившего ранее сообщения не было'

while True:
	message = conn.recv(1024).decode()
	if message.upper() == "STOP":
		sock.close()
		break
	conn.send(last_message.encode())
	last_message = message
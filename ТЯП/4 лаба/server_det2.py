import socket


def det(data):
	return data[0] * data[3] - data[1] * data[2]


sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()


data = conn.recv(1024).decode().strip().split(' ')
data = [int(x) for x in data]
data = [x * det(data) for x in data]


conn.send(str(data).encode())


sock.close()
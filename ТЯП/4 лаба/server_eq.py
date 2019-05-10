import socket


def solver(data):
	a, b, c, k = data[0], data[1], data[2], data[3]
	if b == 0 or a == 0 or (a + b + c * (k - a / b**3)) == 0:
		return "Деление на ноль невозможно :("
	else:
		return abs((a**2 / b**2 + c**2 * a**2)/(a + b + c * (k - a / b**3)) + c + c * (k/b - k/a))


sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()


data = conn.recv(1024).decode().strip().split(' ')
data = [int(x) for x in data]


answer = str(solver(data))
conn.send(answer.encode())
sock.close()
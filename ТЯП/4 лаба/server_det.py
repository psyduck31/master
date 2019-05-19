import socket


def det(data):
	return (data[0] * (data[4] * data[8] - data[5] * data[7]) - 
		data[1] * (data[3] * data[8] - data[5] * data[6]) + 
		data[2] * (data[3] * data[7] - data[6] * data[4]))


sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()


data = conn.recv(1024).decode().strip().split(' ')
data = [int(x) for x in data]

answer = str(det(data))
conn.send(answer.encode())


sock.close()

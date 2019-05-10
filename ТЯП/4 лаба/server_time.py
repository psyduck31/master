from time import localtime, strftime
import socket


sock = socket.socket()
sock.bind(('', 9090))
sock.listen()
conn, addr = sock.accept()

if len(conn.recv(1024)) > 0:
	conn.send(strftime("%d.%m.%Y %H:%M:%S", localtime()).encode())


sock.close()
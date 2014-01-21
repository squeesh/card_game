# client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    print(sock.recv(1024).decode('utf-8'))
    data = input('Command: ')
    sock.sendall(bytearray(data, 'utf-8'))
    print(sock.recv(1024).decode('utf-8'))
    if data == 'exit':
        break


sock.close()

# while True:

#     sock.sendall(b'Hello, world')
#     data = sock.recv(1024)

# sock.close()
# print('Received', repr(data))
# client program
import socket
import pickle

HOST = 'localhost'
PORT = 50007
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

input_data = bytearray()

while True:
    data = ''
    rcv_data = sock.recv(4096)

    if rcv_data:
        data_dict = pickle.loads(rcv_data)

        print(data_dict['data'])
        if data_dict['command'] == '1':

            while not data:
                data = input('Command: ')

            sock.sendall(bytearray(data, 'utf-8'))

        if data == 'exit':
            break


sock.close()

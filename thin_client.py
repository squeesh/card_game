# client program
import socket
import pickle
import settings

HOST = settings.REMOTE_HOST
PORT = settings.REMOTE_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

input_data = bytearray()

while True:
    data = ''
    rcv_data = sock.recv(4096)

    if rcv_data:
        data_dict = pickle.loads(rcv_data)

        # print(data_dict)
        print(data_dict['data'])
        if data_dict['command'] == '1':

            # while not data:
            data = input('Command: ')
            if not data:
                data = '\0'

            sock.sendall(bytearray(data, 'utf-8'))

        if data == 'exit' or data_dict['command'] == '2':
            break


sock.close()

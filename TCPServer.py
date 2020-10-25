import socket
import pickle

# Conexão.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.100.87', 80))

# Ouve até 5 conexões.
server.listen(5)

while True:
    conn, addr = server.accept()
    print(f'Client {addr} has connected.')
    while True:
        data = conn.recv(54169)
        if not data:
            break

        client_data = pickle.loads(data)
        server_data = client_data
        # Modifica o objeto.
        server_data["name"] = "Janette Doe"
        print(f'Got {client_data} from {addr}. \n New data: {server_data}.\n')
        # conn.send(str.encode(f'You have connected. Address: {addr}'))
        serialized_data = pickle.dumps(server_data)
        conn.send(serialized_data)
    conn.close()
    print(f'O cliente {addr} desconectou.')

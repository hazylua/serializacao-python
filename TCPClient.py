import socket
import pickle

# Conexão.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.100.87', 80))

# Objeto a ser enviado.
Object = {'name': "John Doe", "age": "30", "place": "Place"}

while True:
    # Comando (digitar "1") para enviar o objeto quando a conexão for estabelecida.
    command = input("Command: ")
    print()
    serialized_data = None

    # pickle.dumps() serializa o objeto, enquanto pickle.loads()"desserializa" para a leitura.

    if command == "1":
        serialized_data = pickle.dumps(Object)

    if command == "0":
        break

    # Se serialized_data não estiver vazio, enviar para o servidor. O cliente então recebe um objeto modificado.
    if serialized_data:
        client.send(serialized_data)
        data = client.recv(54169)
        server_data = pickle.loads(data)
        print(f'Got {server_data}.')
client.close()

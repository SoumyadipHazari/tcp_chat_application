import socket # it's a low level networking interface gives access to the BSD socket interface
import threading # it provides a way to run multiple threads concurrently within a single process. as for the tcp chat application there are operations of network requests that's why threading is used.

port = 8000
host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client = []

nickname = []

def live(message):
    for x in clinet:
        x.send(message)

def connection(x):
    while True:
        try:
            message = x.recv(1024)
            live(message)
        except:
            index = client.index(x)
            client.remove(x)
            x.close()
            nickname = y[index]
            live("{} left the chat." .format(y).encode('ascii'))
            nickname.remove(y)
            break

def get_message():
    while True:
        x, address = server.accept()
        print("Connected with {}" .format(str(address)))


        x.send('name'.encode('ascii'))
        y = x.recv(1024).decode(ascii)
        nickname.append(y)
        client.append(x)

        print("nickname {}" .format(y))
        live("{} is joined the chat." .format(y).encode('ascii'))
        client.send('Connected to the server.' .encode('ascii'))

        thread = threading.Thread(target = handle, args=(client,))
        thread.start()

    return get_message()

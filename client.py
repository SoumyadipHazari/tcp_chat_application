import socket
import threading

y = input("choose your username to chat: ")
x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x.connect(("127.0.0.1", 8000))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                x.send(y.encode('ascii'))
            else:
                print(message)
        except:
            print("Error occured")
            x.close()
            break


def write():
    while True:
        message = '{}: {}'.format(y, input(''))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target = receive)
receive_thread.start()


write_thread = threading.Thread(target=write)
write_thread.start()



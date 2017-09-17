import socket

def start():
    host = "127.0.0.1"
    port = 3050

    cli1 = socket.socket()
    cli1.connect((host,port))

    print("client started")

if __name__ == '__main__':
    start()
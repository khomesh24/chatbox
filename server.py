import socket

def start():
    host = "127.0.0.1"
    port = 3050

    mysocket = socket.socket()
    mysocket.bind((host,port))

    mysocket.listen(1)
    con, addr = mysocket.accept()
    print("connectition form "+ str(addr))


    print("server started")


if __name__ == '__main__':
    start()


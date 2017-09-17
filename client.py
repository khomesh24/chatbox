import socket

def start():
    host = "127.0.0.1"
    port = 3050

    cli1 = socket.socket()
    cli1.connect((host,port))

    msg = input("->")

    while msg != 'q':
        cli1.send(msg.encode());
        ser_msg = cli1.recv(1024).decode()
        print("form server: "+str(ser_msg))
        msg = input("->")

    cli1.close()


if __name__ == '__main__':
    start()
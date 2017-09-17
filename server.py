import socket

def start():
    host = "127.0.0.1"
    port = 3050

    mysocket = socket.socket()
    mysocket.bind((host,port))

    mysocket.listen(1)
    con, addr = mysocket.accept()
    print("connectition form "+ str(addr))
    while True:
        data = con.recv(1024).decode();
        if not data:
            break
        print("form client"+ str(data))
        msg = input("->")
        con.send(msg.encode())
    con.close()




if __name__ == '__main__':
    start()


import socket, pickle, threading

HEADSIZE = 10
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 6000))
server_socket.listen(2)

clients_snake = {}



HEADERSIZE=10

def thead_client(client):
    global Id
    client.send(bytes(str(Id), "utf-8"))
    while True:
        try:
            full_msg = ''
            new_msg = True
            while True:
                msg = client.recv(10)
                if new_msg:
                    print("new msg len:",msg[:HEADERSIZE])
                    msglen = int(msg[:HEADERSIZE])
                    new_msg = False

                print(f"full message length: {msglen}")

                full_msg += msg

                print(len(full_msg))
                if len(full_msg)-HEADERSIZE == msglen:
                    print("full msg recvd")
                    print(full_msg[HEADERSIZE:])
                    new_msg = True
                    break
            print(full_msg)
            us_full_msg=pickle.loads(full_msg[HEADERSIZE:])
            cid = us_full_msg[0]
            csnake = us_full_msg[1]
            clients_snake[cid] = csnake
            reply = pickle.dumps(clients_snake)
            if not full_msg:
                print("no data")
                client.send(str.encode("Goodbye"))
                print(client, "se fue")
                client.close()
                clients_snake.pop(cid)
                break
            else:
                print(f"Recieved: {full_msg} ")
            client.sendall(reply)
            print("sended: ", clients_snake)
        # catching a lot of errors can be produce into client server communication
        # when the connection isn`t readiable the server get out the client 
        except Exception as ea:
            print(f"causa: {ea}")
            break
   
            
Id = 1

while True:
    clientsocket, adr = server_socket.accept()
    Id += 1
    th = threading.Thread(target=thead_client, args=((clientsocket,)))
    th.start()

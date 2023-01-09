from cmath import pi
import socket, pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = 0

    def get_id(self):
        self.client.connect((socket.gethostname(), 6000))
        self.id = self.client.recv(1024).decode("utf-8")

    def send(self, data):
        try:
            self.client.send(data)
            reply =self.client.recv(2048)
            return reply
        except socket.error as e:
            return str(e)



    
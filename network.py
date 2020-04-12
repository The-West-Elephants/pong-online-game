from constants import *
from socket import *
from pickle import dumps, loads


class Network:
    def __init__(self, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(('192.168.1.59', port))

    def get_xpos(self):
        return int(self.socket.recv(1024).decode('utf-8'))

    def get_player_count(self):
        return int(self.socket.recv(1024).decode('utf-8'))

    def get_ball(self):
        self.socket.send(b'ball')
        return loads(self.socket.recv(1024))

    def send_paddle(self, paddle):
        self.socket.send(dumps(paddle))
        return loads(self.socket.recv(1024))

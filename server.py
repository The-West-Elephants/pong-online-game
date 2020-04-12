from constants import *
from paddle import Paddle
from ball import Ball
from random import randint
from socket import *
from pickle import dumps, loads


class Server:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        port = randint(1024, 9999)
        self.socket.bind(('192.168.1.59', port))
        print('The port is ' + str(port) + '!')
        self.socket.listen(2)
        client1, address1 = self.socket.accept()
        client2, address2 = self.socket.accept()
        client1.send(bytes(str(WINDOW_WIDTH - 100), 'utf-8'))
        client2.send(b'100')
        client1.send(bytes(str(1), 'utf-8'))
        client2.send(bytes(str(2), 'utf-8'))
        paddle1 = loads(client1.recv(1024))
        paddle2 = loads(client2.recv(1024))
        client1.send(dumps(paddle2))
        client2.send(dumps(paddle1))
        self.connection1 = [client1, paddle1, address1]
        self.connection2 = [client2, paddle2, address2]
        print(self.connection1[1].name + '@' + str(self.connection1[2][0]) + ' is connected.')
        print(self.connection2[1].name + '@' + str(self.connection2[2][0]) + ' is connected.')
        self.main()

    def main(self):
        ball = Ball()
        while True:
            ball.move(self.connection1[1], self.connection2[1])
            msg = self.connection1[0].recv(1024)
            if not msg:
                break
            if msg == b'ball':
                self.connection1[0].send(dumps(ball))
            else:
                self.connection1[0].send(dumps(self.connection2[1]))
                self.connection1[1] = loads(msg)
            msg = self.connection2[0].recv(1024)
            if not msg:
                break
            if msg == b'ball':
                self.connection2[0].send(dumps(ball))
            else:
                self.connection2[0].send(dumps(self.connection1[1]))
                self.connection2[1] = loads(msg)


if __name__ == '__main__':
    server = Server()

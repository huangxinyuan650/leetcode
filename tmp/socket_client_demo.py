# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/27 16:39
# File: socket_client_demo.py

import socket
import logging

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999
CLIENT_FLAG = True
logging.basicConfig(level='INFO')


def main():
    _client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _client.connect((SERVER_HOST, SERVER_PORT))
    _client.send(b'Hello World!!!')
    _count = 0
    while CLIENT_FLAG and _count < 10:
        logging.info('Getting response ....\n')
        logging.info(f'Message Content:\n{str(_client.recv(1024))}\nMessage End\n')
        _client.send(bytes(f'message {_count}\n', encoding='utf8'))
        _count += 1
    _client.sendall('End'.encode())
    _client.close()


if __name__ == '__main__':
    main()

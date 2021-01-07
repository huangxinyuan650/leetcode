# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/27 15:46
# File: socket_demo.py

import socket
import logging

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999
ACCEPT_FLAG = True
logging.basicConfig(level='INFO')


def main():
    try:
        logging.info('Begin Socket Create!!!')
        _server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        _server.bind((SERVER_HOST, SERVER_PORT))
        _server.listen()
        logging.info(f'Server Host ({SERVER_HOST}) is listening request on Port ({SERVER_PORT})......\n\n')
        while ACCEPT_FLAG:
            _conn, _addr = _server.accept()
            try:
                while True:
                    logging.info('Message Info Begin\n')
                    _msg = str(_conn.recv(1024), encoding="utf8")
                    logging.info(f'{_msg}')
                    logging.info('\nMessage Info End\n')
                    if _msg == 'End':
                        _conn.close()
                        break
                    _conn.send(bytes('Message has been received!!!\n', encoding='utf8'))
                    logging.info('Listening next message...\n')
            except Exception as client_e:
                logging.warning(f'End client{client_e}')
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()

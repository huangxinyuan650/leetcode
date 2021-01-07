# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/25 08:37
# File: multi_thread_demo.py

import requests
import uuid
from concurrent import futures


def down_one(file_name: str):
    """
    下载单个文件
    """
    _save_dir = '/Users/huangxinyuan/develop_my/leetcode/source'
    _header = {'User-Agent': 'wxx'}
    _response = requests.request(method='GET', url=f'http://127.0.0.1:2650/{file_name}', headers=_header)

    if _response.status_code == 200:
        with open(file=f'{_save_dir}/{uuid.uuid4()}{file_name}', mode='wb+') as f:
            f.write(_response.content)
        print('Success')
    else:
        print('Failed')


if __name__ == '__main__':
    _file_list = ['']
    down_one('1041604017847.jpg')

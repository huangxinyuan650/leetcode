# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/11/17 22:18
# File: cvs_mysql.py

import csv
import pymysql

# 本地csv文件的路径
_file_path = '/Users/huangxinyuan/Desktop/shell/rentinfodata.csv'

# 数据库连接信息
_db_info = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'database': 'my_csv',
    'table': 'my_csv'
}


def handle_csv():
    """
    处理csv文件并存入mysql
    """
    _conn = pymysql.connect(
        host=_db_info['host'],
        port=_db_info['port'],
        user=_db_info['user'],
        password=_db_info['passwd'])
    _cursor = _conn.cursor()

    # 创建数据库
    _cursor.execute(f'drop database if exists {_db_info["database"]};')
    _cursor.execute(f'create database {_db_info["database"]} default character set utf8;')
    _cursor.execute(f'use {_db_info["database"]};')

    with open(_file_path, 'r') as f:
        _reader = csv.reader(f)
        _header = None
        for _ in _reader:
            if not _header:
                _header = _
                _create_str = ''
                for _i in _:
                    _create_str += f'{_i}  varchar(40),'
                # 根据header的字段创建数据表
                _cursor.execute(f'create table {_db_info["table"]} ({_create_str[:-1]});')
                print(_header)
            elif len(_) == len(_header):
                _ = [f'"{__}"' for __ in _]
                # 一行行的插入数据，可修改成批量插入
                _insert_str = f'insert into {_db_info["table"]} ({",".join(_header)}) values({",".join(_)});'
                _cursor.execute(_insert_str)
                print(_)
    _conn.commit()
    _cursor.close()


if __name__ == '__main__':
    handle_csv()

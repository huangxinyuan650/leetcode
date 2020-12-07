# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/11/18 21:16
# File: convert.py

if __name__ == '__main__':
    with open('/Users/huangxinyuan/Desktop/shell/rentinfodata.txt', 'r') as f:

        with open('/Users/huangxinyuan/Desktop/shell/rentinfodata.csv', 'w') as n_f:
            _lines = f.readlines()
            for _ in _lines:
                _array = _.split('\t')
                n_f.write(f'{_array[0]},{_array[1]}')
            n_f.close()
        f.close()

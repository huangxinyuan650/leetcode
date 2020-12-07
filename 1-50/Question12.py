# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/11/29 10:47
# File: Question12.py
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        从打到小除余取整，对余数继续
        注意增加I、X、C
        """
        _re_str = ''
        _map_list = [
            {'key': 'M', 'value': 1000},
            {'key': 'CM', 'value': 900},
            {'key': 'D', 'value': 500},
            {'key': 'CD', 'value': 400},
            {'key': 'C', 'value': 100},
            {'key': 'XC', 'value': 90},
            {'key': 'L', 'value': 50},
            {'key': 'XL', 'value': 40},
            {'key': 'X', 'value': 10},
            {'key': 'IX', 'value': 9},
            {'key': 'V', 'value': 5},
            {'key': 'IV', 'value': 4},
            {'key': 'I', 'value': 1}]
        _s_l = ['I', 'X', 'C']
        for _ in _map_list:
            _c = num // _['value']
            num = num % _['value']
            # _n_l = len(str(_['value']))
            # _l = (_n_l - (2 if str(_['value'])[0] == '1' else 1)) if _n_l > 1 else 0
            # if _['value'] != 1:
            #     _d = num // (_['value'] - 10 ** _l)
            #     num = num % (_['value'] - 10 ** _l)
            # else:
            #     _d = 0
            # _re_str += _['key'] * _c + (_s_l[_l] + _['key']) * _d
            _re_str += _['key'] * _c
        return _re_str


if __name__ == '__main__':
    _s = Solution()
    print(_s.intToRoman(40))

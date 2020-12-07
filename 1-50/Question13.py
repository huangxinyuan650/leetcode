# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/6 10:04
# File: Question13.py
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        罗马数转阿拉伯数

        左右开始读取皆可
        """
        _v_map = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'L': 50,
            'XC': 90,
            'C': 100,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        _l = len(s)
        _total = 0
        for _, _v in enumerate(s):
            if _ < _l - 1 and _v_map[_v] < _v_map[s[_ + 1]]:
                _total -= _v_map[_v]
            else:
                _total += _v_map[_v]
        return _total


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('LVIII'))

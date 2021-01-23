# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2021/1/23 22:06
# File: Question17.py
class Solution:
    def letterCombinations(self, digits: str) -> list:
        """

        """
        _map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def merge(sub_str):
            if len(sub_str) == 0:
                return []
            elif len(sub_str) == 1:
                return _map[sub_str]
            return [f'{_}{_sub}' for _ in _map[sub_str[0]] for _sub in merge(sub_str[1:])]

        return merge(digits)


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))

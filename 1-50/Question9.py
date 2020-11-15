# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/11/8 18:00
# File: Question9.py

class Solution:
    def isPalindrome(self, x: int) -> bool:
        _x_str = str(x)
        for _ in range(len(_x_str)//2):
            if _x_str[_] != _x_str[-(_+1)]:
                return False
        return True

if __name__ == '__main__':
    _s = Solution()
    print(_s.isPalindrome(-121))
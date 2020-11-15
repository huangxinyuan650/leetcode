# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/11/9 22:45
# File: Question11.py


class Solution:
    def maxArea(self, height: list):
        def max(x, y):
            return x if x > y else y

        _max = 0
        _i, _j = 0, len(height) - 1
        while _i < _j:
            if height[_i] < height[_j]:
                _h = height[_i]
                _i += 1
            else:
                _h = height[_j]
                _j -= 1
            _max = max(_max, _h * (_j - _i + 1))

        return _max


if __name__ == '__main__':
    _s = Solution()
    _s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])

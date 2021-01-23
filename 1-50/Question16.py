# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2021/1/23 18:03
# File: Question16.py
class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        """
        将元素排序
        _i_a [0:_l-2]
        _i_b [1:_l-1]
        _i_c target-nums[_i_a]-nums[_i_b]
        """
        nums.sort()
        _l = len(nums)
        _i_a = 0
        _total = 3 * 10 ** 3 + 10 ** 4
        while _i_a < _l - 2:
            _i_b = _i_a + 1
            _i_c = _l - 1
            while _i_b < _i_c:
                _tmp = nums[_i_a] + nums[_i_b] + nums[_i_c] - target
                if _tmp == 0:
                    return target
                elif _tmp < 0:
                    _i_b += 1
                else:
                    _i_c -= 1
                if abs(_tmp) < abs(_total):
                    _total = _tmp
            _i_a += 1
        return _total + target


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest(nums=[-1, 2, 1, -4], target=1))

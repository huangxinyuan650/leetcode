# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2021/1/23 22:42
# File: Question18.py
class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        """
        _i_a [0:_l-4]
        _i_b [1:_l-3]
        _i_c [2:_l-2]
        _i_d [3:_l-1][::-1]
        """
        nums.sort()
        _l = len(nums)
        _i_a = 0
        _re_list = []
        while _i_a < _l - 3:
            if target < 0 and 4 * nums[_i_a] > target:
                break
            if _i_a > 0 and nums[_i_a] == nums[_i_a - 1]:
                _i_a += 1
                continue
            _i_b = _i_a + 1
            while _i_b < _l - 2:
                if _i_b > _i_a + 1 and nums[_i_b] == nums[_i_b - 1]:
                    _i_b += 1
                    continue
                _i_c = _i_b + 1
                _i_d = _l - 1
                while _i_c < _i_d:
                    if target > 0 and 4 * nums[_i_d] < target:
                        break
                    # 去重
                    if _i_c > _i_b + 1 and nums[_i_c] == nums[_i_c - 1]:
                        _i_c += 1
                        continue
                    if _i_d < _l - 1 and nums[_i_d] == nums[_i_d + 1]:
                        _i_d -= 1
                        continue
                    _tmp = nums[_i_a] + nums[_i_b] + nums[_i_c] + nums[_i_d] - target
                    if _tmp == 0:
                        # 满足条件，将结果加入结果列表
                        _re_list.append([nums[_i_a], nums[_i_b], nums[_i_c], nums[_i_d]])
                        _i_c += 1
                        _i_d -= 1
                    elif _tmp > 0:
                        _i_d -= 1
                    else:
                        _i_c += 1
                _i_b += 1
            _i_a += 1
        return _re_list


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum(nums=[-2, -1, -1, 1, 1, 2, 2], target=0))

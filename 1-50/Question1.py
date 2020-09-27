# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 9/27/20 11:44 PM
# File: Question1.py


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        def v1(nums: list[int], target: int) -> list[int]:
            """
            暴力
            :param nums:
            :param target:
            :return:
            """
            _index_i = -1
            for _i in nums:
                _index_i += 1
                _aim = target - _i
                _index_j = _index_i
                for _j in nums[_index_i + 1:]:
                    _index_j += 1
                    if _j == _aim:
                        return [_index_i, _index_j]

        def v2(nums: list[int], target: int) -> list[int]:
            """
            Hash
            先把所有的值加到一个hash表，然后在直接从hash表中取结果
            :param nums:
            :param target:
            :return:
            """
            _hash_dict = {}
            for _index, _v in enumerate(nums):
                _hash_dict.setdefault(_v, []).append(_index)
            for _i, _value in enumerate(nums):
                if (target - _value) in _hash_dict.keys():
                    if (target - _value) != _value:
                        return [_i, _hash_dict[target - _value][0]]
                    elif len(_hash_dict[target - _value]) > 1:
                        return [_i, _hash_dict[target - _value][1]]

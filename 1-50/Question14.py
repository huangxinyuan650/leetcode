# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/6 10:29
# File: Question14.py
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        最长前缀

        暴力匹配
        """
        if not strs:
            return ''
        _min = len(strs[0])
        _m_str = strs[0]
        for _ in strs:
            if len(_) < _min:
                _min = len(_)
                _m_str = _

        for _, _v in enumerate(_m_str):
            for _i in strs:
                if _v != _i[_]:
                    return str(strs[0][:_])

        return _m_str


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(strs=["reflower", "flow", "flight"]))

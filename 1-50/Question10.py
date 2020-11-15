# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/11/8 19:27
# File: Question10.py

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        '.' 任意单个字符
        '*' 0个或多个前面的字符
        先读取p串，遇'.'判断下一个是否为'*'，若为'*'则返回True，否则s和p均往后移一位继续读p串，
        遇其他字符A1判断下一个是否为'*'，若为'*'则开始读取s串，当读取的值为非A1的字符时停止读s串
        """
        _i_p = 0
        _i_s = 0
        _l_s = len(s)
        _l_p = len(p)
        while _i_p < _l_p and _i_s < _l_s:
            if p[_i_p] == '.':
                if _i_p + 1 < _l_p and p[_i_p + 1] == '*':
                    _i_p += 1
                    if _i_p + 1 < _l_p:
                        while _i_s < _l_s:
                            if self.isMatch(s=s[_i_s:], p=p[_i_p + 1:]):
                                return True
                            _i_s += 1
                        return False
                    else:
                        return True
                else:
                    _i_p += 1
                    _i_s += 1
            else:
                if _i_p + 1 < _l_p and p[_i_p + 1] == '*':
                    _i_p += 1
                    if _i_p + 1 < _l_p:
                        while _i_s < _l_s and s[_i_s] == p[_i_p - 1]:
                            if self.isMatch(s=s[_i_s:], p=p[_i_p + 1:]):
                                return True
                            _i_s += 1
                    else:
                        return True
                elif s[_i_s] == p[_i_p]:
                    _i_p += 1
                    _i_s += 1
                else:
                    return False
        return True if _i_p == _l_p and _i_s == _l_s else False


if __name__ == '__main__':
    _s = Solution()
    print(_s.isMatch(s='aab', p='c*a*b'))

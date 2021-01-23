# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/11/8 19:27
# File: Question10.py

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        a* 可以匹配 ''、'a'、'a^n(n>1)'
        . 可以匹配任意字符
        """
        _l_p, _l_s = len(p), len(s)
        if _l_p > 0:
            if p[-1] == '*':
                if _l_p >= 2 and (_l_s == 0 or (_l_s >= 1 and p[-2] != '.' and p[-2] != s[-1])):
                    # 匹配空串 s为空串或者p[-2] != s[-1]
                    return self.isMatch(s, p[:-2])
                elif _l_p >= 2 and _l_s >= 1 and (p[-2] == s[-1] or p[-2] == '.'):
                    # 匹配去掉s串的单个字符或者匹配空串(即使p[-2]==s[-1])
                    if p[-2] == '.':
                        # .*可以匹配0或多个任意字符，即可以有多个.*
                        p1 = p[:_l_p - 2] + s[-1] + '*'  # 替换*为匹配字符
                        p2 = p + f'{s[-1]}*'  # 支持.*匹配不一样的串
                        return self.isMatch(s, p2) or self.isMatch(s, p1)
                    # 匹配去掉s最后一位和char*匹配空串
                    return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])
                return False
            elif _l_s > 0 and (p[-1] == '.' or p[-1] == s[-1]):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False
        else:
            return True if _l_s == 0 else False


if __name__ == '__main__':
    _s = Solution()
    print(_s.isMatch(s='ab', p='b.*'))

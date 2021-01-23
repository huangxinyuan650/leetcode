# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2021/1/23 23:52
# File: Question20.py
class Solution:
    def isValid(self, s: str) -> bool:
        """
        遇(、[、{入栈
        遇)、]、}出栈且需要匹配
        """
        _stack = []
        _map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for _ in s:
            if _ in ['(', '[', '{']:
                _stack.append(_)
            else:
                if len(_stack) > 0 and _map[_stack[-1]] == _:
                    _stack.pop()
                else:
                    return False
        return True if len(_stack) == 0 else False

# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2021/1/23 23:31
# File: Question19.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """

        """
        _stand_head = head
        _list = []
        while _stand_head:
            _list.append(_stand_head)
            _stand_head = _stand_head.next
        _l = len(_list)
        if _l - n - 1 >= 0:
            _list[_l - n - 1].next = _list[-n].next
        else:
            head = _list[-n].next
        return head

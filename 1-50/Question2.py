# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 10/9/20 10:16 PM
# File: Question2.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _r_l = _r_h = ListNode()
        _more = 0
        while l1 and l2:
            _r_l.next = ListNode(val=(l1.val + l2.val + _more) % 10)
            _more = (l1.val + l2.val + _more) // 10
            l1 = l1.next
            l2 = l2.next
            _r_l = _r_l.next
        _l = l1 or l2
        while _l:
            _r_l.next = ListNode(val=(_l.val + _more) % 10)
            _more = (_l.val + _more) // 10
            _l = _l.next
            _r_l = _r_l.next
        if _more:
            _r_l.next = ListNode(val=_more)
        return _r_h.next


if __name__ == '__main__':
    l1 = ListNode(val=9,
                  next=ListNode(val=9,
                                next=ListNode(val=9,
                                              next=ListNode(val=9,
                                                            next=ListNode(val=9,
                                                                          next=ListNode(val=9,
                                                                                        next=ListNode(val=9)))))))
    l2 = ListNode(val=9,
                  next=ListNode(val=9,
                                next=ListNode(val=9,
                                              next=ListNode(val=9))))
    _r = Solution().addTwoNumbers(l1, l2)
    print(_r)

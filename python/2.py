# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        h1 = l1
        h2 = l2
        add = None

        while h1 or h2:
            s = 0
            s += carry
            carry = 0

            if h1:
                s += h1.val
                h1 = h1.next

            if h2:
                s += h2.val
                h2 = h2.next

            carry = s // 10
            s = s % 10

            if add == None:
                add = ListNode(s, None)
                continue
            ta = add
            while ta:
                if ta.next == None:
                    ta.next = ListNode(s, None)
                    break
                ta = ta.next

        if carry != 0:
            ta = add
            while ta:
                if ta.next == None:
                    ta.next = ListNode(carry, None)
                    break
                ta = ta.next
        return add

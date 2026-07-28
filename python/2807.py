import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = head
        prev = None
        while True:
            prev = cur
            cur = cur.next

            if cur is None:
                return head

            x = ListNode(val=math.gcd(cur.val, prev.val), next=cur)
            prev.next = x

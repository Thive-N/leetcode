# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        node_to_remove = nodes[-n]
        if len(nodes) == 1:
            return None

        # at start
        elif len(nodes) == n:
            head = node_to_remove.next
        else:
            node_to_remove_prev = nodes[-n-1]
            node_to_remove_prev.next = node_to_remove.next

        return head

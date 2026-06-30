class Solution:
    def getIntersectionNode(self, A: ListNode, B: ListNode) -> ListNode:
        a, b = A, B
        
        while a != b:
            a = a.next if a else B
            b = b.next if b else A
            
        return a
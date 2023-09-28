class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        dupes = set()
        current = head
        dupes.add(current.val)

        while current:
            if current.next:
                if current.next.val in dupes:
                    current.next = current.next.next
                else:
                    dupes.add(current.next.val)
                    current = current.next
            else:
                current = current.next
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    x = s.deleteDuplicates(head)
    while x:
        print(x.val)
        x = x.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = ListNode(0)
        lower = ListNode(0)

        temp1, temp2 = greater, lower

        cur = head
        while cur:
            if cur.val < x:
                temp2.next = cur
                temp2 = temp2.next
            else:
                temp1.next = cur
                temp1 = temp1.next
            cur = cur.next
        

        temp1.next = None

        temp2.next = greater.next

        return lower.next

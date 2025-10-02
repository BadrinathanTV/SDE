# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        current= head
        lenn=1
        while current.next:
            current=current.next
            lenn+=1
        current.next=head
        k =lenn -(k%lenn)
        while k>0:
            current=current.next
            k-=1
        new=current.next
        current.next = None
        return new
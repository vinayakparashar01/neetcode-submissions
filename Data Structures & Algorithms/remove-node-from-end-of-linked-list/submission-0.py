# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        x=0
        while cur:
            cur=cur.next
            x+=1
        if n == x:
            return head.next
        y=0
        prev=None
        curr=head
        while curr:
            if x-y==n :
                prev.next=curr.next
                return head
            prev=curr
            curr=curr.next
            y+=1

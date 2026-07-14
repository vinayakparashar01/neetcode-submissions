# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x=list1
        y=list2
        dummy=ListNode(-1)
        tail=dummy
        while x and y:
            if x.val<=y.val:
                tail.next=x
                tail=tail.next
                x=x.next
            else:
                tail.next=y
                tail=tail.next   
                y=y.next
        if y:
            while y:
                tail.next=y
                tail=tail.next   
                y=y.next
        elif x:
            while x:
                tail.next=x
                tail=tail.next   
                x=x.next
            

        return dummy.next                     




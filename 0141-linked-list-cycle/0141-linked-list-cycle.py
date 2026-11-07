# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        s,f=head,head
        if head==None:
            return False
        while s and f and f.next:

            if s!=None:
                s=s.next
            if f.next!= None:
                f=f.next.next
            if s is f:
                return True
        return False

        
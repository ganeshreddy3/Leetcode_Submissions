# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        temp=None
        while ptr:
            front=ptr.next
            ptr.next=temp
            temp=ptr
            ptr=front
        return temp
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        Sol 1 
        """

        rev = None

        curr = head

        while curr:

            temp = curr
            curr = curr.next
            temp.next = rev
            rev = temp 


        return rev


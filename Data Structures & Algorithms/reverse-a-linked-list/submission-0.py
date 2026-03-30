# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        runner = head

        result = None

        while runner!= None:

            temp = runner
            runner = runner.next

            temp.next = result
            result = temp

        return result

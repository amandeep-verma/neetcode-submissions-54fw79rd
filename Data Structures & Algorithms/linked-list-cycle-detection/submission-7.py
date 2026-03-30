# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        speedRunner = doubleSpeedRunner = head

        while doubleSpeedRunner and doubleSpeedRunner.next:
            speedRunner = speedRunner.next
            doubleSpeedRunner = doubleSpeedRunner.next.next
            if speedRunner == doubleSpeedRunner:
                return True
            
            
        return False
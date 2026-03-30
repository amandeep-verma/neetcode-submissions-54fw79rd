# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        speedRunner = head
        if head and head.next:
            doubleSpeedRunner = head.next
        else:
            return False

        while speedRunner:
            if speedRunner == doubleSpeedRunner:
                return True
            speedRunner = speedRunner.next
            if doubleSpeedRunner.next and doubleSpeedRunner.next.next:
                doubleSpeedRunner = doubleSpeedRunner.next.next
            else:
                return False
            

        return False
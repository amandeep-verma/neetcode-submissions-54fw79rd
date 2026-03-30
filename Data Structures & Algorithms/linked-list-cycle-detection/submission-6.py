# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        speedRunner = fakeHead = ListNode(0, head)
        doubleSpeedRunner = head

        while speedRunner and doubleSpeedRunner:
            if speedRunner == doubleSpeedRunner:
                return True
            speedRunner = speedRunner.next
            if doubleSpeedRunner.next and doubleSpeedRunner.next.next:
                doubleSpeedRunner = doubleSpeedRunner.next.next
            else:
                return False
            
        return False
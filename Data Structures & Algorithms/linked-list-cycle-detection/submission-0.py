# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr, curr2x = head, head

        while curr and curr2x and curr2x.next:
            curr = curr.next
            curr2x = curr2x.next.next
            if curr == curr2x:
                return True

        return False

        
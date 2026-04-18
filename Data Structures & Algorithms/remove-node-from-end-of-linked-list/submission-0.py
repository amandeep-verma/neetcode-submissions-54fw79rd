# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findLen(l):

            curr = l
            temp = 0
            while curr:
                temp += 1
                curr = curr.next
            return temp

        currSize = findLen(head)
        posToRemove = currSize - n + 1
        print(posToRemove)

        fakeHead = ListNode(None, head)
        curr = fakeHead
        pp = curr
        while curr:
            # print(curr.val," ", posToRemove)
            if posToRemove == 0:
                pp.next = curr.next

                return fakeHead.next
            
            posToRemove -= 1
            pp = curr
            curr = curr.next
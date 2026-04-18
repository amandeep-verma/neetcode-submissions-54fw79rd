# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def findLen(l):

            curr = l
            temp = 0
            while curr:
                temp += 1
                curr = curr.next
            return temp
        

        size1 = findLen(l1)
        size2 = findLen(l2)

        if size2 > size1:
            l1, l2 = l2, l1
            size1, size2 = size2, size1

        curr1 = l1
        curr2 = l2
        prevPointer = None

        carry = 0
        while curr1:
            if curr2 != None:
                valueOnCurr2 = curr2.val
                curr2 = curr2.next
            else:
                valueOnCurr2 = 0
            
            total = curr1.val + valueOnCurr2 + carry
            curr1.val = total%10 
            carry = total//10
            
            prevPointer = curr1
            curr1 = curr1.next

        if carry != 0:
            prevPointer.next = ListNode(carry, None)

        return l1
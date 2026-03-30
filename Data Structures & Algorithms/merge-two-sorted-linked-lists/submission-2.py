# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        Sol 1 
        """

        r1 = list1
        r2 = list2
        res = None
        r3 = res


        while r1 and r2:
            if r1.val < r2.val:
                if r3 == None:
                    res = r1
                    r3 = res
                else:
                    r3.next = r1
                    r3 = r3.next
                r1 = r1.next
            else:
                if r3 == None:
                    res = r2
                    r3 = res
                else:
                    r3.next = r2
                    r3 = r3.next
                r2 = r2.next

        if r1:
            if r3 == None:
                res = r1
            else:
                r3.next = r1
        elif r2:
            if r3 == None:
                res = r2
            else:
                r3.next = r2
            
        return res

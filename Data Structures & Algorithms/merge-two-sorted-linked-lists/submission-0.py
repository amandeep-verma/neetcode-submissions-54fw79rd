# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultHead = ListNode()

        current = resultHead

        while list1!= None or list2!= None:

            if list1 == None:
                current.next = list2
                break
            elif list2 == None:
                current.next = list1
                break

            if list1.val <= list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next


        return resultHead.next
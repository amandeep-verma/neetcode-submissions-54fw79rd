# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stackOne = []
        stackTwo = []

        if p:
            stackOne.append(p)
        if q:
            stackTwo.append(q)
        

        while stackOne and stackTwo and len(stackOne)== len(stackTwo):
            currO = stackOne.pop()
            currT = stackTwo.pop()

            if currO.val != currT.val:
                return False

            if currO.left:
                stackOne.append(currO.left)
            if currT.left:
                stackTwo.append(currT.left)
            
            if len(stackOne) != len(stackTwo):
                return False

            if currO.right:
                stackOne.append(currO.right)
            if currT.right:  
                stackTwo.append(currT.right)
            

        return (not stackOne and not stackTwo)


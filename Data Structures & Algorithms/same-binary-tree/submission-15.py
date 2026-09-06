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

        if p and q:
            stackOne.append(p)
            stackTwo.append(q)
        elif p or q:
            return False
        

        while stackOne and stackTwo:
            currO = stackOne.pop()
            currT = stackTwo.pop()

            if currO.val != currT.val:
                return False

            if currO.left and currT.left:
                stackOne.append(currO.left)
                stackTwo.append(currT.left)
            elif currO.left or currT.left:
                return False


            if currO.right and currT.right: 
                stackOne.append(currO.right)
                stackTwo.append(currT.right)
            elif currO.right or currT.right:
                return False
            

        return True


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

            if not currO and not currT:
                continue

            if not currO or not currT or currO.val != currT.val:
                return False


            stackOne.append(currO.left)
            stackTwo.append(currT.left)

            stackOne.append(currO.right)
            stackTwo.append(currT.right)
            

        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isBalancedHelper(self, node: Optional[TreeNode]):
        if node == None:
            return True, 0

        balancedL, heightLeft = self.isBalancedHelper(node.left)
        balancedR, heightRight = self.isBalancedHelper(node.right)
        
        return balancedL and balancedR and abs(heightRight - heightLeft)<2, 1+ max(heightLeft, heightRight)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        result, height = self.isBalancedHelper(root)
        return result

        

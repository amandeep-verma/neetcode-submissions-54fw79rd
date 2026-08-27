# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:



    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def isBalancedHelper(node: Optional[TreeNode]):
            if node == None:
                return True, 0

            balancedL, heightLeft = isBalancedHelper(node.left)

            # if !balancedL:
            balancedR, heightRight = isBalancedHelper(node.right)
            
            return balancedL and balancedR and abs(heightRight - heightLeft)<2, 1+ max(heightLeft, heightRight)

        result, height = isBalancedHelper(root)
        return result

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True

        def dfs(curr):
            nonlocal isBalanced

            if not curr:
                return 0

            heightLeft = dfs(curr.left)
            heightRight = dfs(curr.right)

            isBalanced = isBalanced and abs(heightRight - heightLeft) <=1

            return 1+ max(heightLeft, heightRight)

        dfs(root)

        return isBalanced
        
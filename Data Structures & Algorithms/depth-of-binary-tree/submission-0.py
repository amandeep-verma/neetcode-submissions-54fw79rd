# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepthHelper(self, current: Optional[TreeNode]) -> int:
        if current == None:
            return 0

        return 1 + max(self.maxDepthHelper(current.left), self.maxDepthHelper( current.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.maxDepthHelper(root)
        
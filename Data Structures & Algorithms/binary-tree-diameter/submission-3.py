# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def dfs(curr):
            nonlocal diameter
            if curr == None:
                return 0

            depthL =  dfs(curr.left)
            depthR =  dfs(curr.right)
            diameter = max(diameter, depthL+ depthR)
            return  1+ max(depthL, depthR)
        
        dfs(root)

        return diameter
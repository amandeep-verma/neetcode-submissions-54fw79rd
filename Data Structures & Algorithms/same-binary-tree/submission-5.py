# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def dfs(nodeOne, nodeTwo):

            if not nodeOne and not nodeTwo:
                return True
            if not nodeOne or not nodeTwo:
                return False

            return nodeOne.val == nodeTwo.val and dfs(nodeOne.left, nodeTwo.left) and dfs(nodeOne.right, nodeTwo.right)

        
        return dfs(p,q)

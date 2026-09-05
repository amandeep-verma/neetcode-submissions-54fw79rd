# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        isSameTree = True

        def dfs(nodeOne, nodeTwo):
            nonlocal isSameTree

            if not nodeOne or not nodeTwo:
                if not nodeOne and not nodeTwo:
                    return True
                else:
                    isSameTree = False
                    return False
            
            a = dfs(nodeOne.left, nodeTwo.left)
            b = dfs(nodeOne.right, nodeTwo.right)

            return nodeOne.val == nodeTwo.val and a and b

        
        return dfs(p,q)





        return isSameTree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, maxV, minV):
            if node == None:
                return True

            if node.val >= maxV or node.val <= minV:
                return False

            return dfs(node.left, node.val, minV) and dfs(node.right, maxV, node.val)

            # a, b = True, True

            # l,r = node.left, node.right
            # if l:
            #     if l.val >= node.val:
            #         return False
            #     a = dfs(l)
            # if r:
            #     if r.val <= node.val:
            #         return False
            #     b = dfs(r)

            # return a and b
        
        return dfs(root, float('inf'),float('-inf'))

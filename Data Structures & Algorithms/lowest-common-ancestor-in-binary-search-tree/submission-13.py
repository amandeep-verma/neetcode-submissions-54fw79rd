# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node: TreeNode, p: TreeNode, q: TreeNode, l, r, v) -> TreeNode:

        if l and r:
            return l, r, v

        if not node:
            return False, False, False

        v1, l1 ,r1 = self.dfs(node.left, p, q, l, r, v)
        v2, l2 ,r2 = self.dfs(node.right, p, q, l, r, v)

        l = l1 or l2
        r = r1 or r2

        if node.val == p.val:
            l = True
        elif node.val == q.val:
            r = True
        
        if v1:
            v = v1
        elif v2:
            v = v2

        if not v and l and r:
            v = node

        return v, l , r

        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        return self.dfs(root,p,q, False, False, False)[0]




        
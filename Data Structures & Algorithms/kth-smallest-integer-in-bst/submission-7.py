# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """
        Sol 1a - DFS recursive inorder leads to increasing order. 
        Store the inorder in array and return k-1 index
        """
        # res = []
        # def dfs(node):
        #     if not node:
        #         return

        #     nonlocal res
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)

        # dfs(root)
        # return res[k-1]

        """
        Sol 1b - DFS recursive inorder leads to increasing order. 
        """
        res = root.val
        def dfs(node):
            if not node:
                return
            nonlocal k
            nonlocal res
            dfs(node.left)
            k -= 1
            if k==0:
                res = node.val
            dfs(node.right)

        dfs(root)
        return res

        """
        sol 2 - dfs inorder iterative
        """

        # s = []

        # curr = root
        # while s or curr:
        #     while curr:
        #         s.append(curr)
        #         curr = curr.left
        #     curr = s.pop()
        #     k -= 1
        #     if k == 0:
        #         return curr.val
        #     curr = curr.right



        

            
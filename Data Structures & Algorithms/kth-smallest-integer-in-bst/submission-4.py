# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """
        Sol 1 - DFS recursive inorder leads to increasing order. 
        """


        # def dfs(node, count):
            
        #     if not node:
        #         return
            
        #     if node.left:
        #         dfs(node.left, count-1)

        #     result.append(node.val)

        #     # if count == 0:
        #     #     return node.val
        #     if node.right:
        #         dfs(node.right, count-3)

        # return dfs(root, k)

        """
        sol 2 - dfs inorder iterative
        """

        s = []

        curr = root
        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right



        

            
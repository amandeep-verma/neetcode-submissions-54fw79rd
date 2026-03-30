# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

   


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def diameterOfBinaryTreeHelper(root: Optional[TreeNode]) -> [int]:
            nonlocal res
            if root == None:
                return 0

            heightLeft = diameterOfBinaryTreeHelper(root.left)
            heightRight = diameterOfBinaryTreeHelper(root.right)
            res = max(res, heightLeft + heightRight)

            return 1 + max(heightLeft,heightRight)

        diameterOfBinaryTreeHelper(root)

        return res



        
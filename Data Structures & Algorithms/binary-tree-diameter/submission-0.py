# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> [int]:
        if root == None:
            return [0 ,0]

        heightLeft, leftMax = self.diameterOfBinaryTreeHelper(root.left)
        heightRight, rightMax = self.diameterOfBinaryTreeHelper(root.right)
        tempMaxDiameter = heightLeft + heightRight
        currMax = max(leftMax, rightMax, tempMaxDiameter)

        return [1 + max(heightLeft,heightRight),currMax]


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        return self.diameterOfBinaryTreeHelper(root)[1]

        
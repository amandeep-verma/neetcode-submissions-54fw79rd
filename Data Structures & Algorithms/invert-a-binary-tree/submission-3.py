# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # def reverse(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    #     if root.left == None and root.right == None:
    #         return root

    #     tempLeft = root.left
    #     root.left = root.right
    #     root.right = tempLeft

    #     reverse(root.left)
    #     reverse(root.right)
    #     return root

        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return root

        tempLeft = root.left
        root.left = root.right
        root.right = tempLeft

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


        

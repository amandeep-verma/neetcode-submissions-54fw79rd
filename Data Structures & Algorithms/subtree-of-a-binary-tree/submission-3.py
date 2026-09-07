# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def sameTree(self, nodeOne, nodeTwo) -> bool:

        if not nodeOne and not nodeTwo:
            return True
        if not nodeOne or not nodeTwo or nodeOne.val != nodeTwo.val:
            return False

        return self.sameTree(nodeOne.left,nodeTwo.left) and self.sameTree(nodeOne.right,nodeTwo.right)

    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        stack = []
        
        if root:
            stack.append(root)

        while stack and stack[0]:
            curr = stack.pop()

            if curr.val == subRoot.val and self.sameTree(curr, subRoot):
                return True
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return False
        


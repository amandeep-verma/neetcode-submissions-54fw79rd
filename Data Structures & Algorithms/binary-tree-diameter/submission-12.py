# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = [root]
        diameter = 0
        explored = {None: 0}

        while stack and stack[0]:
            curr = stack[-1]

            flag = True

            if curr.left and curr.left not in explored:
                stack.append(curr.left)
                flag = False
            if curr.right and curr.right not in explored:
                stack.append(curr.right)
                flag = False
            
            if flag:
                curr = stack.pop()

                leftHeight = explored.get(curr.left)
                rightHeight = explored.get(curr.right)
                currDiam = leftHeight + rightHeight
                explored[curr] = 1 + max(leftHeight, rightHeight)
                diameter  = max(diameter, currDiam)

        return diameter

            


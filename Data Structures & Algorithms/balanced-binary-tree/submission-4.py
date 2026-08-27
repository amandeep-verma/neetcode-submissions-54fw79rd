# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # dfs recursion
        # def isBalancedHelper(node: Optional[TreeNode]):
        #     if node == None:
        #         return True, 0

        #     balancedL, heightLeft = isBalancedHelper(node.left)

        #     balancedR, heightRight = isBalancedHelper(node.right)
            
        #     return balancedL and balancedR and abs(heightRight - heightLeft)<2, 1+ max(heightLeft, heightRight)

        # result, height = isBalancedHelper(root)
        # return result

        # dfs iterative

        stack = [root]
        explored = {}

        while stack and stack[-1]:

            curr = stack[-1]
            if curr.right and curr.right not in explored:
                stack.append(curr.right)
            elif curr.left and curr.left not in explored:
                stack.append(curr.left)
            else:
                popped = stack.pop()
                
                lh = explored.get(curr.left, 0)
                rh = explored.get(curr.right, 0)
                explored[curr] = 1+ max(lh, rh)
                if abs(lh - rh)>1:
                    return False

        return True
            

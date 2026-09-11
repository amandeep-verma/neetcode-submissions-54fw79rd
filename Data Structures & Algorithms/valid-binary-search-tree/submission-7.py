# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        """
        Sol1 - 
        """
        # def dfs(node, maxV, minV):
        #     if node == None:
        #         return True

        #     if node.val >= maxV or node.val <= minV:
        #         return False

        #     return dfs(node.left, node.val, minV) and dfs(node.right, maxV, node.val)

        
        # return dfs(root, float('inf'),float('-inf'))


        """
        Sol2 - BFS
        """
        q = deque()
        if root:
            q.append((root, float('inf'), float('-inf')))

        while q:
            curr, maxV, minV = q.popleft()

            if curr.val >= maxV or curr.val <= minV:
                return False

            if curr.left:
                q.append((curr.left, curr.val, minV))
            if curr.right:
                q.append((curr.right, maxV, curr.val))

        return True



        

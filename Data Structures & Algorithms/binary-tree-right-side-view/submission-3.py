# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        """
        Sol 1 DFS
        """

        result = []

        def dfs(node, depth):
            nonlocal result
            if node == None:
                return

            if len(result)<= depth:
                result.append(node.val)

            dfs(node.right,depth +1)
            dfs(node.left, depth +1)

        dfs(root, 0)
        return result





        """
        Sol 2 BFS -
        use for loop to take out node from queue at each level. Add last node into the result at each level
        """
        # q = deque()
        # if root:
        #     q.append(root)

        # result = []

        # while q:
        #     l = len(q)
            
        #     for i in range(l):
        #         curr = q.popleft()
                
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)

        #         if i == l-1:
        #             result.append(curr.val)

        # return result

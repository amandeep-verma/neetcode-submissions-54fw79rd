# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque([root])
        result = []

        while queue and queue[0]:
            subRes = []
            for i in range(len(queue)):
                curr = queue.popleft()
                subRes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            subRes = subRes[-1]

            result.append(subRes)

        return result
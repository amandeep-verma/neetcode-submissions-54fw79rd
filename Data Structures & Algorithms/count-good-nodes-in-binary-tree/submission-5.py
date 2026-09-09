# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        maxVal = float('-inf')
        total = 0

        queue = deque()
        if root:
            queue.append((root, maxVal))

        while queue:
            for i in range(len(queue)):

                curr, currMax = queue.popleft()
                if curr.val >= currMax:
                    total += 1
                    currMax = curr.val
                
                if curr.left:
                    queue.append((curr.left, currMax))
                if curr.right:
                    queue.append((curr.right, currMax))

        return total
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxD = 0
        queue = deque()
        if root:
            maxD += 1
            queue.append((root, maxD))

        while queue and queue[0]:
            currNode, currDepth = queue.popleft()
            print(currNode.val, "  ",currDepth)

            if currNode.left:
                queue.append((currNode.left, currDepth+1))
            if currNode.right:
                queue.append((currNode.right, currDepth+1))

            maxD = max(maxD, currDepth)

        return maxD



        
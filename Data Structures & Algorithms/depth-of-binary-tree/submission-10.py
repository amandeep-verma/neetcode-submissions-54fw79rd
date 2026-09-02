# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepthHelper(self, node, height):
        if node == None:
            return height

        return max(self.maxDepthHelper(node.left, height+1), self.maxDepthHelper(node.right, height+1))
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # maxD = 0
        # queue = deque()
        # if root:
        #     maxD += 1
        #     queue.append((root, maxD))

        # while queue and queue[0]:
        #     currNode, currDepth = queue.popleft()

        #     if currNode.left:
        #         queue.append((currNode.left, currDepth+1))
        #     if currNode.right:
        #         queue.append((currNode.right, currDepth+1))

        #     maxD = max(maxD, currDepth)

        # return maxD



        
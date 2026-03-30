# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepthHelper(self, current: Optional[TreeNode]) -> int:
        if current == None:
            return 0

        return 1 + max(self.maxDepthHelper(current.left), self.maxDepthHelper( current.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        """
        Sol 1 DFS
        O(n)
        """
        # return self.maxDepthHelper(root)

        """
        Sol 2 BFS - mark the level at each level
        O(n)
        """
        queue = deque()
        if root:
            queue.append(root)
        level = 0

        while queue:

            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return level


        """
        Sol 3 DFS iterative
        O(n)
        """

        # myStack = []
        # if root:
        #     myStack.append([root,1])
        # res = 0

        # while myStack:
        #     node, depth = myStack.pop()
        #     res = max(res, depth)
        #     if node.left:
        #         myStack.append([node.left, depth+1])
        #     if node.right:
        #         myStack.append([node.right, depth+1])

        # return res

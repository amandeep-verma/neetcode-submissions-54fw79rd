# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    

    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # stack = [root]

        # while stack and stack[-1]:
        #     curr = stack.pop()
        #     temp = curr.left

        #     curr.left = curr.right
        #     curr.right = temp

        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)


        # return root
        
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            curr = queue.popleft()
            
            left, right = curr.left, curr.right
            if curr.left:
                queue.append(left)
            if curr.right:
                queue.append(right)

            curr.left = right
            curr.right= left
            

        return root




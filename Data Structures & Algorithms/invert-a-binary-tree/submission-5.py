# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTreeHelper(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node == None:
            return None
        
        temp = node.right
        node.right = self.invertTreeHelper(node.left)
        node.left = self.invertTreeHelper(temp)

        return node

    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.invertTreeHelper(root)

        return root
        
        # queue = deque()

        # if root:
        #     queue.append(root)

        # while queue:
        #     curr = queue.popleft()
            
        #     left, right = None, None
        #     if curr.left:
        #         left = curr.left
        #         queue.append(left)
        #     if curr.right:
        #         right = curr.right
        #         queue.append(right)

        #     curr.left = right
        #     curr.right= left
            

        # return root




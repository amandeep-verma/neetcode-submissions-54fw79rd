# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def inOrder(self, root, res, k):

        if root == None or len(res) >= k :
            return

        if root.left != None:
            self.inOrder(root.left, res, k)
        
        res.append(root.val)

        if root.right != None:
            self.inOrder(root.right, res, k)

        return res


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        myStack = []
        mySet = set()
        myStack.append(root)
        mySet.add(root)

        # while myStack:
        #     l = myStack[-1].left
        #     if l != null and l not in mySet
        #         myStack.append(myStack[-1].left)
        #         mySet.add(l)
        #         continue
            
        res = []
        self.inOrder(root, res, k)

        return res[k-1]
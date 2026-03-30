# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        """
        Sol 1 - recursive
        """
        if (p == None and q == None):
            return True
        if (p == None or q== None or p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        """

        """
        if root == None and subRoot == None:
            return True


        myQueue = deque()
        myQueue.append(root)
        headMatch = False
        current = root

        while(myQueue):
            current = myQueue.popleft()
            if current.val == subRoot.val:
                headMatch = True
                tempC = self.isSameTree(current, subRoot)
                if tempC:
                    return tempC
            if current.left:
                myQueue.append(current.left)
            if current.right:
                myQueue.append(current.right)

        if not headMatch:
            return False

        return self.isSameTree(current, subRoot)
            

        


        
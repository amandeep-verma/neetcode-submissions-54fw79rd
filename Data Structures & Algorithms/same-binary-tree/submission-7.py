# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(nodeOne, nodeTwo):

            if not nodeOne and not nodeTwo:
                return True
            if not nodeOne or not nodeTwo:
                return False

            return nodeOne.val == nodeTwo.val and dfs(nodeOne.left, nodeTwo.left) and dfs(nodeOne.right, nodeTwo.right)

        
        return dfs(p,q)


        isBalanced = True

        stackOne = []
        stackTwo = []

        if p:
            stackOne.append(p)
            if not q:
                return False
            stackTwo.append(q)
        

        while isBalanced and p and q:
            currO = stackOne.pop()
            currT = stackTwo.pop()

            if currO.val != currT.val:
                return False

            if curr0.left:
                stackOne.append(curr0.left)
                if not currT.left:
                    return left
                stackTwo.append(currT.left)

            if curr0.right:
                stackOne.append(curr0.right)
                if not currT.right:
                    return right
                stackTwo.append(currT.right)
            

        return isBalanced


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        """
        preorder - nlr
        inorder - lnr
        
        Sol 1 - Recursive.
        O(n*n)
        """

        # node = None
        # if preorder:
        #     node = TreeNode(preorder[0])
        #     indexI = inorder.index(node.val)
        #     node.left = self.buildTree(preorder[1:indexI+1], inorder[:indexI])
        #     node.right = self.buildTree(preorder[indexI+1:], inorder[indexI+1:])

        # return node

        """
        Sol 2 - using map and iterative ( saving indexing )
        O(n*n)
        """
        myMap = {val: i for i, val in enumerate(inorder)}
        node = None
        
        def dfs(l, r, li, ri):

            if l>r or li>ri:
                return None
                
            node = TreeNode(preorder[l])
            indexI = myMap.get(node.val)
            leftSize = indexI - li

            node.left = dfs(l + 1, l + leftSize, li, indexI - 1)

            node.right = dfs(l + leftSize + 1, r, indexI + 1, ri )

            return node

        return dfs(0, len(inorder)-1, 0, len(inorder)-1)


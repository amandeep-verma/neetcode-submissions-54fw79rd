# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestorHelper(self, current: TreeNode, p: TreeNode, q: TreeNode, leastCommon: TreeNode) -> TreeNode:

        checkSum = 0
        if current == None:
            return  None, checkSum


        a, cs1=  self.lowestCommonAncestorHelper(current.left, p, q, leastCommon)
        b, cs2 =  self.lowestCommonAncestorHelper(current.right, p, q, leastCommon)

        if current.val == p.val or current.val == q.val:
            checkSum =1
        
        print("curr->", current.val)
        print("lefttree", a, cs1)
        print("righttree", b, cs2)

        if a != None:
            leastCommon = a
        if b != None:
            leastCommon = b
        

        if leastCommon == None and checkSum+cs1+cs2 == 2:
            leastCommon = current
        return leastCommon, checkSum +cs1 +cs2


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # a,b =  self.lowestCommonAncestorHelper(root, p, q, None)

        # return a

        """

        """


        a, b = p, q
        if p.val > q.val:
            a,b = b, a

        myqueue = deque()
        myqueue.append(root)

        while myqueue:
            curr = myqueue.pop()

            if a.val == curr.val or b.val == curr.val or (a.val < curr.val and b.val > curr.val):
                return curr

            if a.val < curr.val:
                myqueue.append(curr.left)
            elif b.val > curr.val:
                myqueue.append(curr.right)
            
            



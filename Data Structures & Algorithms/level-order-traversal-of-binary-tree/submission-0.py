# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        myQ = deque()
        print(root)
        myQ.append(root)
        result = []

        while myQ and myQ[0] != None:
            size = len(myQ)

            currentList = []
            for i in range(size):
                curr = myQ.popleft()
                currentList.append(curr.val)
                if curr.left != None:
                    myQ.append(curr.left)
                if curr.right != None:
                    myQ.append(curr.right)

            result.append(currentList)


        return result
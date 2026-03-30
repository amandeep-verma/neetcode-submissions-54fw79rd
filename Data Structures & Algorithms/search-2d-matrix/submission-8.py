class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
        Sol 1 Brute force - iterate through each element to find if there is match
        O(m*n)
        """

        """
        Sol 2 Binary Search - 
        O(log(m*n))
        """



        row = len(matrix)
        col = len(matrix[0])
        # print(row, " ", col)

        r = row -1
        l = 0

        while l <= r :
            m = l+ (r-l)//2
            if target < matrix[m][0]:
                r = m-1
            elif target > matrix[m][col-1]:
                l = m+1
            else:
                iL = 0 
                iR = col -1

                while iL <= iR:
                    iM = iL +(iR-iL)//2
                    if target < matrix[m][iM]:
                        iR = iM -1
                    elif target > matrix[m][iM]:
                        iL = iM +1
                    else:
                        return True

                return False

        return False
        
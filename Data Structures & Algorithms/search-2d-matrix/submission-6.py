class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        l, r = 0 , row -1

        while l <= r:
            mid = l + (r-l)//2
            print(l, r, mid)
            
            if target > matrix[mid][col-1]:
                l = mid +1
            elif target < matrix[mid][0]:
                r = mid -1
            else:
                iL, iR = 0, col -1
                while iL <= iR:
                    iMid = iL + (iR- iL)//2
                    print(iL, iR, iMid)
                    if target > matrix[mid][iMid]:
                        iL = iMid +1
                    elif target < matrix[mid][iMid]:
                        iR = iMid -1
                    else:
                        return True
                return False

        return False




        # row = len(matrix)
        # col = len(matrix[0])
        # # print(row, " ", col)

        # r = row -1
        # l = 0

        # while l <= r :
        #     m = (int)((l + r)/2)
        #     print(l," ", r," ",m)
        #     if target < matrix[m][0]:
        #         # print("here")
        #         r = m-1
        #     elif target > matrix[m][col-1]:
        #         l = m+1
        #     else:
        #         iL = 0 
        #         iR = col -1

        #         while iL <= iR:
        #             iM = (int)((iL+iR)/2)
        #             if target < matrix[m][iM]:
        #                 iR = iM -1
        #             elif target > matrix[m][iM]:
        #                 iL = iM +1
        #             else:
        #                 return True

        #         return False

        # return False
        
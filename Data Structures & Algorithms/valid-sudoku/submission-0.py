class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check for rows and columns
        for i in range(9):
            rowSet = set()
            colSet = set()

            for j in range(9):
                valR= board[i][j]
                valC = board[j][i]
                if valR == "." : pass
                elif valR in rowSet: return False
                else: rowSet.add(valR)
                
                if valC == "." : pass
                elif valC in colSet: return False
                else: colSet.add(valC)

        #  check for grid
        for i in range(0,9,3):
            for j in range(0,9,3):
                newSet = set()
                for newI in range(i, i+3):
                    for newJ in range(j, j+3):
                        val= board[newI][newJ]
                        if val == "." : pass
                        elif val in newSet: return False
                        else: newSet.add(val)

        return True

        
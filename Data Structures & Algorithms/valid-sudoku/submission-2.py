class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        """
        Sol1 - check for row and columns in one loop and check for each 3*3 grid in another
        """
        # # Check for rows and columns
        # for i in range(9):
        #     rowSet = set()
        #     colSet = set()

        #     for j in range(9):
        #         valR= board[i][j]
        #         valC = board[j][i]
        #         if valR == "." : pass
        #         elif valR in rowSet: return False
        #         else: rowSet.add(valR)
                
        #         if valC == "." : pass
        #         elif valC in colSet: return False
        #         else: colSet.add(valC)

        # #  check for grid
        # for i in range(0,9,3):
        #     for j in range(0,9,3):
        #         newSet = set()
        #         for newI in range(i, i+3):
        #             for newJ in range(j, j+3):
        #                 val= board[newI][newJ]
        #                 if val == "." : pass
        #                 elif val in newSet: return False
        #                 else: newSet.add(val)

        # return True

        """
        Sol2 - In 1 loop - Instead of using set, use HashSet - dictionary of sets,
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] == "." : continue

                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in grid[(i//3, j//3)]:
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grid[(i//3, j//3)].add(board[i][j])

        return True

        
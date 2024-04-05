from collections import defaultdict


## https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)

        ##0-8 (1-9)
        subBoxes = [set() for _ in range(9)]

        for i in range(0, 9):

            for j in range(0, 9):

                num = board[i][j]

                if num == ".":
                    continue

                subBoxNumber = self.getSubbox(i, j)
                subBox = subBoxes[subBoxNumber]

                if num in rows[i] or num in columns[j] or num in subBox:
                    return False

                rows[i].add(num)
                columns[j].add(num)
                subBox.add(num)

        return True

    def getSubbox(self, row, column):
        ###0, 1, 2,
        ###3, 4, 5,
        ###6, 7, 8
        rowSubbox = row // 3
        columnSubbox = column // 3

        if rowSubbox == 0 and columnSubbox == 0:
            return 0

        if rowSubbox == 0 and columnSubbox == 1:
            return 1

        if rowSubbox == 0 and columnSubbox == 2:
            return 2

        if rowSubbox == 1 and columnSubbox == 0:
            return 3

        if rowSubbox == 1 and columnSubbox == 1:
            return 4

        if rowSubbox == 1 and columnSubbox == 2:
            return 5

        if rowSubbox == 2 and columnSubbox == 0:
            return 6

        if rowSubbox == 2 and columnSubbox == 1:
            return 7

        if rowSubbox == 2 and columnSubbox == 2:
            return 8

solution = Solution()

print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                              ["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],
                              ["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],
                              ["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],
                              [".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]))

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        # Store numbers already used in each row
        rows = [set() for _ in range(9)]

        # Store numbers already used in each column
        cols = [set() for _ in range(9)]

        # Store numbers already used in each 3x3 box
        boxes = [set() for _ in range(9)]

        # Initialize the sets using existing Sudoku numbers
        for r in range(9):
            for c in range(9):

                value = board[r][c]

                if value != ".":

                    box_index = (r // 3) * 3 + (c // 3)

                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[box_index].add(value)

        # Backtracking function
        def backtrack():

            for r in range(9):
                for c in range(9):

                    # Find an empty cell
                    if board[r][c] == ".":

                        box_index = (r // 3) * 3 + (c // 3)

                        # Try numbers from 1 to 9
                        for num in "123456789":

                            # Check Sudoku constraints
                            if (
                                num not in rows[r]
                                and num not in cols[c]
                                and num not in boxes[box_index]
                            ):

                                # Make a choice
                                board[r][c] = num

                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box_index].add(num)

                                # Explore the next empty cell
                                if backtrack():
                                    return True

                                # Undo the choice
                                board[r][c] = "."

                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box_index].remove(num)

                        # No valid number found
                        return False

            # No empty cells remain
            return True

        backtrack()

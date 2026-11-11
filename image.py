class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:

        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = (
                    matrix[j][i], matrix[i][j]
                )

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
#Time Complexity: O(n²)

#Space Complexity: O(1)

#Optimization: In-place matrix manipulation.

#Key Takeaway:

#A square matrix can be rotated 90 degrees clockwise efficiently by first transposing the matrix and then reversing each row.

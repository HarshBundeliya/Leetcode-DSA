class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Time Complexity = O(log(m*n))
        # Space Complexity = O(1)
        s = 0
        num_row = len(matrix)
        num_col = len(matrix[0])
        e = num_row*num_col - 1
        while s <= e:
            mid = (s + e)//2
            m = mid // num_col
            n = mid % num_col
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target:
                s = mid + 1
            else:
                e = mid - 1
        return False
        
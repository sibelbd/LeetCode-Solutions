# Runtime: 32 ms, faster than 97.46% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 17.2 MB, less than 96.30% of Python3 online submissions for Search a 2D Matrix II.

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Pretty straight forward, check each item in each list within the list and if it equals the target, return true, otherwise, return false

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            for item in row:
                if item == target:
                    return True
        return False
                

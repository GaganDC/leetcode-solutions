class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n = len(mat)
        m  = len(mat[0])
        low = 0
        high = m-1

        while low<= high:
            
            mid = (low + high)//2
            row = max(range(n), key=lambda r: mat[r][mid])

            left = mat[row][mid -1] if mid -1 >= 0 else -1
            right = mat[row][mid +1] if mid+1 < m else -1
            curr = mat[row][mid]

            if curr > right  and curr > left:
                return [row,mid]
            elif left >curr:
                high = mid -1
            else:
                low = mid +1

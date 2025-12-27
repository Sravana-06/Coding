class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)

        def count_less_equal(x):
            cnt = 0
            col = n - 1
            for row in range(n):
                while col >= 0 and mat[row][col] > x:
                    col -= 1
                cnt += (col + 1)
            return cnt

        low, high = mat[0][0], mat[n-1][n-1]

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

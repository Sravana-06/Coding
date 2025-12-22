class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])

        max_ones = 0
        row_index = -1

        for i in range(n):
            left, right = 0, m - 1
            first_one = m

            while left <= right:
                mid = (left + right) // 2
                if arr[i][mid] == 1:
                    first_one = mid
                    right = mid - 1
                else:
                    left = mid + 1

            ones_count = m - first_one

            if ones_count > max_ones:
                max_ones = ones_count
                row_index = i

        return row_index

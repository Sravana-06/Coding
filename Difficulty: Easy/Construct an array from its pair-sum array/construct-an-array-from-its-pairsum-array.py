class Solution:
    def constructArr(self, arr):
        import math
        m = len(arr)
        if m == 1:
            return [1, arr[0] - 1]

        n = (1 + int(math.sqrt(1 + 8*m))) // 2

        res0 = (arr[0] + arr[1] - arr[n - 1]) // 2
        res = [0] * n
        res[0] = res0
        res[1] = arr[0] - res0
        res[2] = arr[1] - res0

        for i in range(3, n):
            res[i] = arr[i - 1] - res0

        return res
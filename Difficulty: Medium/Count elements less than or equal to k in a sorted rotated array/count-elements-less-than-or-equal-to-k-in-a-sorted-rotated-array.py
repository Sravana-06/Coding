class Solution:
    def countLessEqual(self, arr, x):
        count = 0
        for val in arr:
            if val <= x:
                count += 1
        return count

class Solution:
    def minTime(self, rank, n):
        def donuts_in_time(time):
            total = 0
            for r in rank:
                t = r
                cnt = 1
                while t <= time:
                    total += 1
                    cnt += 1
                    t += cnt * r
                if total >= n:
                    return True
            return False

        low = 0
        high = max(rank) * n * (n + 1) // 2
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if donuts_in_time(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

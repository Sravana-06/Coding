class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        res = []

        for c, b, a in zip(code, businessLine, isActive):
            if a and c and all(ch.isalnum() or ch == "_" for ch in c) and b in order:
                res.append((order[b], c))

        res.sort()
        return [c for _, c in res]
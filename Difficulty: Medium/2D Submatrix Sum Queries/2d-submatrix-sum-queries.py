class Solution:
    def prefixSum2D(self, mat, queries):
        n = len(mat)
        m = len(mat[0])

        pref = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                pref[i + 1][j + 1] = (
                    mat[i][j]
                    + pref[i][j + 1]
                    + pref[i + 1][j]
                    - pref[i][j]
                )

        result = []

        for r1, c1, r2, c2 in queries:
            result.append(
                pref[r2 + 1][c2 + 1]
                - pref[r1][c2 + 1]
                - pref[r2 + 1][c1]
                + pref[r1][c1]
            )

        return result


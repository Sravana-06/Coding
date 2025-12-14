class Solution:
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        if len(seats) % 2 != 0 or len(seats) == 0:
            return 0
        
        ways = 1
        for i in range(2, len(seats), 2):
            plants_between = seats[i] - seats[i - 1]
            ways = (ways * plants_between) % MOD
        
        return ways

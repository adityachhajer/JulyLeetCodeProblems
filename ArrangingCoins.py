class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        c = 0
        while (i <= n):
            n = n - i
            i = i + 1
            c = c + 1
        return c

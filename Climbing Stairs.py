class Solution:
    def solve(self,n,l):
        if n==0:
            return 1
        if l[n]!=-1:
            return l[n]
        if n<2:
            l[n]=self.solve(n-1,l)
            return l[n]
        else:
            l[n]=self.solve(n-1,l)+self.solve(n-2,l)
            return l[n]
    def climbStairs(self, n: int) -> int:

        l=[-1 for _ in range(n+1)]
        return self.solve(n,l)
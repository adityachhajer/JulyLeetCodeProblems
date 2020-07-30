class Solution:
    def solve(self,prices,l,a,i,s,x):
        if i>=len(prices):
            l.append(a)
            return 0
        if i==len(prices)-1:
            if s=='ON' and x<prices[i]:
                a=a+(prices[i]-x)
                l.append(a)
                return 0
            else:
                l.append(a)
                return 0
        if s=='ON':
            if prices[i]>x :
                return max(self.solve(prices,l,a+(prices[i]-x),i+2,'OFF',0),self.solve(prices,l,a,i+1,'ON',x))
            else:
                return self.solve(prices,l,a,i+1,'ON',x)
        else:
            return max(self.solve(prices, l, a, i + 1, 'ON', prices[i]), self.solve(prices, l, a, i + 1, 'OFF', x))

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)>60:
            prev_cash, cash, hold = 0, 0, float('-inf')
            for i in range(len(prices)):
                prev_cash, cash, hold = cash, max(cash, hold + prices[i]), max(hold, prev_cash - prices[i])
            return cash
        l=[]
        a=0
        x=0
        self.solve(prices,l,a,0,'OFF',x)
        return max(l)
class Solution:
    def solve(self,h,m):
        x=h+float(m/60)
        angleh=x*30
        anglem=6*m
        if abs(angleh-anglem)>180:
            return 360-abs(angleh-anglem)
        return abs(angleh-anglem)
    def angleClock(self, hour: int, minutes: int) -> float:
        x=self.solve(hour,minutes)
        if int(x)==0:
            return 0
        elif x/int(x)==1:
            return int(x)
        return x
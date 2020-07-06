class Solution:
    def decimalToBinary(self,n):
        return bin(n).replace("0b", "")
    def hammingDistance(self, x: int, y: int) -> int:
        x=self.decimalToBinary(x)
        y=self.decimalToBinary(y)
        c=0
        i=len(x)-1
        j=len(y)-1
        while i>=0 and j>=0:
            if x[i]!=y[j]:
                c=c+1
            i-=1
            j-=1
        while i>=0:
            if x[i]!="0":
                c=c+1
            i-=1
        while j>=0:
            if y[j]!='0':
                c=c+1
            j-=1
        return c
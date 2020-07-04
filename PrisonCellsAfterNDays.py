class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        k=[]
        l=[]
        if N%14==0:
            a=14
        else:
            a=N%14
        for i in range(a):
            for j in range(0,len(cells)):
                if j==0 or j==len(cells)-1:
                    l.append(0)
                else:
                    if (cells[j-1] ==1 and cells[j+1]==1) or (cells[j-1] ==0 and cells[j+1]==0):
                        l.append(1)
                    else:
                        l.append(0)
            k.append(l)
            cells=l
            l = []
        return k[-1]
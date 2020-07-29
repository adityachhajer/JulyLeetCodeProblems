class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        di=[0]*26
        for i in tasks:
            di[ord(i)-65]+=1
        di.sort()
        mostfreq=di[25]-1
        idealtime=mostfreq*n
        for i in range(24,-1,-1):
            idealtime-=min(di[i],mostfreq)
            if idealtime<0: return len(tasks)
        return len(tasks)+idealtime
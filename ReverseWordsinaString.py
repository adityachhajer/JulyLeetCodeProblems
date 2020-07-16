class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        k=''
        for i in s:
            if i==' ':
                if len(k)>=1:
                    l.append(k)
                k=''
            else:
                k=k+i
        l.append(k)
        s=''
        c=l.count('')
        for i in range(c):
            l.remove('')
        l=reversed(l)
        return ' '.join(l)
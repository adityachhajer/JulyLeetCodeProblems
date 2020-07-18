class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        for i in nums:
            if i in di.keys():
                di[i]+=1
            else:
                di[i]=1
        sorted(di.values())
        ans=[]
        for w in sorted(di, key=di.get, reverse=True):
            ans.append(w)
            k-=1
            if k==0:
                break
        return ans
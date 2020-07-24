class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        di={}
        for i in nums:
            if i not in di.keys():
                di[i]=1
            else:
                del di[i]
        l=[]
        for i in di.keys():
            l.append(i)
        return l
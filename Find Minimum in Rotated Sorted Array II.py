class Solution:
    def findMin(self, nums: List[int]) -> int:
        x = float('inf')
        for i in nums:
            if i < x:
                x = i
        return x

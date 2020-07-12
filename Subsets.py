class Solution:
    def solve(self, nums, op, result):
        if len(nums) == 0:
            if op not in result:
                result.append(op)
            return
        l = op[::]
        r = op[::]
        r.append(nums[0])
        nums = nums[1:]
        self.solve(nums, l, result)
        self.solve(nums, r, result)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = []
        result = []
        self.solve(nums, op, result)
        return result
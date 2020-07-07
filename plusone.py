class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        merged = int(''.join(str(i) for i in digits))
        merged = merged + 1
        spl = [int(i) for i in str(merged)]
        return spl
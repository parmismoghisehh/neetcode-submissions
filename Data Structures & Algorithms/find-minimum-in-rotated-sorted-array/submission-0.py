class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        n=len(nums)
        return min(nums)
        
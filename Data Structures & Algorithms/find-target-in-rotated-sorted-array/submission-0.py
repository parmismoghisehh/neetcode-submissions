class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        for i in range(n):
            if target not in nums:
                return -1
            else:
                result=nums.index(target)
        return result

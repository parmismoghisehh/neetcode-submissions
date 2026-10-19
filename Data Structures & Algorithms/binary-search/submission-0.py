class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in range(n):
            if target in nums:
                index=nums.index(target)
            else:
                return -1
        return index

            

        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        used = set()
        for i in range(len(nums)):
            if nums[i] in used:
                return True
            used.add(nums[i])
        return False

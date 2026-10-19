class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        result=[]
        for item,count in frequency.most_common(k):
            result.append(item)
        return result
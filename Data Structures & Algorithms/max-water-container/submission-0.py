class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        largest=0
        while left<right:
            width=right-left
            height=min(heights[right],heights[left])
            Area=width*height
            largest=max(largest,Area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return largest



        
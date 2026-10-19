class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        count=0
        characters=set()
        for right in range(n):
            while s[right] in characters:
                characters.remove(s[left])
                left+=1
            characters.add(s[right])
            count=max(count,right-left+1)
        return count





        
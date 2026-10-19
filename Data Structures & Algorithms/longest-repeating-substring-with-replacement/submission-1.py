class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        result=0
        for c in set(s):
            left=0
            difference=0
            for right, char in enumerate(s):
                if char!=c:
                    difference+=1
                while difference>k:
                    if s[left]!=c:
                        difference-=1
                    left+=1
                result=max(result, right-left+1)
        return result



        



        

        
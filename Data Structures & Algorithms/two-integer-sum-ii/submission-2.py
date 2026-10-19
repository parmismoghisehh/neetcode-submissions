class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        right=n-1
        left=0
        
        while left<right:
            if target< numbers[left]+numbers[right]:
                right-=1
            elif target> numbers[right]+numbers[left]:
                left+=1
            else:
                return [left+1 , right+1]
        return []


        

            
            



        
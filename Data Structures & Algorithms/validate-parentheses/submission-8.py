class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        characters={")": "(", "}": "{", "]": "["}
        if len(s)<=1:
            return False
        
        for char in s:
            
            if char in characters:
                if stack:
                    top_element=stack.pop()
                else:
                    top_element='#'
                if characters[char] != top_element:
                    return False
                
            else:
                stack.append(char)
        return len(stack)==0
    




            
                

        
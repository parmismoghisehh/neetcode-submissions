
class Solution:

    def encode(self, strs: List[str]) -> str:
        e = "" #initialising an empty string
        for s in strs:
            e += f"{len(s)}#{s}"
        return e
            

    def decode(self, s: str) -> List[str]:
        
        if not s:
            return []
        decoded_list=[] #initialising an empty list
        i=0 #initilising i
        while i<len(s): #defining while loop 
            j=s.find("#",i) #defining j variable with value of founded i in string s
            length=int(s[i:j]) # length variable is an integer of string s from index i to j

            
            decoded_list.append(s[j+1:j+1+length]) #adding values to decoded list
            i=j+1+length

        return decoded_list #final answer



   


        

       
        


class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reverse="";
		int i=s.length()-1;
        if(s.isEmpty()){
            return true;
        }
        do{
            char c=s.charAt(i);
            reverse+=c;
            i--;
        }
        while(i>=0);
        return s.equals(reverse);
        
        

        
    }
}

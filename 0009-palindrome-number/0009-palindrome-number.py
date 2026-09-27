class Solution:
    def isPalindrome(self, x: int) -> bool:
        digit=0
        reverse=0
        original=x
        if x<0:
            return False

        while x>0:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        if original==reverse :
            return True
        else:
            return False                

        
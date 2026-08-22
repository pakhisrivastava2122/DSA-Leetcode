class Solution:
    def isPalindrome(self ,x: int) -> bool:
        # if str(x)==str(x)[::-1]:
        #     return True
        # else:
        #     return False


        temp = x
        rev = 0

        while temp > 0 :
            r = temp % 10
            temp //= 10
            rev = rev * 10 + r
        return rev==x 
        
        
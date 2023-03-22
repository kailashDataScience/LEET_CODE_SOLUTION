class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        size=len(x)
        reverse=x[size::-1]
        if reverse==x:
            return True
        else:
            return False

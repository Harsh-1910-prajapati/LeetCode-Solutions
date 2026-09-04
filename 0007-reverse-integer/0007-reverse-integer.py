class Solution(object):
    def reverse(self, x):
        is_neg = x < 0
        x =  abs(x) 
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        if is_neg:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1 :
            return 0
        return rev
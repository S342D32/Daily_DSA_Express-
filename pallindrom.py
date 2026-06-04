def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        
        num =x
        rev=0
        while num>0:
            digit = num %10
            rev = rev * 10 + digit
            num = num //10
        return rev == x

print(isPalindrome(121))
# TC= O(log N)
# SC=O(1)
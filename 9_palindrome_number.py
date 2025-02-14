# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(x):
    str_x = str(x)
    reverse_str_x = str_x[::-1]
    if str_x == reverse_str_x:
        return 'true'
    else:
        return 'false'

print(isPalindrome(10))
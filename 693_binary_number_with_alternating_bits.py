# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

def hasAlternatingBits(n):
    n = int(n)
    bin_n = bin(n)
    bin_n = bin_n[2:]

    for i in range(0,len(bin_n) - 1):
        if bin_n[i] == bin_n[i+1]:
            return False

    return True


print(hasAlternatingBits(11))
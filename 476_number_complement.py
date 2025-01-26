# https://leetcode.com/problems/number-complement/description/

def find_complement(num):
    bin_num = bin(num)
    bin_num = list(bin_num)

    for i in range(0, len(bin_num)):
        if bin_num[i] == '0':
            bin_num[i] = '1'
        elif bin_num[i] == '1':
            bin_num[i] = '0'

    bin_num = bin_num[2:]    

    bin_num = ''.join(bin_num)
    ans = int(bin_num,2)

    return ans

print(find_complement(5))
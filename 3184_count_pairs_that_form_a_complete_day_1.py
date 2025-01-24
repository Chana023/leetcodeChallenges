# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
from collections import defaultdict

def countCompleteDayPairs(hours):
    
    count = 0
    for i in range(0, len(hours), 1):
        for j in range(i + 1, len(hours), 1):
            modcalc = (hours[i] + hours[j]) % 24
            if modcalc == 0:
                count +=1
    
    print(count)


print(countCompleteDayPairs([12,12,30,24,24]))



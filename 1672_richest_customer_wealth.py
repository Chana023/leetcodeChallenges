# https://leetcode.com/problems/richest-customer-wealth/description/

def maximumWealth(accounts):
    current_max = 0
    total = 0
    for i in range(0, len(accounts), 1):
        for j in range(0, len(accounts[i]),1):
           total = total + accounts[i][j]

        if total > current_max:
            current_max = total
        total = 0

    return current_max

maximumWealth([[1,2,3],[3,2,3]])
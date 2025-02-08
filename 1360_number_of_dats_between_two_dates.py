# https://leetcode.com/problems/number-of-days-between-two-dates/ 

import datetime as dt

def daysBetweenDates(date1, date2):

    date01 = dt.datetime(int(date1[:4]), int(date1[5:7]), int(date1[8:]))
    date02 = dt.datetime(int(date2[:4]), int(date2[5:7]), int(date2[8:]))

    result = date02 - date01

    print(abs(result.days))
    return abs(result.days)

daysBetweenDates("2020-01-15", "2019-12-31")
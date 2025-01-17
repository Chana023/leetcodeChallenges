# https://leetcode.com/problems/fizz-buzz/description/

def fizzBuzz(n):
    result_arr = []
    for i in range(1, n+1 ,1):
        if i % 3 == 0 and i % 5 == 0:
            result_arr.append('FizzBuzz')
        elif i % 3 == 0:
            result_arr.append("Fizz")
        elif i % 5 == 0:
            result_arr.append("Buzz")
        else:
            result_arr.append(f'{i}')
    
    print(result_arr)

fizzBuzz(3)
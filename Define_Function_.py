def Equal(first_number, second_number) :
    The_Result=a+b
    return The_Result
print(Equal(8, 99))

def Salary(hour_per_day, per_hour):
    if hour_per_day > 8 :
        return 'Error! too much work!'
    else :
        Daily_Income= hour_per_day*per_hour
        return Daily_Income
print(Salary(8,800))

def print_double(x):
    print(2*x)
print_double(2)    

def shout(word):
    return word +"!"
speak = shout
output= speak('shout')
print(output)

def add(x, y):
    return x+y

def do_twice(a, x, y):
    return a(a(x, y), a(x, y))
a=5
b=10
print(do_twice(add, a, b))

def math(nums, func):
    for num in nums:
        func(num)
math([1,2,3,4,5],lambda num: print(num*2))

from math import pi
print(pi)




'''
Created on ۲۱ فروردین ۱۳۹۹

@author: Mohammad
'''

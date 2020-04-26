import random
call1=[1,2]
call2=[1,2,3,4]
Check=9
second=100
number=random.randint(0,100)
first=number
Pyton_Number=random.randint(0, 100)
#the below function will miones 1 number to a for b times.
def mines(a,b):
    for i in range(1,b):
        add =--a
    return add
# This function will pluss 1 number to a for b times.
def plus(a,b):
    for i in range(1,b):
        add=++a
    return add
#the below function will return the division of a to 2.
def division(a):
    add = (a//2)
    return add
#The below function will return halve of a +a.
def halve(a):
    add=(a//2)+a
    return add

def halve_division(a,b):
    add=((a-b)//2)+b
    return add

def Print():
    print('===================================')
    print('  I guess your number is ', number,'!!')
    print('===================================')
    print('If it is your number press "1"')
    print('----------------------------------')
    print('If your number is bigger press "2"')
    print('----------------------------------')
    print('If your number is smaller press "3"')
    print('----------------------------------')
#The firs game the program will randomize a number between 0-100 and user out to guess it,
# the program will say that user input is bigger or smaller than randomized number until user guess or press 0 to exit.
# print('num: ', Pyton_Number)
# User_Number=int(input('Please guess my random number chosen from 0-100: '))
# user_name=str(input('Please enter your name: '))
# while Pyton_Number != User_Number or User_Number != 0:
#     if User_Number == 0:    
#          print('Good game ',user_name,' :) ')
#          break
#     elif User_Number == Pyton_Number:
#          print('Hooray!!! you WON !')
#          break
#     elif User_Number < Pyton_Number:
#          User_Number=int(input('My number is bigger, guess or press 0 to go to next wonderful game!! : '))
#     elif User_Number > Pyton_Number:
#          User_Number=int(input('My number is smaller! guess or press 0 to go to next wonderful game!! : '))
# print(user_name,'My number was', Pyton_Number)
#program will try to discover usered chosen number with some functions and codes, 
#it will randomize a number between 0-100 at the first and after that will ask from user
# that is it bigger/smaller or equal with his/her number, if it is bigger program will check 
# randomized number plus halve of it again up to the answer is Smaller!
# if the randomized number is smaller the program will check randomized number mines halve of it 
# again until the answer is bigger then it will plus/mines one by one until to get achive the user chosen number
sam=int(input('So, Let me guess your number !!! if you agree press "1" if not press "2" : '))
sam=int(sam)
while (sam == 1):
    Print()
    Check = int(input('And "4" for exit: ' ))
    if Check == 1:
        print('Hooraaaaay!!! I am very clever program :) ', 'isnt it ',user_name, '??? :))))))')
    while Check == 2:
        number=(halve_division(second,first))
    Print()
    Check = int(input('And "4" for exit: ' ))
    while Check == 3:
        for s in range(second,100):
            number=(mines(first,s))
            print(first,second)
            second=number
        Print()
        Check = int(input('And "4" for exit: ' ))
else:    
    exit
if sam == 2 :
    print('Good game',user_name,'Have fun see you soon!'' :) ')
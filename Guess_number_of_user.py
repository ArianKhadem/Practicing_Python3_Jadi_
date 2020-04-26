import time
import random
count=0
call1=[1,2]
call2=[1,2,3,4]
Check=9
first=0
number=50
first=number
Pyton_Number=random.randint(0, 100)
def equal_big_dgt(equal_dgt_big, equal_first_big):
    equal_add_big = 0
    if equal_dgt_big < 101 :
        equal_add_big = (equal_dgt_big//2)+equal_dgt_big
        if equal_add_big > 100 :
            for i in range(1,4):
                equal_add_big = equal_dgt_big+i
                if equal_add_big > 100 :
                    equal_add_big = 100
                    print('We achived to the maximum number that agreed ("100"),')
                    print('We will check the smaller numbers with you now!')
                    return equal_add_big
                else:
                    return equal_add_big
        return equal_add_big
def Time(a):
    add=time.sleep(3)
    return add
def Print(guess):
    print('===================================')
    print('  I guess your number is ', guess,'!!')
    print('===================================')
    print('If it is your number press "Y"')
    print('----------------------------------')
    print('If your number is bigger press "B"')
    print('----------------------------------')
    print('If your number is smaller press "S"')
    print('----------------------------------')
    print('if you want to exit press "E"')
    print('----------------------------------')
def greater_big_dgt(greater_dgt, greater_first):
    if greater_dgt > greater_first:
        greater_add=((greater_dgt-greater_first)//2)+(greater_dgt)
        if greater_add > 100 :
            greater_add = 100
            print('We achived to the maximum number that agreed ("100"),')
            print('We will check the smaller numbers with you now!')
            return greater_add
        return greater_add
def halve_division_plus(big_dgt,big_first) :
    if big_dgt == big_first :
        big_add = equal_big_dgt(big_dgt, big_first)
        return big_add
    elif big_dgt > big_first:
        big_add = greater_big_dgt(big_dgt, big_first)
        return big_add
    return big_add
def Big(big_word,big_dgt,big_first):
    big_count=0
    big_chk=big_word
    while big_chk == 'b' :
        big_number=(halve_division_plus(big_dgt,big_first))
        big_first=big_dgt
        big_dgt=big_number
        Print(big_number)
        big_chk=str(input('Please enter your choice: '))
        big_count +=1
        return big_chk, big_number, big_first
    return big_word, big_dgt, big_first
def equal_sm_dgt(equal_dgt_sm, equal_first_sm):
    equal_add_sm = 0
    if equal_dgt_sm < 51 :
        print(equal_dgt_sm,'dgt_sm','test_equal_sm_dgt')
        equal_add_sm = equal_dgt_sm-(equal_dgt_sm//2)
        print(equal_add_sm,"small")
        if equal_add_sm == 0 :
            for i in range(1,4):
                equal_add_sm = equal_dgt_sm-i
                if equal_add_sm <= 0 :
                    equal_add_sm = 0
                    print('We achived to the minimum number that agreed ("0"),')
                    print('We will check the bigger numbers with you now!')
                    return equal_add_sm
                else:
                    return equal_add_sm
        return equal_add_sm
    print(equal_add_sm,'smmmm')
    return equal_add_sm
def smaller_sm_dgt(smaller_dgt, smaller_first):
    if smaller_dgt < smaller_first:
        smaller_add=((smaller_first-smaller_dgt)//2)+(smaller_dgt)
        print(smaller_add,'add', smaller_first,'first', smaller_dgt,'dgt')
        if smaller_add < 0  :
            smaller_add = 0
            print('We achived to the minimum number that agreed ("0"),')
            print('We will check the bigger numbers with you now!')
            return smaller_add
    return smaller_add
def halve_division_mines(sm_first, sm_dgt):
    if sm_dgt == sm_first :
        sm_add = equal_sm_dgt(sm_dgt, sm_first)
        print(sm_add,'equal_sm_ddt returned add mines',sm_first,'firstin mines',sm_dgt,'dgt in mines')
        return sm_add
    elif sm_first > sm_dgt :
        sm_add = smaller_sm_dgt(sm_dgt, sm_first)
        return sm_add
def Small(sm_word,sm_dgt,sm_first):
    sm_count=100
    sm_chk=sm_word
    while sm_chk =='s' :
        print(sm_count)
        sm_number=(halve_division_mines(sm_first,sm_dgt))
        sm_dgt=sm_first
        sm_first=sm_number
        Print(sm_number)
        sm_chk=str(input('Please enter your choice: '))
        print(sm_first,'small', sm_dgt,'old',sm_number, 'it is mines output')
        sm_count +=1
    return sm_chk, sm_number, sm_first
def Yes():
    print('Hooraaaaay!!! I am very clever program :) ', 'isnt it ',name, '??? :))))))')
def Exit(word):
    print('Good game',name,'Have fun and see you soon!'' :) ')
    return 'y'
name = str(input('Please enter your name: '))
print('Hello',name)
# Time(3)
print('this is a matematical game, are you ready?! ')
# # for i in range(1,3):
#     Time(i)
#     print(i,'....')
print('Please guess a number between 0-100 ')
# Time(7)
Print(number)
chk=str(input('Please enter your choice: '))
chk1=chk
while chk != 'y' :
    if chk == 'b' :
        chk, number, first = (Big(chk,number,first))
        print(chk,number,first)
    elif chk == 's':
        print(first,number,'123123123')
        chk, number, first =(Small(chk,number,first))
    elif chk == 'e':
        chk=(Exit(chk))
    else:
        chk=input('Please choose the right answer: "Y" or "B" or "S" or "E"')
if chk1 == 'y' : 
    Yes()






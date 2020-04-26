import time
import random

def Print_starting_messages() :
        name =  str(input('Please enter your name : '))
        print('Hello', name)
        # Time(3)
        print('this is a matematical game, are you ready?! ')
        # # for i in range(1, 3) : 
        #     Time(i)
        #     print(i, '....')
        print('Please guess a number between 0-100 ')
        # Time(7)
        return name
def Print_instructions(guess) :
    print(' == == == == == == == == == == == == == == == == == = ')
    print('  I guess your NUMBER is ', guess, '!!')
    print(' == == == == == == == == == == == == == == == == == = ')
    print('If it is your NUMBER press "Y"')
    print('----------------------------------')
    print('If your NUMBER is bigger press "B"')
    print('----------------------------------')
    print('If your NUMBER is smaller press "S"')
    print('----------------------------------')
    print('if you want to exit press "E"')
    print('----------------------------------')
    return str(input('Please enter your choice : '))
def Print_messages(chk) :
    if chk == 'max' :
        print('We achived to the maximum old that agreed ("100"), ')
        print('We will check the smaller olds with you now!')
    elif chk == 'min':
        print('We achived to the minimum old that agreed ("0"), ')
        print('We will check the bigger olds with you now!')
left = 0
right = 100
guess = 50
yes = 'y'
name = Print_starting_messages()
Input = Print_instructions(guess)
while (Input !=  yes and Input != 'Y') :
    if Input == 'b' : 
        left = guess + 1
        guess = ( left + right)//2
        Input = Print_instructions(guess)
    elif Input == 's' : 
        right = guess - 1
        guess = ( left + right )//2
        Input = Print_instructions(guess)
    elif Input == 'e':
        print('Good game', name, 'Have fun and see you soon!'' : ) ')
        Input = yes
    else : 
        Input = input('Please choose the right answer : "Y" or "B" or "S" or "E"')
print('Hooraaaaay!!! I am very clever program : ) ', 'isnt it ', name, '??? : ))))))')
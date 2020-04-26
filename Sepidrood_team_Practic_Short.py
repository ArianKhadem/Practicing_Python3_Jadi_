number = 0
counter = 0
total = 0
while (number < 4) and (number >= 0) and (number != 2):
    number = int(input('0-1-3 for result of game or "4 for exit" : '))
    if (number != 4) and (number != 2):
        total = total + number
    counter = (counter + 1)
if number == 4 :
    counter = counter - 1
print('total scores of sepidrood team is :',total)
print('the number of game that sepidrood plyaed is: ',counter)
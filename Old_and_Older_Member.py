old = 10
older = 90
age=0
while age != -1:
    age = int(input('Please enter the age of members :'))
    if (age >= 10) and (age <= 90):
        if (older <= age) and (age != -1):
            oldest = age
            print('oldest: ',older)
        if (old >= age) and (age != -1):
            old = age
            print('youngest: ', old)
    else:
        print('Please enter the age between 10-99: ')
print('the older member: ',older,'this is the second member: ', old)
oldest = 10
youngest = 90
age=0
while age != -1:
    age = int(input('Please enter the age of members :'))
    if (age >= 10) and (age <= 90):
        if (oldest <= age) and (age != -1):
            oldest = age
            print('oldest: ',oldest)
        if (youngest >= age) and (age != -1):
            youngest = age
            print('youngest: ', youngest)
    else:
        print('Please enter the age between 10-99: ')
print(oldest, youngest)
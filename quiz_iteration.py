for i in range(10):
    if not i % 2 == 0:
        print(i+1)
        print(i)
#-------------------------------
x = input('number: ')
x=int(x)
count=0
c=0
for i in range(1,x):
    count+=1
    if (x%i==0):
        c+=1
if (c==1):
    print('okey')
else:
    print('Not Okey!')
print('The loop is doing for :', count)

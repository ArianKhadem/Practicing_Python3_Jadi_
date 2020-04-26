rooms = [1,2,3,4,5]
for i in rooms:
    print(i)
    if i == 5:
        print('reached the nice 5 :) ')
    break
    
i = 3
while i>=0:
   print(i)
   i = i - 1

i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

for i in range(10):
  if not i % 2 == 0:
    print(i+1)
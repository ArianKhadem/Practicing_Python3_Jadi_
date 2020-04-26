f2t = dict()
f2t['yek'] = 'bir'
f2t['do'] = 'ikki'
print(f2t)
ghad = {'jadi' : 180, 'hasan' : 200, 'zahra' : 167}
print(ghad['jadi'])
print(f2t)
ghad.keys()
print(len(f2t))
print(ghad.keys())
print(list(ghad.keys()))
print(ghad.values())
if 'jadi' in ghad:
    print('jadi')
string = 'Salam. Jadi is here and testing the python for fun'
counter = dict()
for letter in string:
    if letter in counter:
        counter[letter] += 1
        counter[letter] = counter.get(letter, 0) + 1
    else:
        counter[letter] = 1


print(counter)
for this_one in list(counter.keys()):
    print ('%s appeared %s times' % (this_one, counter[this_one]))
print(ghad.get('jadi', 1))
print(ghad.get('jaadi', 1))
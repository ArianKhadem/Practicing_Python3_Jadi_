the_name = input('Please enter your name: ')
# for i in (0, len(the_name)):
    # print(i,the_name(i))
the_lengh = len(the_name)
print(the_lengh)    
for letter in the_name: 
    print(letter)
Sentence = 'This is a sample !'
print(Sentence[0])
# Sentence[-8:] = 'Real not sample!'
print(Sentence)
print(Sentence[4:])
print('sa' in Sentence)
if Sentence < the_name:
    print('our name is longer than yours ! ',Sentence<the_name)
if Sentence != the_name:
    print('your name is not equal to ours:',Sentence != the_name)
print(Sentence.upper())
print(the_name.upper())
print(the_name.count('a'))
print(dir('the_name'))
# print(help(the_lengh))
print(Sentence.find('b'))
print(Sentence.find('i'))
print(Sentence.strip())
print(Sentence.lower())
print(Sentence.startswith('o'))
print(Sentence.startswith('t'))
print(Sentence.startswith('T'))
print(Sentence.lower().startswith('t'))
print('%s ;lsdj;alsdjfa;l %s S5djf' % (Sentence,the_name))

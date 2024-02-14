import random as r
space = ' '
print(space*10,end='')
for i in range(20):         # some basic styling for the intro
    print('*',end='')

print(f'\n{space*11}PASSWORD GENRATOR')

print(space*10,end='')

for i in range(20):     
    print('*',end='')
print()

upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerCase = upperCase.lower()
numbers = '0123456789'
specialCh = '!@#$%&*'

while True:

    length = int(input('Enter the length of your password\n(minimum length is 8): '))
    if length >= 8:
        break
    else:
        print('length should be atleast 8')
        
strength = input('Write the strength of your password(normal,strong,very strong) : ')

material = ''

if strength.lower() == 'normal':
    material+=lowerCase
    material+=numbers
elif strength.lower() == 'strong':
    material+=upperCase
    material+=lowerCase
    material+=numbers
elif strength.lower() == 'very strong':
    material+=upperCase
    material+=lowerCase
    material+=numbers
    material+=specialCh


test = ''.join(r.sample(material,length))
password = ''
if not(test in upperCase) and (strength.lower() == 'strong' or strength.lower() == 'very strong'):
    password = test[:length-1] + ''.join(r.sample(upperCase,1))
if not(test in lowerCase):
    password = password[:length-1] + ''.join(r.sample(lowerCase,1))
if not(test in numbers):
    password = test[:length-1] + ''.join(r.sample(numbers,1))
if not(test in specialCh) and (strength.lower() == 'very strong'):
    password = test[:length-1] + ''.join(r.sample(specialCh,1))
print(f'Your password is: "{password}"')




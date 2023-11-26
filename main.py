import random

char_bank = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[]\{}|;,./<>?'
print('Let\'s generate some passwords')
print('++++++++++++++++++++++++++++++')
len = int(input('Enter length of password(8 is recommended ):'))
nump = int(input('Enter number of passwords required :'))
print('Here are passwords : ')
print()
for pas in range(nump):
    result=''
    for i in range(len):
        result += random.choice(char_bank)
    print(result)

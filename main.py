from random import *

def generate_password(chars, lenght):
    password = ''
    
    for i in range(lenght):
       password += choice(chars)
       
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = []

count_passwords = int(input('Количество генерируемых паролей: '))
lenght_password = int(input('Длина каждого пароля: '))

numbers_bool = input('Включать ли цифры 0123456789? д - да, н - нет \n')
lowercase_bool = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д - да, н - нет \n')
uppercase_bool = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д - да, н - нет \n')
punctuation_bool = input('Включать ли символы !#$%&*+-=?@^_? д - да, н - нет \n')
not_bool = input('Исключать ли неоднозначные символы 1ilLo0O? д - да, н - нет \n')

if numbers_bool.lower() == 'д':
    chars.extend(digits)
if lowercase_bool.lower() == 'д':
    chars.extend(lowercase_letters)
if uppercase_bool.lower() == 'д':
    chars.extend(uppercase_letters)
if punctuation_bool.lower() == 'д':
    chars.extend(punctuation)
if not_bool.lower() == 'д':
    chars = [i for i in chars if i not in '1ilLo0O']
    
print(chars)
print(*[generate_password(chars,lenght_password) for _ in range(count_passwords)], sep = '\n')

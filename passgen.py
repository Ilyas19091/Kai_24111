import random
import string

def Survey(question):
    isAnswerCorrect = False
    while(not isAnswerCorrect):
        answer = input(question)
        if(answer.upper() == "ДА"): return True
        elif(answer.upper() == "НЕТ"):  return False
        else: print('Неопознанная команда. Попробуйте еще раз') 
      
seqOfUpper = string.ascii_uppercase
seqOfLower = string.ascii_lowercase
seqOfDigits = string.digits
seqOfSpecials = string.punctuation

sequence = []

isAnswerCorrect = False        
while(not isAnswerCorrect):
    passLength = int(input('Введите желаемую длину пароля: '))
    if(not (passLength < 0 or passLength > 30)): break
    else: print('Длина пароля не может быть меньше 8 или больше 30')

isUpperCase = Survey('Пароль должен содержать буквы в верхнем регистре? (Да/Нет): ')
isLowerCase = Survey('Пароль должен содержать буквы в нижнем регистре? (Да/Нет): ')
isDigits = Survey('Пароль должен содержать цифры? (Да/Нет): ')
isSpecials = Survey(f'Пароль должен содержать спецсимволы (~|\'\"@#$%^&!"№;%:?*()_+-=/\\{{}}[]:;.,<>) ? (Да/Нет): ')

if((isUpperCase or isLowerCase or isDigits or isSpecials) == False): 
    print('Вы ответили на все вопросы \"Нет\". Для генерации пароля будут использованы лишь буквы в нижнем регистре')
    isLowerCase = True

if(isUpperCase): sequence.extend(seqOfUpper) 
if(isLowerCase): sequence.extend(seqOfLower) 
if(isDigits): sequence.extend(seqOfDigits) 
if(isSpecials): sequence.extend(seqOfSpecials) 

password = [0] * passLength 

for i in range(passLength):
    password[i] = random.choice(sequence)
    
print(f'Ваш пароль: {"".join(password)}')
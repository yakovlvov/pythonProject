from random import *
sec = randint(1,100)
counter = 0
print("Добро пожаловать в угадайку")

def is_valid():
   if (n.isdigit() == True) and ((int(n) >= 1) and (int(n) <= 100)):
       return True
   else:
       return False

while True:
    n = input('Введите номер:')
    counter +=1
    if is_valid() == True:
        n = int(n)
        if n < sec:
            print('Число больше')
        elif n > sec:
            print('Число меньше')
        else:
            print(f'Угадал за {counter} попыток!')
            break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')





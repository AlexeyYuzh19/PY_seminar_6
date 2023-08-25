'''
6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Напишите функцию
- Аргументы: список чисел и границы диапазона
- Возвращает: список индексов элементов (смотри условие)
Примеры/Тесты:
lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
<function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
<function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
<function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
(*) Усложнение. Для формирования списка внутри функции используйте Comprehension
(*) Усложнение. Функция возвращает список кортежей вида: индекс, значение
Примеры/Тесты:
lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
<function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]
'''

# РЕШЕНИЕ

# Импорт модулей
import re
import random

# Функции
def inputArray():
    while True:
        values = input('Введите значения массива через пробел или с запятыми : ').replace(',', ' ').split()
        valArr = []
        for part in values:            
            if re.match('^[-+]?\d*\.?\d+$', part):
                valArr.append(float(part)) if '.' in part else valArr.append(int(part))
            elif len(part) > 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                valArr.append('слово')
            elif re.match('^[^a-zA-Zа-яА-ЯёЁ0-9]+$', part):
                valArr.append('символ')
            elif len(part) == 1 and re.match('^[a-zA-Zа-яА-ЯёЁ]+$', part):
                valArr.append('буква')
            elif re.match('^[-+]?\d+(\/\d+)?$', part):
                valArr.append('дробь')
            else:
                valArr.append('хз')
        yesArr = all(isinstance(value, (int, float)) for value in valArr)
        if len(valArr) > 0:
            if yesArr:                
                endArray = valArr
                if all(elem == 0 for elem in endArray):
                    print('Введены только нули.')
                    continue
                else:
                    break
            else:
                endArray = ' '.join(map(str, valArr))
                print(f'\033[31mОшибка!\033[0m Введены не все числа :\n{endArray}\nПовторите ввод.')
        else:
            print('\033[31mОшибка!\033[0m Вы не ввели последовательность чисел. Повторите ввод.')
    return endArray

def controlInput(phrase):
    element = input(f'Введите {phrase} : ')
    while not element.replace('-', '').replace('.', '', 1).isdigit() and not element.isdigit():
        element = input(f'\033[31mОшибка!\033[0m Повторите ввод - {phrase} \033[33m(число!)\033[0m : ')
    element = float(element)   
    return element

def positiveInteger(phrase):
    while True:
        try:
            posIn = int(input(f'Введите {phrase} : '))
            if posIn <= 0:
                print('\033[31mОшибка!\033[0m Значение должно быть больше нуля.')                 
                continue 
            break           
        except ValueError:
            print('\033[31mОшибка!\033[0m Введено не целое число.') 
    return posIn

def findIndex(listArr, min_val, max_val):
    index = []  
    for i in range(len(listArr)):
        if listArr[i] >= min_val and listArr[i] <= max_val:
            index.append(i)
    return index
# (*) Усложнение
def findIndexCort(listArr, min_val, max_val):
    index = [(i, listArr[i]) for i in range(len(listArr)) if listArr[i] >= min_val and listArr[i] <= max_val]
    return index

# Код
choice = input('\033[34mВыберите способ ввода элементов массива :\033[0m\n\033[32m" 1 " - набор с клавиатуры\033[0m \n\033[35m" 2 " - рандомно с заданием параметров\033[0m \n\033[36m"произвольный символ" - рандомно : \033[0m')
if choice == '1':
    resArray = inputArray()
elif choice == '2':
    minArr = controlInput('минимальное значение массива')    
    while True:
        maxArr = controlInput('максимальное значение массива')
        if maxArr < minArr:
            print('\033[31mОшибка!\033[0m Значение должно быть больше минимального.')                 
            continue 
        break        
    countArr = positiveInteger('количество чисел в массиве') 
    resArray = list(map(float, (round(random.uniform(minArr, maxArr), 3) for _ in range(countArr))))    
    if countArr > 2 and all(value == 0 for value in resArray):
                index = random.randint(0, len(resArray)-1)
                resArray[index] = 1
else:
    resArray = list(map(int, (random.randint(1, 100) for _ in range(25))))
print(f'Задан массив из {len(resArray)} элементов : \n\033[30m{resArray}\033[0m')
minVal = controlInput('минимум диапазона')
while True:
        maxVal = controlInput('максимум диапазона')
        if maxVal <= minVal:
            print('\033[31mОшибка!\033[0m Значение должно быть больше минимального.')                 
            continue 
        break 
resFir = findIndex(resArray, minVal, maxVal)
if len(resFir) == 0:     
    print('В заданном диапазоне [ {} _ {} ] искомые значения отсутствуют.\n'.format(minVal, maxVal))
else:
    print('Индексы элементов массива, значения которых принадлежат заданному диапазону [ {} _ {} ] :\n{}.\nКоличество индексов : {}.'.format(minVal, maxVal, resFir, len(resFir)))
    print(f'Cписок кортежей вида: индекс, значение - которые принадлежат заданному диапазону :\n{findIndexCort(resArray, minVal, maxVal)}\n')  
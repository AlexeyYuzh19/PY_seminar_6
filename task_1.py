'''
6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
Программа принимает от пользователя три числа :
Первый элемент прогрессии, Разность (шаг) и Количество элементов
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Напишите функцию
- Аргументы: три указанных параметра
- Возвращает: список элементов арифметической прогрессии.
Примеры/Тесты:
Ввод: 7 2 5
Вывод: [7 9 11 13 15]
Ввод: 2 3 12
Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
(*) Усложнение. Для формирования списка внутри функции используйте Comprehension
(**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, 
вам понадобится распаковка и Comprehension или map
'''
# РЕШЕНИЕ

# Импорт модулей
import re

# Функции
def inputArray(phrase):
    while True:
        values = input(f'Введите {phrase} через пробел или с запятыми: ').replace(',', ' ').split()
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
        checkArray = ' '.join(map(str, valArr))
        yesArr = all(isinstance(value, (int, float)) for value in valArr)
        if len(valArr) == 3 and str(valArr[2]).isdigit() and int(valArr[2]) >= 1:
            if yesArr:
                endArray = valArr
                break
            else:
                print(f'\033[31mОшибка!\033[0m Введены не все числа:\n{checkArray}\nПовторите ввод.')
        elif len(valArr) != 3 and len(valArr) != 0 :
            print(f'\033[31mОшибка!\033[0m Введено не три значения.\n{checkArray}\nПовторите ввод.')
        elif len(valArr) == 3 :
            if not str(valArr[2]).isdigit() or int(valArr[2]) < 1:
                print(f'\033[31mОшибка!\033[0m\n{checkArray}\n\033[33mВвод чисел.\033[0m "Количество элементов прогрессии" - \033[33mцелое положительное число\033[0m.')
        else:
            print('\033[31mОшибка!\033[0m Вы не ввели последовательность чисел. Повторите ввод.')
    return endArray

def arithProgress(firstEl, diff, elemCount):
    return [int(firstEl + (i * diff)) if float(firstEl + (i * diff)).is_integer() else round(firstEl + (i * diff), 3) for i in range(elemCount)]

# Код
firEl, dif, elemCo = inputArray('первый элемент, разность и количество элементов прогрессии')
print(f"\033[32mМассив, заполненный элементами арифметической прогрессии :\n\033[36m{arithProgress(firEl, dif, elemCo)}\n\033[0m")
import random
from random import randint
task = int(input('введите номер залачи от 1 до 5:'))
match task:
    case 1:
#         Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11
        number = float(input('Введите вещественное чило: '))
        sum = 0
        while number != int(number):
            number *= 10
        while number > 0:
            sum += number % 10
            number //= 10
        print('сумма цифр в цисле:')
        print(int(sum))

    case 2:
#         2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
        number = int(input('Введите число N: '))
        print('набор произведений чисел от 1 до N')
        factorial = 1
        for i in range(1,number+1):
            factorial*= i
            print(factorial, end=' ')
    case 3:
# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

        num = int(input('введите число: ')) 
        sum=0
        for x in range (1, num + 1):
            n=round((1 + 1 / x)**x) 
            sum+=n

        print('При n равном',{num})
        print("Сумма элементов",sum)

    case 4:
        # 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
        # Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
               
        def list(n):
            list = []
            for i in range(n):
                list.append(randint(-n, n))
            return list

        n = int(input('Введите число N: '))
        numbers = list(n)
        print(numbers)
        x = open('file.txt','r')
        result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
        print('сумма элементов из файла')
        print(result)
        
    case 5:
        # 5 Реализуйте алгоритм перемешивания списка.
        
        arr = [1, 2, 3, 4, 5, 6]
                
        print("Вот такой список имеем: ", arr)
                
        n = len(arr)
        print("Длинна списка: ", n)
        for _ in range(n):              # пробегаем по списку
            j = random.randint(0, n-1) # задаем произволный индекс
            element=arr.pop(j)          # удаляет элемент из списка с произвольным индексм и запоминаем в element
            arr.append(element)         # дописываем удаленный элемент в конец списка
        print("Вот что получилось: ",arr)
        
    case _:
        print('Это нам не задавали')

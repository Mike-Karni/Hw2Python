'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11'''

import main as sum


number = input("Введите число ")
print(main.sum(number))

print()
def Sum(num):
    sum = 0
    for i in range(len(num)):
        if num[i].isdigit():
            sum += int(num[i])
    return sum

number = input("Введите число ")

print(Sum(number))
'''Напишите программу, которая принимает на вход число N и выдает набор
произведений чисел от 1 до N.
Пример:
 пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''


'''
factorial =1
list= []
for i in range(1, n + 1):
    factorial *= i
    list.append(factorial)
print(list)'''
'''
def Factorial(n):
    factorial = 1
    list = []
    for i in range(1, n + 1):
        factorial *= i
        list.append(factorial)
    return list

print(Factorial(n))'''
import task2 as FunctionFile

n = int(input("Введи какуюнибудь херню " ))

print(FunctionFile.Factorial(n))

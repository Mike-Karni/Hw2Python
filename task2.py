def Sum(num):
    sum = 0
    for i in range(len(num)):
        if num[i].isdigit():
            sum += int(num[i])
    return sum

def Factorial(n):
    factorial = 1
    list = []
    for i in range(1, n + 1):
        factorial *= i
        list.append(factorial)
    return list

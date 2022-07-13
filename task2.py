def Sum(num):
    sum = 0
    for i in range(len(num)):
        if num[i].isdigit():
            sum += int(num[i])
    return sum
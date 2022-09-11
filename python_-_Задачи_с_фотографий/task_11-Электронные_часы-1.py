# Входные данные:150

# Вывод программы:2 30

n = int(input())
if n < 1440:
    print (n // 60)
    print (n % 60)
else:
    a = 1440 - n
    a *= -1
    print(a // 60)
    print (a % 60)

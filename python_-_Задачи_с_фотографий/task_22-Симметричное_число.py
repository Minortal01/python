# Входные данные:
# 2002

# Вывод программы:
# 1

a = int(input())
b = (a % 10) * 1000
c = ((a//10)%10)*100
x = ((a//100)%10)*10
z = (a//1000)%10
y = b + c + x + z
print(a - y + 1)

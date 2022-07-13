# Допишите программу для нахождения числа сочетаний из n по k
# (значения вводятся в программе)
# Sample Input:6 3
# Sample Output:20
# ввод данных
import math
n, k = map(int, input().split())
c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(math.trunc(c))

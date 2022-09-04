# Входные данные:
# 10
# 3
# 2

# Вывод программы:
# 8

import math
h = int(input())
a = int(input())
b = int(input())
x = (h - a) / (a - b)
print(math.ceil(x + 1))

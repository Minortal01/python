#Sample Input:6 3
#Sample Output:20
# ввод данных
n, k = map(int, input().split())
# здесь продолжите программу
import math
c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(math.trunc(c))
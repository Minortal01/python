# В летний лагерь нужно отвести n детей и m вожатых с помощью автобусов. Максимальная вместимость каждого автобуса 20 человек.
# Допишите программу для вычисления минимального числа автобусов, необходимых для перевозки детей вместе с вожатыми. Результат выведите в консоль в виде целого числа.
#Sample Input:40 5
#Sample Output:3
# ввод данных
n, m = map(int, input().split())
# здесь продолжите программу
import math
print(math.ceil((n+m)/20))

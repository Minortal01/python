#Допишите текст программы для вычисления евклидового расстояния (гипотенузы) по перемещениям a и b.
#Sample Input:3 4
#Sample Output:5.0
import math
a, b = map(int, input(). split())
x = (math.sqrt(a**2 + b**2 ))
print(round(x, 2))

#Вводится вещественное число. Нужно проверить, что оно попадает или в диапазон [0; 2] или в диапазон [10; 20] (включительно).
#На экран вывести True, если попадает и False - в противном случае.
#Задача делается без использования условного оператора.

#Sample Input:1.2
#Sample Output:True

# put your python code here
a = float(input())
print((a <= 2 and a >= 0) or (a <= 20 and a >= 10))
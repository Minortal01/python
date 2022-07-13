# Напишите программу ввода двух слов через пробел.
# Сформируйте новую строку, продублировав первое слово дважды,
# а второе-трижды (все слова в результирующей строке должны идти через пробел).
# Результат выведите на экран.

# Sample Input:
# hello python
# Sample Output: hello hello python python python

# put your python code here
a, b = input().split()
s1 = ((a+' ') * 2) + ((b+' ')*3)
print(s1)

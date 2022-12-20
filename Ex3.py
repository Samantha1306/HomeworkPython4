# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [int(i) for i in input('Введите числа через пробел: ').split()]
newlist=[]
[newlist.append(i) for i in list if i not in newlist]
print(newlist)
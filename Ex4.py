# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введите натуральную степень числа: "))

koef=[randint(0,100) for i in range(k)]+[randint(1,100)]
x='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koef) if j][::-1])
x=x.replace('x^0', '')
x+=('','1')[x[-1]=='+']
x=(x, x[:-2])[x[-2:]=='^1']
print(x)


file = open('file.txt', 'w')
file.write(x)
file.close()

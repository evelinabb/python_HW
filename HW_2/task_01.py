# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


import random

n = int(input('Введите количество монеток => '))
monetki = []
for i in range(n):
    a = random.randint (0,1)
    monetki.append(a)
print(monetki)

o = 0
r = 0
for i in monetki:
    if monetki[i] == 0:
        o += 1
    if monetki[i] == 1:
        r += 1

print(o)
print(r)

if o < r:
    print(o)
else:
    print(r)

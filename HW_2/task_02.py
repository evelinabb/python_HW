# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y 
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать 
# задуманные Петей числа.

import random
import math

x = random.randint(0,1000)
y = random.randint(0,1000)

print(x)
print(y)

s = x + y
p = x * y

print(s)
print(p)

y = (s - math.sqrt(s**2-4*p))/2 
x = s - y

print(x)
print(y)


# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)
#а данное решение не совсем поняла 
import random

num1=random.randint(1, 29)
num2=random.randint(1, 29)
num3=random.randint(1, 29)
while num1==num2 or num2==num3:
    num1=random.randint(1, 29)
    num2=random.randint(1, 29)
    num3=random.randint(1, 29)
print('A sua primeira terra é a:',num1)
print('A sua segunda terra é a:',num2)
print('A sua terceira terra é a:',num3)
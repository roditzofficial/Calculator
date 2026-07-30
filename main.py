import math
firstnum = 0
sign = 0
secondnum = 0
result = 0
exited = False

print('RoditzCalculator')
print('Type in your calculations in the following order: First number, the sign, and the second number')
print('Currently, you can only make + - / and * ecuations')
print('If at any point you want to close this calculator, just type exit when you have to place the sign or Ctrl + C (I would appreciate if you do the first one, ty)')

def calc():
    if sign == '+':
        result = firstnum + secondnum
        print(f'The result is {result}')
    elif sign == '-':
        result = firstnum - secondnum
        print(f'The result is {result}')
    elif sign == '/':
        result = firstnum / secondnum
        print(f'The result is {result}')
    elif sign == '*':
        result = firstnum * secondnum
        print(f'The result is {result}')

while exited == False:

    firstnum = int(input())
    sign = input()
    secondnum = int(input())

    if sign == 'exit':
        exited = True
    else:
        calc()

    if exited == True:
        break
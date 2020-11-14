##################################################################
#Tasks: 7
'''7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя
яка б приймала 3 аргументи - один з яких операцiя, яку зробити!'''
###################################################################
def fun_operation(a,b,c):
    if operation == '+':
        rez=(a+b)
        print('sum: ',rez)
    elif operation == '-':
        rez=a-b
        print('difference: ',rez)
    elif operation == '*':
        rez=a*b
        print('product: ',rez)
        
    return rez

n1 = float(input('Input the first number: '))
n2 = float(input('Input the second number: '))
operation= input('Input the operation + – *  ')
reply=fun_operation(n1,n2,operation)
########################################################
'''Task 5. Написати функцію < fibonacci >, яка приймає
один аргумент і виводить всі числа Фібоначчі,
що не перевищують його.'''
def fibonacci(n):
    fib = []
    a = 0
    b = 1
    for i in range(n):
        a , b = b , a+b
        fib.append(a)
        #print(a, end=' ')
    print('Fibonacci numbers ->',fib)
    return fib
##############################
n=int(input('Input number fibonacci n = '))
fibonacci(n)
  
    



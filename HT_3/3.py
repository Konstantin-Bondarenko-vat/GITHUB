##########################################################################
'''Task 3. Написати функцию < is_prime >, яка прийматиме 1
аргумент - число від 0 до 1000, и яка вертатиме True,
якщо це число просте, и False - якщо ні.'''
###################################
def is_prime(x):
    n=0
    for i in range(1,x):
        if x%i==0:
            n+=1
    if n>2:
        result=False
    else:
        result=True
    
    return result
#####################################
x=int(input('Input->(2-1000): '))
if x>1 and x<=1000:
    print(is_prime(x))
else:
    x=int(input('Input->(2-1000): '))




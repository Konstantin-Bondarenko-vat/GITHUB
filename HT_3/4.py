##########################################################################
'''Task 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи
- початок і кінець діапазона, і вертатиме список простих чисел всередині
цього діапазона.'''
##################################################
def prime_list(diapazon_n, diapazon_k):
    st=[]
    for num in range(diapazon_n, diapazon_k+1):
        n = 0
        delitel = 2
        while delitel < num:
            if num % delitel == 0:
                n += 1
            delitel += 1
        if n == 0:
            st.append(num)     
    
    return st
####################################
begin_range = int(input('Input begin_range: '))
end_range = int(input('Input end_range : '))

if begin_range <= 2 or begin_range > 1000:
    begin_range = int(input('Input begin_range: '))
if end_range < begin_range or end_range >1000:
    end_range = int(input('Input end_range : '))
st = prime_list(begin_range,end_range)
print(st) 
 
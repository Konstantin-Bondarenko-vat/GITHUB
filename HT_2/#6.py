#################################################################
# Tasks: 6
'''6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno
400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"->
просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього,
   яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину,
кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо
рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя'''
###################################################################
def fun_1(st):
    sum=0
    length_st=len(st)     
    n_numbers=0
    letters=[]
        
    for i in range(len(st)):
        for k in range(9):
            if str(k)==st[i]:
                sum+=int(st[i])
                print(type(k))
                st
                del st[i]
                
    print('sum= ',sum)
    print('letters= ',st)
    return   
######################################################    
def fun_2(st):
    
    length_st=len(st)
    print('length_st=',length_st,)
    n_numbers=0
    for i in range(len(st)):
        for k in range(10):
            if st[i]==str(k):
                n_numbers+=1
                n_letters=length_st-n_numbers
    print('n_numbers=',n_numbers,)
    print('n_letters=',n_letters)
    return 
##############################################################
st=input('Input string: ')

if len(st)<10:
    rez=fun_1(st)

if len(st)>=10 and  len(st)<=50:
    rez=fun_2(st)



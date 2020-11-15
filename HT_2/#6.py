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
-  якщо довжина бульше 50 - > ваша фантазiя...прінтує числа з рядка'''
###################################################################
def fun_1(string):
    sum=0
    letters=''
    for i in range(0,len(string)):
#       if string[i].isnumeric():
        if string[i].isdigit():
            sum+=int(string[i])
        else:        
            letters+=string[i]                                        
    print('sum = ',sum)
    print('letters: ',letters)
    return   
######################################################    
def fun_2(string):
    length_st=len(string)
    print('length_st=',length_st,)
    n_numbers=0
    for i in range(len(string)):
        if string[i].isnumeric():
                n_numbers+=1
                n_letters=length_st-n_numbers
    print('n_numbers=',n_numbers,)
    print('n_letters: ',n_letters)
    return 
##############################################################
def fun_3(string):
    string_numbers=''
    for i in range(0,len(string)):
#       if string[i].isnumeric():
        if string[i].isdigit():
            string_numbers+=string[i]
                    
    print('string_numbers: ',string_numbers)
    
    return  
##############################################################

string=input('Input string: ')

if len(string)<30:
    result=fun_1(string)

if len(string)>=30 and len(string)<=50:
    result=fun_2(string)

if len(string)>50:
    result=fun_3(string)
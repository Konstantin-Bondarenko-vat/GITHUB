#########################################################################
'''Task 8. Написати функцію, яка буде реалізувати логіку циклічного зсуву
елементів в списку. Тобто, функція приймає два аргументи: список і величину
зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його
кінець). Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
'''
#######################################
def fun_lan(List, shift):
    
    if shift > 0:
        for i in range(shift):
            List.insert(0,List[-1])
            List.pop(-1)
    elif  shift < 0:
        for i in range(0,abs(shift)):
            List.append(List[0])
            List.remove(List[0])
   
    print('Output list ->',List)
    return List
########################################
#List=list(input('Input List:'))
List=[1, 2, 3, 4, 5]
print('Input list -> ',List)
shift=int(input( 'Input shift -> '))
fun_lan(List, shift)
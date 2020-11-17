#########################################################
''' Task 7. Написати функцію, яка приймає на вхід список
 і підраховує кількість однакових елементів у ньому.'''
def fun_count(List):
    dict_n = {i: List.count(i) for i in List}
    print(dict_n)
    return dict_n
#############################
list_input=list(input('Input list: '))
fun_count(list_input)
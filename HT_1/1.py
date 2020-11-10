####################################Tasks:
# 1 .Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#         Sample data : 1, 5, 7, 23
#         Output :
#         List : [‘1', ' 5', ' 7', ' 23']
#         Tuple : (‘1', ' 5', ' 7', ' 23')


L=input('Input data: ')
L=L.replace(', ','')
print('List :',list(L))
print('Tuple :',tuple(L))
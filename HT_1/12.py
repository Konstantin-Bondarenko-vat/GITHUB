####################################Tasks:
#10. Write a script to concatenate following dictionaries to create a new one.
#       Sample Dictionary :
#       dic1={1:10, 2:20}
#       dic2={3:30, 4:40}
#       dic3={5:50,6:60}
#       Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5: 50,6: 60}
print('dic1 = {1:10, 2:20}')
print('dic2 = {3:30, 4:40}')
print('dic3 = {5: 50,6: 60}')
dic_N={}
dic_N.update(dic1)
dic_N.update(dic2)
dic_N.update(dic3)
print(dic_N)

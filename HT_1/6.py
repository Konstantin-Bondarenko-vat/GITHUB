####################################Tasks:
#6. Write a script to check whether a specified  is contained in a group of values.
#       Test Data :
#       3 -> [1, 5, 8, 3] : True
#       -1 -> (1, 5, 8, 3) : False
s=int(input('Input value: '))
a=[1, 5, 8, 3]
i=0
flag=0
while i<len(a) and flag==0:
    if s==a[i]:
        flag=1
    i = i+1
if flag==1:
    print(s,'->',a, ':True')
else:
    print(s,'->',a, ':False')
 

####################################Tasks:
#4. Write a script to concatenate N strings.
n=input('N strings ? ')
st=''
for i in range(int(n)):
    print('Input strings #',i+1,'+ Enter: ')
    st1=input()
    st+=st1+' '
print(st) 
####################################Tasks:
#8. Write a script to replace last value of tuples in a list.
#       Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#       Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
L=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print('Sample list:    ',L)
n=len(L)
s=[]
for i in range(len(L)):
   s+=L[i]
for i in range(2,len(s),3):
    s[i]=100
L=[]
N=()
i=0
while i<(len(s)):
    N=tuple(s[i:n+i])
    L.append(N)
    i=i+n
print('Expected Output:',L)
#9. Write a script to remove an empty tuple(s) from a list of tuples.
#        Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
L=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print('Sample data: ',L)
LN=[]
N=()
for i in range(len(L)):
    if L[i]!=():
       N=tuple(L[i])
       LN.append(N)
print('Expected output: ',LN)
####################################Tasks:
#7. Write a script to concatenate all elements in a list into a string and print it.
L=list(input('Input list: '))
print(L)
S=str()
for i in range(len(L)):
    S=S+(L[i])
print(S)
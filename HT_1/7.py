
#7. Write a script to concatenate all elements in a list into a string and print it.
L=['He', 'll', 'o']
print(L)
S=('')
for i in range(len(L)):
    S=S+L[i]
print(S)
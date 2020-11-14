####################################Tasks:
#11. Write a script to remove duplicates from Dictionary.

a={1: 10, 2: 20, 3: 23, 4: 40, 5: 50, 6: 60}
print(a)
b={}
for i in range(len(a)): 
    for k in range(len(a)):
         b.update(a)            
print(b)
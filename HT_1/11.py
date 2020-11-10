####################################Tasks:
#11. Write a script to remove duplicates from Dictionary.

a={1: 100, 2: 20, 3: 100, 4: 100, 5: 50, 6: 100}
print(a)
Len=len(a)
print(Len)

for i in range(0,len(a)-1):    
    if a[i]==a[i+1]:
        print  ('is a duplicate') 
        
print(a)   
    
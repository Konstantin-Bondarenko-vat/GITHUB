##################################### Завдання:
#5. Write a script to convert decimal to hexadecimal
#		Sample decimal number: 30, 4
#		Expected output: 1e, 04

i=int(input('Input decimal number: '))
i10=i
i16=str(hex(i))
for i in range(len(i16)):
    i16=i16.replace('x','')
if len(i16)>2:
    for i in range(len(i16)):
        i16=i16.replace('0','')   
print(i10,'=',i16)
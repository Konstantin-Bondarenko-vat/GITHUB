##############################################
'''Tasks: 4
Знайти: чи iснує трикутник, тип трикутника, яка площа трикутника''' 
###############################################
def tr_f_t (a,b,c):     
    if ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
        triangles_f_t=True
    else:   
        triangles_f_t=False
    return triangles_f_t
################################################
def tr_typ (a,b,c):   
    if (a == b) and (b == c) and (c == a):
        triangle='Трикутник рівносторонній'
    elif a == b or b == c or c == a:
        triangle='Трикутник рівнобедренниц'
    else:
       triangle='Трикутник різносторонній'
        
    return triangle
#################################################
def perimeter2(a,b,c):
    p2 = float((a+b+c)/2)
    return p2
#################################################
def s(a,b,c,p2):
    p2 = float(p2)
    tr_square = ((p2-a)*2+(p2-b)*2+(p2-c)*2) ** 0.5
    return tr_square
##################################################
a = float(input('Input side of the triangle a = '))
b = float(input('Input side of the triangle b = '))
c = float(input('Input side of the triangle c = '))

if (tr_f_t (a,b,c)) == True:
    print(tr_f_t (a,b,c))
    print(tr_typ (a,b,c))
else:
    print('not triangle')
    print('triangles False')
    a = float(input('Input side of the triangle a = '))
    b = float(input('Input side of the triangle b = '))
    c = float(input('Input side of the triangle c = ')) 

p2 = perimeter2(a,b,c)
s=s(a,b,c,p2)
s=round(s,2)
print('s = ',s)
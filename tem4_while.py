


'''
x=0

while x <= 10:
    print(x)
    x+=1
numer: 7

7x1=7
7x2=14
7x3=21
.
.
.
7x10=70
fin
'''

print("Dame un número y yo te doy una tabla ")
num1 = input("Num1: ")
y=0

while y <= 10:
    print("{}x{}={}".format(num1,y,int(num1)*y))
    y+=1

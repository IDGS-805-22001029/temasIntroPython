
'''
En java
for(int i=0; i<29; i++) 
'''
#Aquí le decimos donde termina (0-9)
print(list(range(10)))

#Aquíe le decimos donde empieza y donde termina (1-19)
print(list(range(1,20)))

#Aquí le decimos donde empieza, donde termina y de cuanto en cuanto avanza
print(list(range(0,20,2)))

tem1=list(range(10))
tem2=range(10)
print(type(tem1))
print(type(tem2))


#En python se puede hacer un for con un range
for i in range(1,10,2):
    print(i)


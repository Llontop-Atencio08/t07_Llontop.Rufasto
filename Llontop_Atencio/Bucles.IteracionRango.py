#Ejercicio01
i=0
s=0
max=50
while(i<=max):
    i+=1
    if((i%2)==0):
        s=s+2
        #fin_si
#fin_while
print("suma pares:",s)
s=0
for i in range (51):
    if((i%2)==0):
        s=s+i
    #fin_if
#fin_for
print("suma pares:",s)


#Ejercicio02
#Numeros pares del 0 al 100
n=0
while(n<=100):
    print(n)
    n+=2
#fin_while
n=0
for n in range (100):
    print(n)

#fin_for


#Ejercicio03
#suma de la serie
i=0
s=0
max=30
while(i<=max):
    i+=3
    if((i%2)==0):
        s=s+10
        #fin_si
#fin_while
print("suma:",s)
s=0
for i in range (31):
    if((i%2)==0):
        s=s+i
    #fin_if
#fin_for
print("suma:",s)

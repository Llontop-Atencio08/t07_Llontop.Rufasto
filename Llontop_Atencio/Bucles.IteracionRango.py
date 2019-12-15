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

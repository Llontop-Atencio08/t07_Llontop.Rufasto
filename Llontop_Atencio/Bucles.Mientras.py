edad=22
edad_invalida=(edad<25 or edad>100)
while(edad_invalida):
    edad=int(input("ingrese edad:"))
    edad_invalida=(edad<25 or edad >100)
#fin_while
print("edad valida:",edad)

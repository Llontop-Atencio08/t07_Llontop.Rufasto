edad=22
edad_invalida=(edad<25 or edad>100)
while(edad_invalida):
    edad=int(input("ingrese edad:"))
    edad_invalida=(edad<25 or edad >100)
#fin_while
print("edad valida:",edad)



#Ejercicio02
hemoglobina=10
hemoglobina_invalida=(hemoglobina<13 or hemoglobina>16)
while(hemoglobina_invalida):
    hemoglobina=float(input("ingrese hemoglobina:"))
    hemoglobina_invalida=(hemoglobina<13 or hemoglobina>16)
#fin_while
print("hemoglobina valida:",hemoglobina)

Ejercicio01
#Pedir edad de ingreso a la escuela PNP
edad=10
edad_invalida=(edad<16 or edad >25)
while(edad_invalida):
    edad=int(input("ingrese edad:"))
    edad_invalida=(edad<16 or edad >25)
#fin_while
print("edad valida:",edad)


#Ejercicio02
#Pedir nota de sustentacion de tesis
nota=0
nota_desaprobada=(nota<12 or edad >20)
while(nota_desaprobada):
    nota=int(input("Ingrese nota:"))
    nota_desaprobada=(nota<12 or edad >20)
#fin_while
print("Nota aprobada:",nota)


#Ejercicio03
#Pedir puntaje minimo para ingresar a la UNPRG
puntaje=12.20
puntaje_invalido=(puntaje<90.00 or puntaje>300.00)
while(puntaje_invalido):
    puntaje=float(input("Ingrese puntaje:"))
    puntaje_invalido=(puntaje<90.00 or puntaje>300.00)
#fin_while
print("Puntaje alcanzado:",puntaje)


#Ejercicio04
#Pedir ponderado de un alumno para ver si ocupa el tercio superior
ponderado=9.6
ponderado_no_valido=(ponderado<15.00 or ponderado>20.00)
while(ponderado_no_valido):
    ponderado=float(input("Ingrese ponderado:"))
    ponderado_no_valido=(ponderado<15.00 or ponderado>20.00)
#fin_while
print("Ponderado valido:",ponderado)


#Ejercicio05
#Pedir temperatura de una persona
temperatura=23.0
temperatura_alta=(temperatura<35.0 or temperatura>38.0)
while(temperatura_alta):
    temperatura=float(input("Ingrese temperatura:"))
    temperatura_alta=(temperatura<35.0 or temperatura>38.0)
#fin_while
print("Temperatura normal:",temperatura)


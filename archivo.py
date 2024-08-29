#Ingrese 10 edades de las cuales 
#muestre cuantos son mayores de edad
#y sume las edades que cumplan la condicion.
#a=0
#suma=0
#for b in range(1,11):
#    edad=int(input("Ingrese su edad:"))
#    if edad>=18:
#        print("Es mayor de edad:")
#        a=a+1
#        suma=suma+edad
#    else:
#        print("Es menor de edad:") 
#print("Cantidad de mayores de edad:", a)
#print("Suma de mayores de edad", suma)

#crear un programa que permita e ingreso de n cantidad de valores
#enteros, de los cuales se desea saber
#cuantos valores positivos,cuantos negativos y cuantos neutros, sumar los valores positivos.
positivo=0
negativo=0
neutro=0
suma=0
n=int(input("Cuantos numeros va a ingresar:"))
for x in range(n):
    b=int(input("Ingrese un numero:"))
    if b>0:
        print("Es positivo")
        positivo=positivo+1
        suma=suma+b
    elif b<0:
        print("Es negativo")
        negativo=negativo+1
    else:
        print("Es neutro")
        neutro=neutro+1
print("Suma de positivos", suma)
print("cantidad de positivo", positivo)
print("cantidad de negativos", negativo)
print("cantidad de neutros", neutro)
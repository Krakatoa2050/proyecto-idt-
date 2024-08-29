
'''for i in range(5):
    print("Hoy es juernes",i)

for i in range(1,6):
    print("Quiero plata...")
'''

'''p=0
for i in range(10):
    a=int(input("Ingrese un valor:"))
    if a>0:
        p=p+1
print("Cantidad de positivos:",p)

n=int(input("Ingrese la cantidad:"))
'''

'''superficie=0
n=int(input("Ingrese una cantidad:"))
for i in range(n):
    base=int(input("Ingrese el valor de la base:"))
    altura=int(input("Ingrese el valor de la altura:"))
    area=(base*altura)/2
    print("Area:",area)
    if area>12:
        superficie=superficie+1
print("Cantidad de triangulos con area mayor a 12:",superficie)
'''
cero=0
posi=0
nega=0
for i in range(10):
    v=int(input("Ingrese un valor:"))
    if v==0:
        cero=cero+1
    elif v>=0:
        posi=posi+1
    elif v<0:
        nega=nega+1
print("Cantidad de valores iguales a cero:",cero)
print("Cantidad de valores positivos:",posi)
print("Cantidad de valores negativos:",nega)
    





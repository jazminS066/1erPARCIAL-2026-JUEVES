#Escribir una funcion iterativa que calcule la cantidad total de donas consumidas en una fiesta.
# Recibe como parametros dos numeros (naturales) a (donas por persona) y b (cantidad de personas), y
#devuelve el total de donas consumidas.
a= int(input("Cant. de donas consumidas: "))
b= int(input("Cant. de personas: "))
def total_donas(a,b):
    total= 0
    for x in range (b):
        total+= a
    return total
print("Total de donas: " total_donas)
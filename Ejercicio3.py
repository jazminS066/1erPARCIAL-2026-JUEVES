#Escribir una función recursiva que calcule cuántas veces Bart ha interrumpido a Marge.
#Recibe como parámetros dos números (naturales) a (interrupciones por hora) y b (horas de la tarde),
# y devuelve el total de interrupciones.
a= int(input( "Interrupciones por hora: "))
b= int(input ( "Hora de la tarde: "))
def interrupciones(a,b):
    if b <= 0:
        return= 0
    else:
        return a + interrupciones (a, b-1) 
print("Total de interrupciones: ", interrupciones(a,b))
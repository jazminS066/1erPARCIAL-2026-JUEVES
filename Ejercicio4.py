#Escribir una función que reciba dos parámetros: (i) una lista desordenada de "eventos"
#(ej: "Kermés", "Concurso de Comida", "Reunión del Concejo Municipal");
#y (ii) una expresión booleana (que puede ser evaluada a True o False).
#si el valor de la expresión es True, la lista de eventos se ordenará alfabéticamente
# en orden descendente (de la Z a la A). En caso contrario,
# se ordenará de forma ascendente (de la A a la Z). Por defecto, si la función es llamada
# sin una "expresión" (solo la lista de eventos), la lista debe retornar ordenada de forma ascendente.
eventos=["Kermes","Concurso de comida", "Reunion del Concejo Municipal"]
def ordenar_eventos(eventos:list, expression: bool= False):
    if not isistance (expression, bool):
        raise TypeError("La expresion debe ser un booleano")
    ordenados []
    for evento in eventos:
        ordenados.append(evento)
    ordenados.sort(reverse= expression)
    return ordenados
print(ordenar_eventos(eventos))
print(ordenar_eventos, True)
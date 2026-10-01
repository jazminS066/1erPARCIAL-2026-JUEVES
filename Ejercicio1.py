#Generar una lista por compresi0n que contenga la cantidad de donas que Homero consume en el infierno.
#Por cada dona que Homero consume apareceran mas donas al ritmo de raiz de dos donas (raiz de 2)
# en su suplicio hasta que reviente.
#Ejemplo: { 1: 1, 2: 1.41421356237, 3: 2, 4: 2.82842712475, 5: ... }
donas= "Canti. de donas que consume homero: "
n= int(input(donas))
lista_donas = [ 2** ((x-1)/2) for x in range(1, n + 1)]
print(lista_donas)
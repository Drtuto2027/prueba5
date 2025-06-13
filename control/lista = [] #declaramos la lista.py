lista = [] #declaramos la lista
for i in range(10): #usamos un ciclo para solicitar los datos
    n = int(input('Ingrese el numero a ingresar en la lista: '))
    lista.append(n) #ingresamos los datos a la lista

# Inicializamos el menor con el primer elemento de la lista
menor = lista[0]
# Inicializamos la posición del menor con 0 (la posición del primer elemento)
posicion = 0

for i in range(1, len(lista)):
    # Comparamos el elemento actual con el menor encontrado hasta ahora
    if lista[i] < menor:
        # Si encontramos un elemento más pequeño, lo actualizamos como el nuevo menor
        menor = lista[i]
        # Actualizamos la posición del menor con la posición actual en la lista
        posicion = i


print("La lista es",lista,'el numero menor de la lista es,',menor,'Ubicado en la posición',posicion)






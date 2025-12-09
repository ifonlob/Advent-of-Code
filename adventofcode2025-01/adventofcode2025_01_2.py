with open("./input.txt", "r") as archivo:
    lineas = list(archivo)

contador_numero_seguros = 0

def es_seguro(lista):
    if len(lista) < 2:
        return False
    if (lista == sorted(lista) or lista == sorted(lista, reverse=True)):
        for i in range(len(lista) - 1):
            if not (1 <= abs(lista[i] - lista[i+1]) <= 3):
                return False
        return True
    return False

for linea in lineas:
    numeros = list(map(int,linea.split()))
    segura = es_seguro(numeros)
    if segura:
        contador_numero_seguros += 1
    else:
        dampener_aplicado = 0
        for j in range(len(numeros)):
            modificado = numeros[:j] + numeros[j+1:]
            if es_seguro(modificado):
                dampener_aplicado = 1
        contador_numero_seguros += dampener_aplicado

print(contador_numero_seguros)

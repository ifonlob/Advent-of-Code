with open("./input.txt", "r") as archivo:
    lineas = list(archivo)

contador_numero_seguros = 0

def sacar_menor(numeros):
    menor = float('inf')
    for numero in numeros:
        if numero < menor:
            menor = numero
    numeros.remove(menor)
    return menor
                   
for linea in lineas:
    i = 0
    numeros_ordenados = []
    contador = 0
    numeros = list(map(int,linea.split()))
    numeros_copy = numeros.copy()
    for _ in range(len(numeros_copy)):
        menor = sacar_menor(numeros_copy)
        numeros_ordenados.append(menor)
    if numeros == numeros_ordenados or numeros == numeros_ordenados[::-1]:
        while i < len(numeros) - 1:
            if 1 <= abs(numeros[i] - numeros[i + 1]) <= 3:
                contador += 1
            i += 1
        if contador == len(numeros) - 1:
            contador_numero_seguros += 1                    
print(contador_numero_seguros)
        
    
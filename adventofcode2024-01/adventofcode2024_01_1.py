lista_ordenada_izquierda = []
lista_ordenada_derecha = []

def cargar_listas():
    with open("./input.txt", "r") as archivo:
        lineas = list(archivo)
    numero_lineas = len(lineas)
    izquierda = []
    derecha = []
    for linea in lineas:
        numero1, numero2 = map(int, linea.split())
        izquierda.append(numero1)
        derecha.append(numero2)

    def sacar_menor(izquierda, derecha):
        menor_izq = float('inf')
        menor_der = float('inf')
        for numero in izquierda:
            if numero < menor_izq:
                menor_izq = numero
        for numero in derecha:
            if numero < menor_der:
                menor_der = numero
        izquierda.remove(menor_izq)
        derecha.remove(menor_der)
        return menor_izq, menor_der

    for i in range(numero_lineas):
        menor_izq, menor_der = sacar_menor(izquierda, derecha)
        lista_ordenada_izquierda.append(menor_izq)
        lista_ordenada_derecha.append(menor_der)
    return lista_ordenada_izquierda,lista_ordenada_derecha
if __name__ == "__main__":
    cargar_listas()
    acumulador_distancia = 0
    for j in range(len(lista_ordenada_izquierda)):
        distancia = abs(lista_ordenada_izquierda[j] - lista_ordenada_derecha[j])
        acumulador_distancia += distancia

    print(lista_ordenada_derecha)
    print(lista_ordenada_izquierda)
    print(acumulador_distancia)

from adventofcode2024_01_1 import cargar_listas
lista_ordenada_izquierda,lista_ordenada_derecha = cargar_listas()
contador = 0
puntuacion = 0
suma_puntuacion = 0
for numero_izq in lista_ordenada_izquierda:
    contador = 0
    for numero_der in lista_ordenada_derecha:
        if numero_izq == numero_der:
            contador += 1
    puntuacion = numero_izq * contador
    suma_puntuacion += puntuacion
print(suma_puntuacion)
        
    
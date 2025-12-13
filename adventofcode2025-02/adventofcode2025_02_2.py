import sys
def leer_archivo() -> list[str]:
    try:
        with open('input.txt', "r") as archivo:
            texto = archivo.read().strip()
            lista_rangos = texto.split(",")
        return lista_rangos
    except FileNotFoundError:
        print(f"Error. Archivo 'input.txt' no encontrado")
        sys.exit(1)

def obtener_ids_invalidos(rangos:list[str])->int:
    contador = 0
    for rango in rangos:
        numeros = rango.split("-")
        numero1 = int(numeros[0])
        numero2 = int(numeros[1])
        for numero in range(numero1,numero2 + 1):
            numero_invalido_encontrado = False
            k = 2
            numero_cadena = str(numero)
            longitud_numero = len(numero_cadena)
            while k < (longitud_numero + 1) and not numero_invalido_encontrado:
                if longitud_numero % k == 0:
                    if numero_cadena[:(longitud_numero//k)] * k == numero_cadena:
                        contador += numero
                        numero_invalido_encontrado = True
                k += 1
    return contador

def main():
    rangos = leer_archivo()
    contador = obtener_ids_invalidos(rangos)
    print(contador)

if __name__ == "__main__":
    main()
    
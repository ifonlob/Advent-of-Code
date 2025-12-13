import sys
def leer_archivo() -> list[str]:
    try:
        with open('input.txt', "r") as archivo:
            texto = archivo.read().strip()
            lista_rangos = texto.split(",")
        return lista_rangos
    except FileNotFoundError:
        print(f"Error. Archivo {sys.argv[1]} no encontrado")
        sys.exit(1)

def obtener_ids_invalidos(rangos:list[str])->int:
    contador = 0
    for rango in rangos:
        numeros = rango.split("-")
        numero1 = int(numeros[0])
        numero2 = int(numeros[1])
        for numero in range(numero1,numero2 + 1):
            numero_cadena = str(numero)
            if len(numero_cadena) % 2 == 0:
                mitad = len(numero_cadena) // 2
                if (numero_cadena[0:mitad]) == numero_cadena[mitad:]:
                    contador += numero
    return contador
    


def main():
    rangos = leer_archivo()
    contador = obtener_ids_invalidos(rangos)
    print(contador)

if __name__ == "__main__":
    main()
    
import sys
def leer_archivo()->list[str]:
    try:
        with open(sys.argv[1], "r") as archivo:
            lista_lineas = archivo.read().splitlines()
        return lista_lineas
    except FileNotFoundError:
        print(f"Error. Archivo {sys.argv[1]} no encontrado")
        exit()

def obtener_cantidad_veces_0(lista_lineas:list[str])->int:
    indice = 50 # El valor inicial es 50
    contador = 0 # Contador del número de apariciones de 0 en la combinación.
    for linea in lista_lineas:
        numero_a_sumar = 0
        numero_a_restar = 0
        if linea[0] == "L":
            numero_a_restar = int(linea[1:])
            for _ in range(numero_a_restar):
                if indice == 0:
                    indice = 99
                else:
                    indice -= 1
                if indice == 0:
                    contador += 1    
        elif linea[0] == "R":
            numero_a_sumar = int(linea[1:])
            for _ in range(numero_a_sumar):
                if indice == 99:
                    indice = 0
                else:
                    indice += 1
                if indice == 0:
                    contador += 1
    return contador
    

def main():
    lista_lineas = leer_archivo()
    contador = obtener_cantidad_veces_0(lista_lineas)
    print(contador)

if __name__ == "__main__":
    main()
    
import sys
def leer_archivo() -> list[str]:
    try:
        with open('input.txt', "r") as archivo:
            lista_bancos = archivo.read().strip().splitlines()
        return lista_bancos
    except FileNotFoundError:
        print(f"Error. Archivo 'input.txt' no encontrado")
        sys.exit(1)
        
def obtener_descarga_mas_alta(lista_bancos:list[str])->int:
    contador = 0
    for banco in lista_bancos:
        mayor = 0
        numeros_banco = list(map(int,banco))
        for i in range(len(numeros_banco)):
            for j in range(i + 1,len(numeros_banco)):
                numero = str(numeros_banco[i]) + str(numeros_banco[j])
                numero = int(numero)
                if numero > mayor:
                    mayor = numero
        max_banco = mayor
        contador += int(max_banco)
    return contador
    
def main():
    lista_bancos = leer_archivo()
    contador = obtener_descarga_mas_alta(lista_bancos)
    print(contador)

if __name__ == "__main__":
    main()
    
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
        numeros_banco = list(map(int,banco))
        numeros_a_eliminar = len(banco) - 12
        voltaje_maximo = [numeros_banco[0]]
        for numero in numeros_banco[1:]:
            while voltaje_maximo and numeros_a_eliminar > 0 and voltaje_maximo[-1] < numero:
                voltaje_maximo.pop()
                numeros_a_eliminar -= 1
            voltaje_maximo.append(numero)
        if numeros_a_eliminar > 0:
            voltaje_maximo = voltaje_maximo[:-numeros_a_eliminar]
        voltaje_maximo = voltaje_maximo[:12]
        voltaje_maximo = list(map(str,voltaje_maximo))
        contador += int("".join(voltaje_maximo))
    return contador
def main():
    lista_bancos = leer_archivo()
    contador = obtener_descarga_mas_alta(lista_bancos)
    print(contador)

if __name__ == "__main__":
    main()
    
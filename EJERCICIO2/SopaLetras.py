import random


# Verifica si el tamaño N es suficiente para albergar las palabras más largas
def es_suficiente_tamano(N, palabras):
    max_len = max(len(palabra) for palabra in palabras)
    return N >= max_len


# Genera una matriz NxN inicializada con espacios vacíos
def generar_matriz(N):
    return [[' ' for _ in range(N)] for _ in range(N)]


# Verifica si es posible colocar una palabra en una dirección y posición específicas sin sobrescribir celdas ocupadas
def es_posible_colocar(matriz, palabra, direccion, fila, col):
    N = len(matriz)
    long = len(palabra)

    if direccion == 'horizontal':
        if col + long > N:
            return False
        for i in range(long):
            if matriz[fila][col + i] != ' ' and matriz[fila][col + i] != palabra[i]:
                return False

    elif direccion == 'vertical':
        if fila + long > N:
            return False
        for i in range(long):
            if matriz[fila + i][col] != ' ' and matriz[fila + i][col] != palabra[i]:
                return False

    elif direccion == 'diagonal_positiva':
        if fila - long < -1 or col + long > N:
            return False
        for i in range(long):
            if matriz[fila - i][col + i] != ' ' and matriz[fila - i][col + i] != palabra[i]:
                return False

    elif direccion == 'diagonal_negativa':
        if fila + long > N or col + long > N:
            return False
        for i in range(long):
            if matriz[fila + i][col + i] != ' ' and matriz[fila + i][col + i] != palabra[i]:
                return False

    return True


# Coloca una palabra en la matriz en una dirección y posición específicas
def colocar_palabra(matriz, palabra, direccion, fila, col):
    long = len(palabra)

    if direccion == 'horizontal':
        for i in range(long):
            matriz[fila][col + i] = palabra[i]

    elif direccion == 'vertical':
        for i in range(long):
            matriz[fila + i][col] = palabra[i]

    elif direccion == 'diagonal_positiva':
        for i in range(long):
            matriz[fila - i][col + i] = palabra[i]

    elif direccion == 'diagonal_negativa':
        for i in range(long):
            matriz[fila + i][col + i] = palabra[i]


# Encuentra la mejor posición para una palabra recorriendo todas las posibles ubicaciones y direcciones
def encontrar_mejor_posicion(matriz, palabra, i):
    N = len(matriz)
    direcciones = ['horizontal', 'vertical', 'diagonal_positiva', 'diagonal_negativa']

    posx = random.sample(range(10), 10)
    posy = random.sample(range(10), 10)

    for direccion in direcciones[i:]:
        for fila in range(10):
            for col in range(10):
                if es_posible_colocar(matriz, palabra, direccion, posx[fila], posy[col]):
                    return direccion, posx[fila], posy[col]
    return None


# Rellena las celdas vacías de la matriz con letras aleatorias
def rellenar_matriz(matriz):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            if matriz[fila][col] == ' ':
                matriz[fila][col] = random.choice(letras)


# Muestra la matriz en la consola
def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))


def main():
    # Solicita al usuario el tamaño de la sopa de letras y las palabras
    # N = int(input("Ingrese el tamaño de la sopa de letras (N): "))
    palabras = input("Ingrese las palabras separadas por comas: ").split(',')

    # Limpia y convierte las palabras a mayúsculas
    palabras = [palabra.strip().upper() for palabra in palabras]

    palabras = sorted(palabras, key=len, reverse=True)

    # # Verifica si el tamaño es suficiente para las palabras
    if not es_suficiente_tamano(10, palabras):
        print("Error: El tamaño N no es suficiente para albergar la longitud de las palabras.")
        return

    # Genera la matriz 10x10
    matriz = generar_matriz(10)

    # Intenta colocar cada palabra en la mejor posición posible
    i = 0
    for palabra in palabras:
        mejor_posicion = encontrar_mejor_posicion(matriz, palabra, i)
        if mejor_posicion:
            i = (i + 1) % 4
            direccion, fila, col = mejor_posicion

            if random.choice([True, False]) :
                palabra = palabra[::-1]

            colocar_palabra(matriz, palabra, direccion, fila, col)
        else:
            print(f"No se pudo colocar la palabra: {palabra}")

    # Rellena las celdas vacías con letras aleatorias
    rellenar_matriz(matriz)

    # Muestra la matriz generada
    mostrar_matriz(matriz)


if __name__ == "__main__":
    main()

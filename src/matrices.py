def es_matriz(matriz: list[list[int | float]]) -> bool:
    """
    Comprueba si una lista de listas representa una matriz válida.

    Parámetros:
    matriz (list[list[int | float]]): Lista de listas que se quiere comprobar.

    Devuelve:
    bool: True si todas las filas tienen el mismo número de elementos.
    """
    
    if len(matriz) == 0:
        return True
    # TODO: Ejecutar con el depurador
    # Esto es un esquema de para todo
    num_columnas = len(matriz[0])

    es_rectangular = True
    for fila in matriz[1:]:
        # Si NO se cumple la condicion
        if len(fila) != num_columnas:
            es_rectangular = False
            break
    return es_rectangular


def suma_matrices(
    m1: list[list[int | float]], m2: list[list[int | float]]
) -> list[list[int | float]] | None:
    """
    Suma dos matrices de las mismas dimensiones.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]] | None: Matriz resultante, o None si las matrices
    no son válidas o tienen dimensiones distintas.
    """
    num_filas = len(m1)
    num_columnas = len(m1[0])
    matriz_suma = []
    for i in range (num_filas):
        fila = [0]* num_columnas
        matriz_suma.append(fila)
    for i in range(num_filas):
        matriz_suma[i][j] = m1[i][j] + m2[i][j]
    return matriz_suma

def suma_filas(
    matriz: list[list[int | float]],
) -> list[int | float] | None:
    """
    Suma los elementos de cada fila de una matriz.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuyos elementos se sumarán.

    Devuelve:
    list[int | float] | None: Lista con la suma de cada fila, o None si la
    matriz no es válida.
    """
    filas_sumadas = []
    if es_matriz(matriz) == False:
        return None
    for fila in range(len(matriz)):
        fila_sumada = sum(fila)
        filas_sumadas.append(fila_sumada)
    return filas_sumadas


def suma_diagonal(matriz: list[list[int | float]]) -> int | float | None:
    """
    Suma los elementos de la diagonal principal de una matriz cuadrada.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuadrada de números.

    Devuelve:
    int | float | None: Suma de la diagonal, o None si la matriz no es válida
    o no es cuadrada.
    """
    if not es_matriz(matriz) or len(matriz) != len(matriz[0]):
        return None
    res = 0
    for elem in range (len(matriz)):
        res += matriz[elem][elem]
    return res

def transponer(
    matriz: list[list[int | float]],
) -> list[list[int | float]] | None:
    """
    Devuelve la matriz transpuesta.

    Parámetros:
    matriz (list[list[int | float]]): Matriz que se quiere transponer.

    Devuelve:
    list[list[int | float]] | None: Matriz transpuesta, o None si la matriz
    no es válida.
    """
    if not es_matriz(matriz):
        return None
    if len(matriz) == 0:
        return []
    num_columnas = len(matriz[0])
    traspuesta = []
    for i in range(num_columnas):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        traspuesta.append(fila)
    return traspuesta

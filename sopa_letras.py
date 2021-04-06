import random
import string 

def crear_matrix(nxn):
    """Devuelve matrix de nxn filas/columnas."""
    matrix = []
    for i in range(nxn):
        matrix.append([])
        for j in range(nxn):
            matrix[i].append("")
    return matrix

def completar_matrix(matrix, n, randomChar=True):
    """Completa y devuelve una matriz con letras aleatorias o con asteriscos.
    Parametros:
    mtx        -- matriz a completar
    n          -- entero de filas/columnas a completar
    randomChar -- booleano que indica si son letras aleatorias o asteriscos
    """
    for i in range(n):
        for j in range(n):
            if randomChar:
                if matrix[i][j] == "" : 
                    matrix [i][j] = random.choice(string.ascii_lowercase)
            else:
                if matrix[i][j] == "" : 
                    matrix[i][j] = "*"
    
    return matrix

def valores_posicion(matrix, nxn, isrow, pos):
    """Devuelve una lista con informacion acerca de una fila/columna especifica de la matriz.
    Parametros:
    isrow -- booleano que indica si es fila o columna
    pos   -- entero que indica fila/columna
    """
    
    valores = []
    espacios = 0
    for i in range(nxn):
        if isrow:
            if matrix[pos][i] != "":
                valores.append(espacios)
                valores.append(matrix[pos][i])
            else:
                espacios += 1
        else:
            if matrix[i][pos] != "":
                valores.append(espacios)
                valores.append(matrix[i][pos])
                espacios = 0
            else:
                espacios += 1
    # Si la fila/columna esta vacia, indicar que existen nxn espacios vacios
    if espacios == nxn:
        valores.append(espacios)
        valores.append('0')

    return valores

def colocar_palabra(matrix, palabra, esfila, pos, inicio):
    """Coloca la palabra dentro de la matriz en la fila/columna especificada.
    Params:
        - palabra: cadena a ubicar
        - esfila: determina si es fila o columna
        - pos: posicion de la fila/columna
        - inicio: margen que tiene desde el inicio de la fila/columna
    """
    for i in range(inicio, inicio+len(palabra)):
        if esfila:
            matrix[pos][i] = palabra[i - inicio]
        else:
            matrix[i][pos] = palabra[i - inicio]
    return matrix

def procesar_palabra(matrix, nxn, palabras):
     """Acomoda las palabras en la matriz tablero, y la devuelve junto a una lista de posiciones y entero de las palabras salteadas.
    Para acomodar las palabras se les asigna un sentido, una direccion y una posicion aleatoria dentro de la matriz.
    Se pide informacion de tal fila/columna a la funcion "valores_posicion" hasta que la palabra en cuestion pueda ser correctamente acomodada dentro de la matriz.
    Si la palabra no puede ser acomodada en la fila/columna random, con la direccion random, se prueba en la siguiente fila/columna con la misma direccion; una vez
    recorridas todas las filas/columnas, cambia la direccion y prueba nuevamente una por una. Si tampoco sirve, se saltea la palabra
    Las primeras dos palabras cumplen con ciertas condiciones:
    1) La primer palabra debe tener direccion vertical y estar posicionada de arriba hacia abajo
    2) La segunda palabra debe tener direccion horizontal y estar posicionada de derecha a izquierda
    Parametros:
    matrix   -- matriz en la que procesar las palabras
    nxn      -- entero que indica la longitud de la matrix
    palabras -- lista de palabras para procesar
    """
    salteadas = 0
    posiciones = []

    # direccion       -- booleano que indica la direccion de la palabra
    # posicion        -- entero que indica fila o columna en la que colocar la palabra
    # sentido_inverso -- booleano que indica el sentido de la palabra

    for i in range(len(palabras)):
        posicion_inicial = random.randint(0,nxn-1)
        sentido_inverso = bool(random.randint(0,1))

        if i == 0:
            direccion_inicial = False # Primer palabra siempre Vertical
        elif i == 1:
            direccion_inicial = True  # Segunda palabra siempre Horizontal
            sentido_inverso = True    # Segunda palabra siempre Invertida
        else: 
            direccion_inicial = bool(random.randint(0,1))

        posicion = posicion_inicial
        direccion = direccion_inicial

        if sentido_inverso:
            palabras[i] = palabras[i][::-1]

        colocada = False
        while (not colocada):
            # Siempre Par
            valores_en_posicion = valores_posicion(matrix, nxn, direccion, posicion)

            for j in range(len(valores_en_posicion)//2):
                 # Si el espacio para acomodar la palabra es mayor en longitud, se le agrega un margen random a la palabr
                if int(valores_en_posicion[j*2]) >= len(palabras[i]):
                    margen = int(valores_en_posicion[j*2]) - len(palabras[i])
                    if margen > 0:
                        inicio = random.randint(0,margen)

                    matrix = colocar_palabra(matrix, palabras[i], direccion, posicion, margen)

                    if direccion:
                        flia_inicio = posicion
                        columna_inicio = margen

                        fila_final = posicion
                        columna_final = margen + len(palabras[i]) -1
                    else:
                        columna_inicio = posicion
                        flia_inicio = margen

                        columna_final = posicion
                        fila_final = margen + len(palabras[i]) - 1

                    if sentido_inverso:
                        aux = fila_final
                        fila_final = flia_inicio
                        flia_inicio = aux

                        aux = columna_final
                        columna_final = columna_inicio
                        columna_inicio = aux
                    
                    # Alternativa para hacer "legible" las posiciones
                    # posiciones.append(str(columna_inicio)+","+str(fila_inicio)+":"+str(columna_final)+","+str(fila_final))
                    posiciones.append(str(columna_inicio)+","+str(flia_inicio)+","+str(columna_final)+","+str(fila_final))
                    colocada = True
                    break

            if not colocada:
            # Si en esa posicion no entra, probar en la siguiente
                if posicion < nxn-1: posicion += 1
                else: posicion = 0

                # Cuando prueba todas las posiciones, cambiar direccion y probar de nuevo
                if posicion == posicion_inicial :
                    direccion = not direccion

                    # Si cambiar la direccion y probar en todas las posiciones tampoco sirve, entonces saltear palabra
                    if direccion == direccion_inicial:
                        salteadas+=1
                        # Si, "Break" porque el while esta dentro del For.
                        break

        if salteadas != 0:
            return matrix, posiciones, salteadas
        else:
            return matrix, posiciones, 0
    # Nueva linea

def mostrar_tablero(matrix, n):
    """Imprime la matriz en forma de tablero, con letras para indicar las columnas y numeros para indicar las filas."""
    # Cabecera de Columnas    
    fila = '/ |'
    for i in range(n):
        fila = fila + " " + chr(65+i)
    print(fila)
    print("-"*(2*n+3))
    # Cabecera de Filas
    for i in range(n):
        fila = str(i+1)
        if i < 9:
            fila += " |"
        else:
            fila += "|"
        for j in range(n):
            fila = fila+" "+ matrix[i][j]
        print(fila)
        fila = ""
    # Nueva linea
    print("")

def jugar_sopa_letras(n, palabras):
    """[Genera una sopa de letras aleatoria]

    Args:
        n ([int]): [Numero de columnas y filas]
        palabras ([list]): [Lista que contiene las palabras]

    Returns:
        tablero[list]: [Retorna una lista que forma el tablero]
    """
    matrix = crear_matrix(n)
    matrix_completa = completar_matrix(matrix, n, True)
    matrix_procesada, posiciones, salteadas = procesar_palabra(matrix, n, palabras)
    return mostrar_tablero(matrix_procesada,n)









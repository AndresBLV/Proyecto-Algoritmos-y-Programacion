import random 
#Escenario donde transcurre el juego
escenario = \
    '''
~~~~~~~~~|~
         |
 0123456 J         
~~~~~~~~~~~
'''

simbolos = '><(((°>'

def inicializar_juego(diccionario):
    """[Inicia los parametros iniciales para el juego del ahorcado]

    Args:
        diccionario : [Diccionario que trae las palabras a utilizar en el juego]

    Returns:
        [Tablero]: [Tablero del juego]
        Palabra: palabra random del diccionario para utilizar en la ronda
    """
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []

def mostrar_escenario(errores):
    """[Imprime el escenario donde transcurre el juego]

    Args:
        errores : [Registra los errores cometidos en el escenario]
    """
    escena = escenario
    for i in range(0,len(simbolos)):
        simbolo = simbolos[i] if i < errores else ' '
        escena = escena.replace(str(i), simbolo)
    print(escena)

def mostrar_tablero(tablero, letras_erroneas):
    """[Imprime el tablero donde transcurre el ahorcado

    Args:
        tablero ([list]): [Lista que muestra el tablero donde transucrre el juego]
        letras_erroneas ([str]): [Letras que no forman parte de la palabra a adivinar]
    """
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erroneas:',*letras_erroneas)
        print()

def pedir_letra(tablero, letras_erroneas):
    """[Pide una letra al jugador para colocarla en el tablero]

    Args:
        tablero ([list]): [Lista que muestra el tablero]
        letras_erroneas ([str]): [Letras erroneas en el juego]

    Returns:
        letra[str]: [Letra a colocar en el tablero]
    """
    valida = False
    while not valida: 
        letra =input('Introduce una letra (a-z): ').lower()
        valida = 'a' <= letra <= 'z'and len(letra) == 1
        if not valida:
            print('Error, la letra tiene que estar entre a y z.')
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print('Letra repetida, prueba con otra.')
    return letra

def procesar_letra(letra, palabra, tablero, letra_erroneas):
    """[Introduce la letra anteriormente dada para colocarla en el tablero

    Args:
        letra ([str]): [Letra a procesar]
        palabra ([str]): [Palabra a comprobar si la letra esta contenida]
        tablero ([list]): [Tablero del juego]
        letra_erroneas ([str]): [Letras erroneas dadas por el juagador]
    """
    if letra in palabra:
        print('¡Genial! Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print("¡Oh! Has fallado.")
        letra_erroneas.append(letra)

def actualizar_tablero(letra, palabra, tablero):
    """[Actualiza el tablero con la letra procesada]

    Args:
        letra ([str]): [Letra procesada por el usuario]
        palabra ([str]): [palabra contenida en el diccionario, para comprobar si la letra forma parte de la palabra]
        tablero ([list]): [Tablero del juego]
    """
    for i, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[i] = letra

def comprobar_palabra(tablero):
    """[Comprobar si el tablero se actualizo de manera correcta]

    Args:
        tablero ([List]): [Tablero del juego]

    Returns:
        [str]: [Nos muestra que se actualizo el tablero]
    """
    return '_' not in tablero

def jugar_ahorcado(diccionario,enunciado, clue, count_clue):
    """[Inicia todo el juego del ahorcado devolviendo un booleano dependiendo del resultado]

    Args:
        diccionario ([list]): [Palabras que pueden salir en el juego]
        enunciado ([str]): [Breve descrpcion que da una pequena pista de la palabra]
        clue(str): Pista para ayudar al jugador
        count_clue[int]: Contador con las pistas que tiene el juagador 
    Returns:
        [booleano]: [Retorna verdadero si se gana el juego y falso si se pierde]
        count_clue[int]: Retorna el nuevo valor del contador
    """
    print(enunciado)
    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)
    while len(letras_erroneas) < len(simbolos):
        print(enunciado)
        mostrar_escenario(len(letras_erroneas))
        clue_input = input('Desear usar una pista Si(s) o No(n):\n==> ').lower() #Input de la pista
        while clue_input != 's' and clue_input != 'n':
            clue_input = input('Ingresa Si(s) o NO(n):\n==> ') 
        if clue_input == 's':
            if count_clue > 0:
                print(clue)
                count_clue -= 1 
            else:
                print('No tienes mas pistas')

        mostrar_tablero(tablero,letras_erroneas)
        letra = pedir_letra(tablero, letras_erroneas)
        procesar_letra(letra, palabra, tablero, letras_erroneas)
        if comprobar_palabra(tablero):
            return True, count_clue
    else:
        print(f'Lo siento! Has perdido la palabra a adivinar era {palabra}')
        mostrar_escenario(len(letras_erroneas))
        return False, count_clue
    
   



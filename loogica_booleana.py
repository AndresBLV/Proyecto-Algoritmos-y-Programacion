def logica_booleana(question,funcion, answer,clue,count_clue):
    """[Inicia el juego de logica boolena, si el jugador realiza el codigo en frio de manera correcta,
    entonces devuelve True, sino devuelve Falso]

    Args:
        question ([str]): [Pregunta a constestar por el jugador]
        funcion ([str]): [Funcion con la cual va a trabajar el jugador]
        answer ([str]): [Respuesa a la pregunta]
        clue ([str]): [Pistas que puede usar el jugador]
        count_clue ([int]): [Numero de pistas restantes del jugador]

    Returns:
        [booleano]: [Devuelve True si acierta la pregunta, False si se equivoca]
        count_clue[int]: Devuelve el numero de pistas restantes
    """
    print(question)
    clue_input = input('Desear usar una pista Si(s) o No(n):\n==> ').lower() #Inputo de la pista
    while clue_input != 's' and clue_input != 'n':
        clue_input = input('Ingresa Si(s) o NO(n):\n==> ') 
    if clue_input == 's':
        if count_clue > 0:
            print(clue)
            count_clue -=1
        else:
            print('No tienes mas pistas')
    user_input=eval(input(f'Ingresa el codigo para resolver {funcion} (la variable de la frase se llama funcion):\n==>'))
    if user_input == answer:
        return True,count_clue
    else:
        return False,count_clue
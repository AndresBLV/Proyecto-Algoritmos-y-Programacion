def encuentra_logica(question, answer, clue, count_clue):
    """[Inicia el juego de encuentra la logica, imprimiendo la preguna , el jugador tiene que colocar la respuesta correcta para ganar]

    Args:
        question ([str]): [Pregunta contenida en el endpoint]
        answer ([str]): [Respuesta contenida en el endpoint]
        clue ([str]): [Pista para el jugador]
        count_clue ([int]): [Contador de las pistas restantes del jugador]

    

    Returns:
        booleanos: Victoria = True Derrota= False
        count_clue: Contador de pistas
    """
    while True:
        print(question)
        clue_input = input('Desear usar una pista Si(s) o No(n):\n==> ').lower() #Input de la pista
            
        while clue_input != 's' and clue_input != 'n':
            clue_input = input('Ingresa Si(s) o NO(n):\n==> ') 
        if clue_input == 's':
            if count_clue > 0:
                print(clue)
                count_clue -=1
            else:
                print('No tienes mas pistas')
        user_input = input('Ingrese su respuesta:\n==>')
        if answer == user_input:
            return True, count_clue
        else:
            return False, count_clue
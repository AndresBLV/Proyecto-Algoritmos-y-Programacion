def pregunta_py(question, answer, clue, count_clue):
    """[Funcion que inicia el minijuego de preugntas, donde se le imprime una pregunta o adivinanza al jugador
    , este tiene el objetivo de responder bien esa pregunta, si lo consigue la funcion retorna True, si en cambio 
    se equivoca  retorna False]

    Args:
        question ([str]): [Pregunta contenida en el endpoint]
        answer ([str]): [Respuesta a la pregunta]
        clue ([str]): [Pista que se le otorga al jugador]
        count_clue ([int]): []

    Returns:
        [booleanos]: [Si ganas devuelve True, si pierders devuelve False]
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
    user_input = input('Ingresa la respuesta de la adivinanza:\n')
    if user_input == answer:
        return True, count_clue
    else:
        return False, count_clue
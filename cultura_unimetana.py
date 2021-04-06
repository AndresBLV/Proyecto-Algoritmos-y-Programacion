def cultura_unimet(question, answer, posible_answer, clue, count_clue):
    """[Inicia el juego de cultura unimetana, imprimiendo la preguna, el jugador tiene que colocar el numero de la respuesta correcta para ganar]

    Args:
        question ([str]): [Pregunta contenida en el endpoint]
        answer ([str]): [Respuesta contenida en el endpoint]
        posible_answer ([list]): [Todas las posibles respuestas que puede dar el usuario]
        clue ([str]): [Pista para el jugador]
        count_clue ([int]): [Contador de las pistas restantes del jugador]

    

    Returns:
        booleanos: Victoria = True Derrota= False
        count_clue: Contador de pistas
    """
    print(question)
    for i, posible in enumerate(posible_answer):
        print(f'{i+1}.- {posible}')
    while True:
        clue_input = input('Desear usar una pista Si(s) o No(n):\n==> ').lower() #Input de la pista
        
        while clue_input != 's' and clue_input != 'n':
                clue_input = input('Ingresa Si(s) o NO(n):\n==> ') 
        if clue_input == 's':
            if count_clue > 0:
                print(clue)
                count_clue -=1
            else:
                print('No tienes mas pistas')
        while True:
            try:
                user_input = ('Ingrese el numero de la respuesta correcta:\n==>')
                while (not user_input.isnumeric()) or user_input == 0 or user_input not in range(1,5):
                    user_input = ('Ingreso invalido, ingrese una opcion adecuada a su respuesta:\n==>')
                    raise Exception
                break 
            except:
                print('Error, introduzca una opcion correcta')
        if user_input == answer:
            return True, count_clue 
        else:
            return False, count_clue


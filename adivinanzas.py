def adivinanza(question, answers, clue, count_clue):
    """
    Devuelve un booleano si la pregunta esta bien contestada
    
    Parametros: 
    question: tipo str 
    answer: tipo str
    clue: tipo str
    count_clue = tipo int

    Retorno:
        [booleano]: [Retorna verdadero si se gana el juego y falso si se pierde]
        count_clue[int]: Retorna el nuevo valor del contador
    """
    while True: # Bucle que permite seguir funcionando el juego hasta que el jugador responda la pregunta
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
        else:
            user_input = input('Ingresa la respuesta de la adivinanza:\n==> ') #Input de la respuesta
            if user_input not in answers:
                return False, count_clue
            else:
                return True, count_clue
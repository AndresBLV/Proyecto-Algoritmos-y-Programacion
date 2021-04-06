import random

def escoge_numero(a,b,count_clue):   
    """[Inicia el juego de escoger un numero, se usa random para genera un numero aleatorio de en el rango 
    dado en el endpoint, la pista advierte que tan cerca esta el jugador, el juegador solo puede terminar el juego
    si acierta el numero]

    Args:
        a ([int]): [Rango inicial del numero aleatorio]
        b ([int]): [Rango final del numero aleatorio]
        count_clue ([int]): [Contador de pistas restantes del jugador]


    Returns:
        [booleano]: [Siempre True, solo puede terminar el juego si gana el juego]
        count_clue[int]: Devuelde el contador de pistas restantes
    """
    count = 0
    numero_aleatorio = random.randint(a,b)
    while count == 0:
        user_input = int(input(f'Ingresa un numero entre {a} y {b}'))
        while user_input.type() != int:
            user_input = input('Ingresa un numero entero entre {a} y {b}:\n==> ') 
        if user_input == numero_aleatorio:
            count += 1
        else:
            print('Numero incorrecto')
            while True:
                try:
                    user_pista = input('Desear utilizar una pista Si(s) o No(n): {}').lower()
                    while user_pista != 's' and user_input != 'n':
                        useruser_pista_pista = input('Ingresa Si(s) o No (n):\n==> ')  
                        raise Exception
                    break
                except:
                    print('Ingreso un valor erroneo')
            if user_pista == 's':
                if count_clue > 0:
                    if numero_aleatorio - user_input > 0 and numero_aleatorio - user_input < 2:
                        print('Esta muy cerca por arriba')
                        count_clue -=1
                    elif numero_aleatorio - user_input > 2 and numero_aleatorio - user_input > 5:
                        print('Estas cerca por arriba')
                        count_clue -=1                        
                    elif numero_aleatorio - user_input > 5:
                        print('Estas muy lejos por arriba')
                        count_clue -=1
                    elif numero_aleatorio - user_input < 0 and numero_aleatorio - user_input > -2:
                        print('Estas muy cerca por abajo')
                        count_clue -=1
                    elif numero_aleatorio - user_input < -2 and numero_aleatorio - user_input > -5:
                        print('Estas cerca por abajo')
                        count_clue -=1
                    else:
                        print('Estas muy lejos por abajo') 
                        count_clue -=1
                else:
                    print('No tienes mas pistas')
            else:
                print('Vuelve a intentarlo')
           
    return True, count_clue   
import random
import requests
import json
from funciones import *
from jugador import Jugador
from room import Room
from objeto import Objeto
from juego import Juego



def main():
    # Listas a utilizar en el juego
    jugadores = []
  
    inventario = []

    records = []

    leader = []

    # Endpoint realizado con la funcion endpoint
    endpoint_json = endpoint()

    # Bucle para mantener el juego funcionando de manera continua
    while True:
        # Menu
        print( 'Bienvenidos a Unimet-Scape, el comienzo de una aventura')
        print('\n')
        print('1.-Nueva Partida\n2.- Instrucciones del juego\n3.- Ver los records\n4.- Salir')
        print('\n')
        while True:
            try:
                option = input('Ingresa la opcion que desear ingresar:\n==> ') 
                while (not option.isnumeric()) and (option not in range(1,5)):
                    option = input('Ingresa una opcion valida del menu: ')
                    raise Exception
                break
            except:
                print('Ingreso un valor invalido')
        print('\n')
        # Opcion 1 Crear nuevo Juego
        if option == '1':
            # Nuevo bucle para mantenerse en la seccion 1, hasta terminar el juego, por si ocurre algun error
            while True:
                # Input para saber si el usuario esta registrado
                while True:
                    try:
                        user_input = input('Es un usario registrado Si(s) o No(n):\n==> ').lower()
                        while user_input != 's' and user_input != 'n':
                            user_input = input('Ingresa Si(s) o No (n):\n==> ')  
                            raise Exception
                        break
                    except:
                        print('Ingreso un valor erroneo')
                # Si la respuesta es si, se verifica
                if user_input == 's':
                    # Se verifica a traves de la funcion iniciar_sesion que devuelve un booleano
                    jugador, avatar, player = iniciar_sesion(jugadores)
                    # Si el booleano es True empieza el juego
                    if player:
                        #Se seleciona la dificultad con un metodo de jugador
                        jugador = jugador.dificultad()
                        # Se imprimen las narrativas
                        print('\n')
                        print('Que comience la aventura')
                        print('\n')
                        print(f'Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {jugador.time} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?')
                        reto = input('Si(s) o No(n):\n==> ').lower
                        # No importa la desicion del jugador ya no hay vuelta a tras
                        print('Sin importar tu respuesta, ya no hay vuelta atras, prepara tu mente y supera estos desafíos para salvar el disco duro.')
                        print('\n')
                        print(f'Bienvenido {avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.')
                        # Iniciamos todo el escape room, con la funcion iniciar_escape_room, la cual devuelve los valores para guardar en los records
                        jugador, win, lose, time, cuarto_visitado = iniciar_escape_room(jugador, avatar, endpoint, inventario)
                        
                        # Actualizamos la lista records con las variables, dadas por iniciar_escape_room, utilizando actualizar_records
                        records = actualizar_records(records, jugador, win, lose, time, cuarto_visitado)

                        # Se crea un archivo records.json donde se guarda los datos obtenidos de este jugador, como base de datos
                        with open('records.json','a') as file:
                            json.dump(records,file)

                        # Se vuelve al menu
                        break
                    # Su el booleano es False devuelve atras al usuario para registrase
                    else:
                        print('Usuario no registrado')
                # Si el usuario no esta registrado, se le pregunta si quiere registrarse
                else:
                    while True:
                        try:
                            registro = input('Deseas registrate, Si(s) o No(n):\n==> ').lower()
                            while user_input != 's' and user_input != 'n':
                                user_input = input('Ingresa Si(s) o No (n):\n==> ')  
                                raise Exception
                            break
                        except:
                            print('Ingreso un valor erroneo')
                    # Si el usuario desea registrarse se usa la funcion registrar_usuario, la cual agrega al jugador a jugadores, luego vuelve al inicio del bucle y se le pregunta si esta registrado para poder jugar
                    if registro == 's':
                        jugadores = registrar_usuario(jugadores)
                    # Si no quiere registrarse se le manda un mensaje de que no puede jugar sin registrarse  y se devuelve al menu
                    else:
                        print('Tienes que registrarte para poder jugar')
                        break

        # Opcion 2 muestras las instrucciones
        elif option =='2':
            # Se imprime las instrucciones
            print('\n')
            print('''
            Instrucciones:
            1.- Para empezar el juego, es necesario tener un usuario registrarlo, en caso de no tenerlos, se tiene que registrar.
            2.- Al iniciar una nueva partida, tienes que escoger la dificultad, dependiendo de ella, el jugador tendra una cantidad de vidad, pistas y tiempo determinado.
            3.- En el juego, el jugador encontrara distintos cuartos, los cuales, contendran distintos objetos dispersos en su interior.
            4.- Al agarrar o tocar un objetos, el jugador activara un acertijo/juego que al ganarlo otorga una recompensa que se guarda en el inventario.
            5.- En el inventario se guardaran todas las recompensas, que gane el jugador a traves de los distintos juegos.
            6.- Dependiendo del objeto, va a perdir o no una recompensa al jugador para iniciar el juego.
            7.- El juego termina cuando resuleves el ultimo juego en el tiempo determinado y sin perder todas las vidas, o cuando pierdes todas las vidas, o se acaba el tiempo.
            ''')

        # Opcion 3 muestra los records guardados en records.json de una forma especifica
        elif option =='3':
            # Le preguntamos al usuario que records quiere ver exactamente
            print('Que records quiere ver:\n1.- Learderboard\n2.-Cuarto mas visitado\n3.- Usuario que mas juega')
            while True:
                try:
                    user_option = input('Ingresa la opcion que desear ingresar:\n==> ') 
                    while (not user_option.isnumeric()) and (user_option not in range(1,4)):
                        user_option = input('Ingresa una opcion valida del menu: ')
                        raise Exception
                    break
                except:
                    print('Ingreso un valor invalido')
            print('\n')
            # Si la opcion es 1 se imprimen los 5 mejores tiempos por dificultad
            if user_option == '1':
                # Acrualiza la lista leaders para imprimir los mejores 5 jugadores con sus tiempos
                leaders = leaders(leaders)
                for i,leader in  enumerate(leaders):
                    print(f'{i+1}.- {leader}')
            # Si la opcion es la 2 se imprime el nombre del cuarto mas visitado
            elif user_option =='2':
                # la funcion cuarto_visitado guarda en una variable el str del nombre del cuarto que mas se visita
                cuarto_visitado()
            # La tercera opcion imprime la cantidad de veces que un jugador ha jugado
            else:
                # No se me ocurrio forma de imprimirlo
                 pass
        # La cuarta opcion, nos permite salir del bucle inicial y terminar el programa
        else:
            break   

main ()
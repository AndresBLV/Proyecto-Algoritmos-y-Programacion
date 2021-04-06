import random
import requests
import time
import json
from jugador import Jugador
from room import Room
from objeto import Objeto
from juego import Juego
from adivinanzas import *
from ahorcado import *
from criptograma import *
from cultura_unimetana import *
from encuentra_logica import *
from escoge_numero import *
from final_boss import *
from images import *
from loogica_booleana import *
from memoria import *
from palabra_mezclada import *
# from preguntas_matematica import pregunta_mat Problema que no me deja agarrar sympy haciendo que el programa crashee
from preguntas import *
from palabra_mezclada import *
from palabra_mezclada import *
from sopa_letras import *


def endpoint():
    """
    Genera un archivo json, donde se guardan todos los datos de la API en forma de diccionario
    para luego pasarlos a python como una lista de diccionarios, a traves de la libreria json y la ur de la API

    retorna:
    endpoint [lista]: Lista de dicionarios
    """

    url = 'https://api-escapamet.vercel.app/'
    
    response = requests.get(url).json() 

    with open('endpoint.json', 'w') as file:
        json.dump(response,file) 

    with open('endpoint.json') as file:
        endpoint = json.load(file)
        return endpoint

def registrar_usuario(jugadores):
    """[Registra un nuevo usuario en el juego, se le van pidiendo cada uno de los datos necesarios al jugador
    y luego se crea con los datos dados una clase jugador que es aagregado a la lista jugadores, que contiene a 
    todos los jugadores registrados]

    Args:
        jugadores ([list]): [Lista que contiene a los objetos de la clase jugador]


    Returns:
        jugadores[list]: [Lista actualizada con los nuevos jugadores agrgados]
    """
    print('Registro')
    print('\n')
    while True:
        username = input('Ingresa un nombre de usuario único:\n==> ')
        for usuario in jugadores:
            if username == usuario:
                print('El nombre colocado ya esta registrado')
            else:
                break
    
    password = input('Ingrese su contrasena:\n==> ')

    while True:
        try:
            age = input('Ingrese su edad:\n==>')
            while (not age.isnumeri()) and age < 0:
                age = input('Ingresa una edad valida:\n==>')
                raise Exception
            break
        except:
            print('Ingreso un valor erroneo')

    print('Avatares:\n1.- Scharifker\n2.- Eugenio Mendoza\n3.- Pelusa\n4.- Gandhi')
    while True:
            try:
                avatar = input('Ingresa la opcion que desear ingresar:\n==> ') 
                while (not avatar.isnumeric()) and (avatar not in range(1,5)):
                    option = input('Ingresa una opcion valida del menu: ')
                    raise Exception
                break
            except:
                print('Ingreso un valor invalido')
    if avatar == '1':
        avatar = 'Scharifker'
    elif avatar == '2':
        avatar = 'Eugenio Mendoza'
    elif avatar == '3':
        avatar == 'Pelusa'
    else:
        avatar = 'Gandhi'

    time = [] 

    win = 0

    lose = 0

    nuevo_usuario = Jugador(username, password, age, avatar, time, win, lose)

    jugadores.append(nuevo_usuario)

    print('Usuario registrado')

    return jugadores

def iniciar_sesion(jugadores):
    """
    Verifica que el jugador pueda iniciar sesion, teneindo que ingresar dos variables, el usuario y la contrasena
    si la contrasena no se encuentra en la lista jugadores, devuelde un booleano False, indicando que no pudo inicciar
    sesion, en cambio si la contrasena esta bien, retorna un booleanos True, asi como el jugador edseado y su avatar

    Parametros:
    jugadores[list]: Lista que contiene a los objetos jugadores

    Retorno:
    jugador[jugador]: Jugador deseado de la lista de jugadores
    avatar[str]: avatar que escogio el jugador al registrarse
    boolenao: True o False que indica si inicio o no sesion
    """
    username = input('Ingrese su nombre de usuario:\n==> ')
    contrasena = input('Ingrese su contrasena:\n==> ')
    for jugador in jugadores:
        while jugador['password'] != contrasena:
            opcion = input('Contrasena incorrecta, deseas volver a intentarlo Si(s) o No(n):\n==> ')
            while True:
                try:
                    opcion = input('Es un usario registrado Si(s) o No(n):\n==> ').lower()
                    while opcion != 's' and opcion != 'n':
                        opcion = input('Ingresa Si(s) o No (n):\n==> ')  
                        raise Exception
                    break
                except:
                    print('Ingreso un valor erroneo')
            if opcion == 's':
                contrasena = input('Ingrese su contrasena:\n==> ')
            else:
                return username, 'No avatar',False
        
        return jugador, jugador['avatar'], True
         
def actualizar_records (records, jugador, win, lose, time):
    """
    Actualiza la lista de records, a traves de una variable llamada player que guarda todos los datos que se pasan
    en forma de diccionario

    Parametros:
    records[list]: Lista a actualizar
    jugador[jugador] :Objeto que contiene los atributos de un jugador
    win[int] : Vicotrias, si completo el juego
    lose[int] : Derrotas, si perdio todas las vidas o por tiempo 
    time[int]: tiempo que tardo en finalizar el juego

    Retorno:
    records[lista]: Lista actualizada
    """
    player = {}
    player['jugador'] = jugador
    player['win'] = win
    player['lose'] = lose
    player['time'] = time
    records.append(player)

    return records

def leaders(leaders):
    """[Actualiza la lista leaders, de tal forma que contenga los 5 mejores tiempos en orden, segun la dificultad que desea ver el jugador
    esto se hace a traves de un manejo de archivos de records.json y el uso de bucles y listas para agurpar los mejores tiempos]

    Args:
        leaders ([list]): [Lista con los mejores tiempos por dificultad]

    Returns:
        leaders[list]: [Lista actualizada con los mejores tiempos por dificultad]
    """
    count = 0
    facil = []
    normal = []
    dificil = []
    tiempos = []
  
    # Manejo de datos en el archivo records.json para agrupar los jugadores en lista por su dificultad
    with open('records.json') as file:
        for i in file:
            if i.dificultad == 'f':
                facil.append(i)
            elif i.dificultad == 'n':
                normal.append(i)
            elif i.dificultad == 'd':
                dificil.append(i)
            else:
                print('Todavia no hay ningun record')

    # Preguntar la dificultad en la cual desea ver los mejores tiempos
    print('Que dificultad deseas ver:\n1.-Facil\n2.-Normal\n3.-Dificil')
    user_input = input('Ingrese su eleccion:\n==> ')
    # Input para escoger
    while (not user_input.isnumeric()) and user_input not in range(1,4):
        user_input = input('Ingresa un valor correcto:\n==> ')
    # Opcion 1 agrupa los mejores tiempos en facil
    if user_input == '1':
        # Agrupa los tiempos de los jugadores en una lista
        for jugador in facil:
            tiempos.append(jugador.time)
        # Ordenamos la lista de menor a mayor
        tiempos = tiempos.sort()
        # Agrupamos los primeros 5 tiempos a traves de recorres la lista tiempo con un bucle que cuando guarda los 5 mejores se termina
        while count < 5:
            for tiempo in tiempos:
                leaders.append(jugador['tiempo'])
                count += 1
        # retornamos la lista
        return leaders
    
    # Mismo procedimiento que la opcion 1 pero para una dificultad normal
    elif user_input == '2':
        for jugador in normal:
            tiempos.append(jugador.time)
        tiempos = tiempos.sort()
        while count < 5:
            for tiempo in tiempos:
                leaders.append(jugador['tiempo'])
                count += 1
        return leaders

     # Mismo procedimiento que la opcion 1 pero para una dificultad normal
    else:
        for jugador in dificil:
            tiempos.append(jugador.time)
        tiempos = tiempos.sort()
        while count < 5:
            for tiempo in tiempos:
                leaders.append(jugador['tiempo'])
                count += 1
        return leaders
            
def cuarto_visitado():
    with open('records.json') as file:
        for i in file:
            print(f'Jugador:{i.username}. Cuarto mas visitado: {cuarto_visitado}')

def iniciar_escape_room(jugador, avatar, endpoint, inventario):
    """[Funcion que incia el juego escape_room, en este se agrupan disitntas funciones que permiten ir a distitnas
    habitaciones, tocar objetos, y jugar minijuegos con el cual obtienes recompensas, pierdes vidas o ganas y un limite
    de tiempo establecido que si se acaba se termina el juego]

    Args:
        jugador ([jugador]): [Objeto que contiene los atributos de un jugador]
        avatar ([str]): [Avatar del jugador]
        endpoint ([diccionario]): [Diccionario que contiene la informacion de la API]
        inventario ([list]): [Inventario donde se guardan los objetos requeridos para jugar un juego]
    """
    cuartos = [biblioteca, plaza_rectorado, puerta_laboratorio_rota, puertas_laboratorio, cuarto_servidores]
    print(biblioteca)
    while True:
        print(jugador.live)
        user_input = input('Que deseas hacer moverte(m) o tocar un objeto(t):\n==> ').lower()
        while user_input != 'm' and user_input != 't':
            user_input = input('Ingresa m para moverte y t para tocar:\n==> ') 
        if user_input == 'm':
            mover = jugador.move_room(biblioteca, plaza_rectorado,puertas_laboratorio)
            print(mover)
        else:
            tocar = jugador.touch_objects()
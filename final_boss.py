import random

def piedra_papel_tijeras():
    """[Inicia juego de Piedra, papel y tijeras]

    Returns:
        [booleano]: [True si gana, False si pierde]
    """
    print('No hay pistas')
    while True:
        aleatorio = random.randrange(0, 3) #Genera numero aleatorio entre 0 y 3
        elijePc = ""
        print("1)Piedra")
        print("2)Papel")
        print("3)Tijera")
        opcion = int(input("Que elijes: ")) #Selecciona la opcion a utilizar 
        while opcion.type() == int and opcion not in range(1,4):
            opcion = int(input('Elige uno de los valores dados:==> '))

        # Cambiamos nuestra seleccion para escoger que usar
        if opcion == 1:
            elijeUsuario = "piedra"
        elif opcion == 2:
            elijeUsuario = "papel"
        elif opcion == 3:
            elijeUsuario = "tijera"

        print("Tu elijes: ", elijeUsuario)

        # Todas las posibles soluciones para el juego
        if aleatorio == 0:
            elijePc = "piedra"
        elif aleatorio == 1:
            elijePc = "papel"
        elif aleatorio == 2:
            elijePc = "tijera"
        print("PC elijio: ", elijePc)
        print("...")
        if elijePc == "piedra" and elijeUsuario == "papel":
            print("Ganaste, papel envulve piedra")
            return True
        elif elijePc == "papel" and elijeUsuario == "tijera":
            print("Ganaste, Tijera corta papel")
            return True
        elif elijePc == "tijera" and elijeUsuario == "piedra":
            print("Ganaste, Piedra pisa tijera")
            return True
        if elijePc == "papel" and elijeUsuario == "piedra":
            print("perdiste, papel envulve piedra")
            return False
        elif elijePc == "tijera" and elijeUsuario == "papel":
            print("perdiste, Tijera corta papel")
            return False
        elif elijePc == "piedra" and elijeUsuario == "tijera":
            print("perdiste, Piedra pisa tijera")
            return False
        elif elijePc == elijeUsuario:
            print("empate")
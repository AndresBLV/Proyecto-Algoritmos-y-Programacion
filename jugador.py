class Jugador:
    def __init__(self, username, password, age, avatar, time, win, lose):
        self.username = username
        self.password = password
        self.age = age
        self.avatar = avatar
        self.time = 0
        self.win = 0
        self.lose = 0
        self.live = 0
        self.clue = 0
        self.dificultad = dificultad 

    def dificultad(self):
        """[sumSeleciona la dificultad en la que quiere jugar el jugador, el juego, dependiendo de la 
        difiultad, va a tener unas vidas, pistas y tiempo determinado, la funcion, registra la difucultad que 
        desea el jugador y retorna el ujugador con los valores agregados]

        Returns:
            live[int]: [Vidas segun dificultad]
            clues[int]: Pistas segun dificultad
            tiempo[int]: Tiempo segun la dificultad
        """
        while True:
            try:
                dificultad = input('En que dificultad quieres jugar, Facil(f), Normal(N) o Dificil (d):\n==> ').lower()
                while dificultad != 'f' or dificultad != 'n' or dificultad != 'd':
                    dicicultad   = input('Ingresa Facil(f), Normal (n) o Dificil (d):\n==> ')  
                    raise Exception
                break
            except:
                print('Ingreso un valor erroneo')
        if dicicultad == 'f':
            new_lives = 5
            new_clues = 5
            new_time = 50
            self.time =  new_time
            self.live = new_lives
            self.clue = new_clues
            self.dificultad = 'f'
            return self.live, self.clue, self.tiempo, self.dificultad

        elif dicicultad == 'n':
            new_lives = 3
            new_clues = 3
            new_time = 35
            self.time =  new_time
            self.live = new_lives
            self.clue = new_clues
            self.dificultad = 'n' 
            return self.live, self.clue, self.tiempo, self.dificultad

        else:
            new_lives = 1
            new_clues = 2
            new_time = 20
            self.time =  new_time
            self.live = new_lives
            self.clue = new_clues 
            self.dificultad = 'd'
            return self.live, self.clue, self.tiempo, self.dificultad          
    
    def move_room(self,escenario_actual, escenario1, escenario2):
        """[Funcion de la clase jugador que permite a este moverse de habitacion a haitacion, preguntando si desea
        moverse de habitacion, y segun su respuesta se le ofrece dos lugares al cual moverse
        segun su seleccion, se puede mover a uno de esas habitaciones o quedarse en al actual]

        Args:
            escenario_actual ([str]): [Escenaario donde se encuentra actualmente el jugadro]
            escenario1 ([str]): [Escenario posible para moverse]
            escenario2 ([str]): [Escenario posible para moverse]

        Returns:
            escenario[print]: [Retorna el escenario al cual desea moverse el jugador]
        """
        while True:
            try:
                move = input('Deseas moverte de habitacion SI(s) NO (n):\n==>').lower()
                while move != 's' and move != 'n':
                    move = input('Ingresa Si(s) o No (n):\n==> ')  
                    raise Exception
                break
            except:
                print('Ingreso un valor erroneo')
        
        if move == 's':
            while True:
                try:    
                    room = input(f'A cual cuarto te quieres mover \n1.- {escenario1} \n2.-{escenario2}:\n==> ')
                    while not room.isnumeric  and room not in range(1,3):
                        move = input(f'Ingresa 1 para ir a {escenario1}, ingresa 2 para ir a {escenario2}:\n==>')
                        raise Exception
                    break
                except:
                    print('Ingreso un valor erroneo')
            if room == '1':
                return escenario1
            else:
                return escenario2
        else:
            return escenario_actual

    def touch_object(self, objeto_izquierda, objeto_centro, objeto_derecha, game1, game2, game3):
        """[Esta funcion de la clase jugador, permite al jugador tocar los objetos de las distintas habitaciones,
        dependiendo del objeto que toque, va a retornar uno de los juegos, necesarios para conseguir la recompensa]

        Args:
            objeto_izquierda (str): [Objeto ubicado a la izquierda]
            objeto_centro (str): [Objeto ubicado en el centro]
            objeto_derecha (str): [Objeto ubicado en la derecha]
            game1 (str): [Juego del objeto izquierdo]
            game2 (str): [Juego del objeto del centro]
            game3 (str): [Juego del objeto derecho]


        Returns:
            game[str]: [Regrea uno de los juegos de los objetos, de acuerdo al objeto que decidio tocar]
        """
        while True:
            try:
                tocar = input(f'Cual objeto deseas tocar \n1.- {objeto_izquierda}\n2.- {objeto_centro}\n3.- {objeto_derecha}:\n==> ')
                while not tocar.isnumeric() and tocar not in range(1,4):
                    tocar = input(f'Ingresa 1 para tocar el {objeto_izquierda}, 2 para tocar el {objeto_centro} o 3 para tocar el {objeto_derecha}:\n==> ')  
                    raise Exception
                break
            except:
                print('Ingreso un valor erroneo')
        if tocar == '1':
            return game1
        elif tocar == '2':
            return game2
        else:
            return game3

    def perder_vida(self, vida_perdida):
        """[Funcion de la clase juador, que permite reducir el numero de vidas, segun el mini juego que pierda
        si la funcion se ejecuta cuando el jugador pierde su ultima vida, suma derrota y se acaba el juego]

        Args:
            vida_perdida ([int or float]): [Vida perdida en el minijuego]

        Returns:
            live[int or float]: [Actualiza la vida restante del jugador]
            lose[int]: Retorna derrota si la vida es menor o igual a 0, cuando se ejecuta la funcion
        """
        if self.live > 0:
            self.live -+ vida_perdida
            return self.live
        else:
            print('GAME OVER')
            self.lose += 1  
            return self.lose



def criptograma(message, desplazamiento):
    """[Encripta un mensaje dado por el endpoint]

    Args:
        message ([str]): [Mensaje a encriptar]
        desplazamiento ([int]): [Desplazamiento que va a presentar el encriptamiento]

    Returns:
        cifrado[str]: [Mensaje cifrado]
        desplazamiento[int]: Desplazamiento del mensaje cifrado
    """
    if message == message.upper():
        abc ='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    else:
        abc = 'abcdefghijklmnñopqrstuvwxyz' 

    cifrad = ''

    for i in message:
        if i in abc:
            cifrad += abc[(abc.index(i)+desplazamiento) % (len(abc))]
        else:
            cifrad += i

    return cifrad, desplazamiento

def jugar_criptograma(message, desplazamiento, clue, count_clue):
    """[Incia el juego de criptograma devolviendo un booleano dependiendo si gana o pierde asi como el contador de pistas]

    Args:
        message ([str]): [Mensaje dado en el endpoint]
        desplazamiento ([int]): [Desplazamiento del mensaje encriptado]
        clue[str]: Pista para ayudar al usuario
        count_clue[int]: Contador de pistas

    Returns:
        [Booleano]: [Si se gana devuelve True si se pierde devuelve False]
        count_clue:

    """
    texto_cifrado, texto_desplazado = criptograma(message, desplazamiento)
    while True:
        print('Texto cifrado:', texto_cifrado)
        print('Desplazamiento:',texto_desplazado)
        clue_input = input('Desear usar una pista Si(s) o No(n):\n==> ').lower() #Inputo de la pista
        
        while clue_input != 's' and clue_input != 'n':
                clue_input = input('Ingresa Si(s) o NO(n):\n==> ') 
        if clue_input == 's':
            if count_clue > 0:
                print(clue)
                count_clue -=1
            else:
                print('No tienes mas pistas')
        respuesta = input('Ingresa el texto desenciptado: ').lower()
        if respuesta == message.lower():
            return True
        else:
            return False




import random

def palabra_mezclada(categoria, palabras):
    count = 0
    
    tamano = 10

    palabras_desordenadas = []
    
    palabras_usuario = []
    
    print(f'{categoria}')
    
    print('\n')
    
    palabras_ordenadas = palabras.sort()
    
    for palabra in palabras:
        palabras_desordenada = random.sample(palabra,tamano)
        palabras_desordenadas.append(palabras_desordenada)
    
    print(palabras_desordenadas)
    
    while count < 4:
        user_input = input('Ingresa una de las palabras ordenadas:\n==> ')
        
        palabras_usuario.append(user_input)
        
        count += 1
    
    palabras_usuario_ordenado = palabras_usuario.sort()

    if palabras_usuario_ordenado == palabras_ordenadas:
        return True
    else:
        return False
    




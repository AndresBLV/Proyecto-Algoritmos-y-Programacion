from sympy import Derivate, diff, simplify 
from fractions import Fraction 

def derivada(derivada = 3*x, evaluar = 1):
    dx = simplify(diff(derivada,x).subs(x, evaluar))
    dx_fraction = str(Fraction(dx).limit_denominator())
    return dx_fraction

def pregunta_mat(question, derivada, evaluar):
    print('No hay pistas')
    print('\n')
    dx = derivada(derivada, evaluar)
    print(question)
    user_input = input('Escribe la respuesta de la derivada mostrada como una fraccion:\n')
    if user_input == dx:
        return True
    else:
        return False


    
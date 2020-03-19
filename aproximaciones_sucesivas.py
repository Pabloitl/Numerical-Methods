from math import *
import pandas as p

def ask_data():
    eps = float(input('Error: '))
    x   = float(input('Valor inicial: '))
    n   = int(input('Numero maximo de iteraciones'))
    g   = input('Funcion g(x): ')
    gp  = input('Funcion g\'(x): ')
    return eps, x, n, g, gp

def calculate_error(valor_aprox, valor_anterior):
    if valor_anterior == 0:
        return 1e10
    return round(abs(valor_anterior - valor_aprox) / abs(valor_aprox) * 100, 4)

def convergencia(g, x):
    if abs(round(eval(g), 4)) > 1:
        return False
    return True

def aproximate(eps, x, n, g, gp):
    frame = p.DataFrame()
    x_anterior = 0

    for i in range(n):
        error = calculate_error(x, x_anterior)
        temp_frame = p.DataFrame({'i'           : [i],
                                 'x'            : [x],
                                 'g(x)'         : [round(eval(g), 4)],
                                 'Convergencia' : [convergencia(gp, x)],
                                 'Ea'           : [error]})
        frame = frame.append(temp_frame)
        x_anterior = x
        x = round(eval(g), 4)

        if error < eps:
            return frame
    return f"Procedimiento completado sin éxito después de {n} iteraciones"

def main():
    (eps, x, n, g, gp) = ask_data()
    print(aproximate(eps, x, n, g, gp))

if __name__ == '__main__':
    main()

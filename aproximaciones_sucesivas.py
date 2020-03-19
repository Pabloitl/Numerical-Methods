from math import *
import pandas as p

def ask_data():
    eps = .05
    x = 1
    return eps, x

def calculate_error(valor_aprox, valor_anterior):
    if valor_anterior == 0:
        return 99999999
    return round(abs(valor_anterior - valor_aprox) / abs(valor_aprox) * 100, 4)

def convergencia(g, x):
    if abs(round(eval(g), 4)) > 1:
        return False
    return True

def aproximate(eps, x):
    frame = p.DataFrame()
    (g, gp) = ('(1 - x ** 3 + 2 * x ** 2) / 3',
               '(-3 * x ** 2 + 4 * x) / 3')
    i = 0
    x_anterior = 0

    while True:
        error = calculate_error(x, x_anterior)

        temp_frame = p.DataFrame({"i": [i],
                                 "x": [x],
                                 "g(x)": [round(eval(g), 4)],
                                 "Convergencia": [convergencia(gp, x)],
                                 "Ea": [error]})
        frame = frame.append(temp_frame)
        print(frame)
        input()

        if error < eps and convergencia(gp, x):
            return frame
        x_anterior = x
        x = round(eval(g), 4)
        i = i + 1

def main():
    (eps, x) = ask_data()
    print( aproximate(eps, x) )

if __name__ == '__main__':
    main()

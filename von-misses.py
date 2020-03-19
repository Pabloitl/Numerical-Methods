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

def aproximate(eps, x):
    frame = p.DataFrame()
    (f, fp) = ('x ** 3 - 2 * x ** 2 + 3 * x - 1',
               '3 * x ** 2 - 4 * x + 3')
    i = 0
    x_inicio = x
    x_anterior = 0
    error_anterior = 9999999999999999

    fp = fp.replace(' x ', 'x_inicio')
    while True:
        error = calculate_error(x, x_anterior)

        temp_frame = p.DataFrame({"i": [i],
                                 "x": [x],
                                 "f(x)": [round(eval(f), 4)],
                                 "f'(x)": [round(eval(fp), 4)],
                                 "Ea": [error]})
        frame = frame.append(temp_frame)

        if error < eps or error > error_anterior:
            return frame
        x_anterior = x
        error_anterior = error
        x = round(x - (round(eval(f),  4) / round(eval(fp),  4)), 4)
        i = i + 1

def main():
    (eps, x) = ask_data()
    print( aproximate(eps, x) )

if __name__ == '__main__':
    main()

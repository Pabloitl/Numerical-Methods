from math import *

def ask_data():
    eps = .05
    x = 2
    return eps, x

def calculate_error(valor_aprox, valor_anterior):
    if valor_anterior == 0:
        return 99999999
    return round(abs(valor_anterior - valor_aprox) / abs(valor_aprox) * 100, 4)

def aproximate(eps, x):
    print("i", "x", "f", "f'", "f''", "Ea", sep = "\t\t")
    (f, fp, fpp) = ('sin(10 * x) + cos(3 * x)',
                    '10 * cos(10 * x) - 3 * sin(3 * x)',
                    '-100 * sin(10 * x) - 9 * cos(3 * x)')
    i = 0
    x_anterior = 0

    while True:
        error = calculate_error(x, x_anterior)

        print(i, x, round(eval(f), 4), round(eval(fp), 4), round(eval(fpp),  4), error, sep='\t')

        if round(eval(f),  4) * round(eval(fpp),  4) <= 0 or error < eps:
            return
        x_anterior = x
        x = round(x - (round(eval(f),  4) / round(eval(fp),  4)), 4)
        i = i + 1

def main():
    (eps, x) = ask_data()
    aproximate(eps, x)

if __name__ == '__main__':
    main()

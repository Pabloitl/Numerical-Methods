import math

def ask_data():
    x  = float(input('Valor x: '))
    it = int(input('Iteraciones: '))
    return x, it

def aproximate(x, it):
    aprox = 0

    for i in range(it):
        temp = round(x ** (2 * i + 1) / math.factorial(2 * i + 1), 4)
        aprox = aprox + temp if i % 2 == 0 else aprox - temp

        print(f"iteración: {i}", f"aproximación: {aprox}", sep="\n")

def main():
    (x, it) = ask_data()
    results = aproximate(x, it)

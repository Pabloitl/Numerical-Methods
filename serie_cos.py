import math

def askData():
    x   = float(input('Valor x: '))
    eps = float(input('Error porcentual: '))
    return x, eps

def calculate_error(valor_real, valor_aprox):
    return round(abs(valor_real - valor_aprox) / abs(valor_real) * 100, 4)

def aproximate(x, eps):
    valor_real  = round(math.cos(x), 4)
    i           = 0
    valor_aprox = 0

    while (calculate_error(valor_real, valor_aprox) >= eps):
        temp = round(math.pow(x, i * 2) / math.factorial(i * 2), 4)
        if i % 2 == 0:
            valor_aprox = round(valor_aprox + temp, 4)
        else:
            valor_aprox = round(valor_aprox - temp, 4)
        i = i + 1
    return {'valor_real': valor_real, 'valor_aprox': valor_aprox}

def show_results(results):
    for key, value in results.items():
        print("{0}: {1}".format(key, value))

def main():
    (x, eps) = askData()
    results = aproximate(x, eps)
    show_results(results)

if __name__ == '__main__':
    main()

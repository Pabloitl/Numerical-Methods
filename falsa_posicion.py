import math

def ask_data():
    eps = float(input('Error porcentual: '))
    min = float(input('MIN: '))
    max = float(input('MAX: '))
    return eps, (min, max)

def calculate_error(valor_aprox, valor_anterior):
    if valor_anterior == 0:
        return 9999999
    return round(abs(valor_anterior - valor_aprox) / abs(valor_aprox) * 100, 4)

def sign(x):
    return x > 0

def aproximate(eps, rango):
    def f(x):
        return round(x ** 3 - 2 * math.sin(x), 4)
    i = 0
    m = 0
    m_anterior = 0
    (a, b) = rango
    print("i", "a", "f(a)", "b", "f(b)", "m", "f(m)", "error", "eps", sep='\t' * 2)

    while True:
        m_anterior = m
        m = round((b * f(a) - a * f(b)) / (f(a) - f(b)), 4)
        error = calculate_error(m, m_anterior)

        print(i, a, f(a), b, f(b), m, f(m), error, eps, sep='\t' * 2)

        if f(m) == 0:
            break

        if sign(f(a)) == sign(f(m)):
            a = m
        else:
            b = m

        if error < eps:
            return
        i = i + 1

def main():
    (eps, rango) = ask_data()
    aproximate(eps, rango)

if __name__ == '__main__':
    main()

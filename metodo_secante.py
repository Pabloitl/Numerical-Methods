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
        return round(6 * x ** 2 - 7 * x + 2, 4)
    (i, m, m_p) = (0, 0, 0)
    (a, b) = rango

    print("i", "a", "f(a)", "b", "f(b)", "m", "f(m)", "error", "eps", sep='\t' * 2)
    while True:
        m_anterior = m
        m = round((a * f(b) - b * f(a)) / (f(b) - f(a)), 4)
        error = calculate_error(m, m_anterior)

        print(i, a, f(a), b, f(b), m, f(m), error, eps, sep='\t' * 2)
        if f(m) == 0:
            break
        a = b
        b = m
        if error < eps:
            return
        i = i + 1

def main():
    (eps, rango) = ask_data()
    aproximate(eps, rango)

if __name__ == '__main__':
    main()

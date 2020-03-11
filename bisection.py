import math

def ask_data():
    eps = float(input('Error porcentual: '))
    min = float(input('MIN: '))
    max = float(input('MAX: '))
    return eps, (min, max)

def calculate_error(valor_aprox, valor_anterior):
    return round(abs(valor_anterior - valor_aprox) / abs(valor_aprox) * 100, 4)

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
        m = round((a + b) / 2, 4)
        error = calculate_error(m, m_anterior)

        print(i, a, f(a), b, f(b), m, f(m), error, eps, sep='\t' * 2)

        if f(a) * f(m) > 0:
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

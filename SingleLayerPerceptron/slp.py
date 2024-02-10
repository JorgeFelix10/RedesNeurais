entradas = [1, 7, 5]
pesos = [0.1, 0.8, 0]


def soma(e, p):
    s = 0
    for i in range(3):
        s += e[i] * p[i]
    return s


def stepfunction(valor):
    if valor >= 1:
        return 1
    return 0


pe = soma(entradas, pesos)
n = stepfunction(pe)

if n == 1:
    print(f'Neurônio Excitado.')
else:
    print(f'Neurônio Inibido.')

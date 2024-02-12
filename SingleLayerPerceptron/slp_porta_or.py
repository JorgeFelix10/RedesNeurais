import numpy as np

entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 1, 1, 1])
pesos = np.array([0.0, 0.0])
taxaApredizagem = 0.1


def stepfunction(pe):
    if pe >= 1:
        return 1
    return 0


def calculasaida(registro):
    s = registro.dot(pesos)
    return stepfunction(s)


def treinar():
    errototal = 1
    while errototal != 0:
        errototal = 0
        for i in range(len(saidas)):
            saidacalculada = calculasaida(np.asarray(entradas[i]))
            erro = saidas[i] - saidacalculada
            errototal += erro
            # EXIBIÇÃO DA TABELA VERDADE
            print(f'{entradas[i][0]}  {entradas[i][1]}     {saidacalculada}')
            for j in range(len(pesos)):
                pesos[j] += (taxaApredizagem * entradas[i][j] * erro)
            # print(f'Peso atualizado: {str(pesos)}')
        # print(f'Erro total: {str(errototal)}')
        print('\n')


treinar()
print(f'peso 1: {pesos[0]} peso 2: {pesos[1]}')

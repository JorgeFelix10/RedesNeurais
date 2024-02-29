import numpy as np


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))


def sigmoidderivada(sig):
    return sig * (1 - sig)  # derivada da função sigmoid


entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([[0], [1], [1], [0]])
"""
pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358, -0.577, 0.469]])
pesos1 = np.array([[-0.017], [-0.893], [0.148]])
"""

pesos0 = 2 * np.random.random((2, 3)) - 1
pesos1 = 2 * np.random.random((3, 1)) - 1
epocas = 100000
taxaAprendizagem = 0.3
momento = 1
# ESSE TRECHO DE CÓDIGO SERVE PARA PREVINIR A WARNING CAN BE UNDEFINED
camadaSaida = np.array([0, 1, 1, 0])

# FAZER UM FOR COM O NÚMERO DE EPOCAS
for _ in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)

    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)

    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print(f'Erro:{str(mediaAbsoluta)}')

    derivadaSaida = sigmoidderivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida

    pesos1Transposta = pesos1.T
    deltaSaidaXPesos = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPesos * sigmoidderivada(camadaOculta)

    camadaOcultaTransposta = camadaOculta.T
    pesosNovos1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovos1 * taxaAprendizagem)

    camadaEntradaTransposta = camadaEntrada.T
    pesosNovos0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovos0 * taxaAprendizagem)

# print(camadaSaida)
print(f' \n {round(camadaSaida[0][0])} \n {round(camadaSaida[1][0])} \n {round(camadaSaida[2][0])}'
      f' \n {round(camadaSaida[3][0])}')

# IMPLEMENTAÇÃO FUNÇÃO SIGMOIDE
import numpy as np


def sigmoide(soma):
    return 1 / (1 + np.exp(-soma))


a = sigmoide(0)

print(f'{a}')

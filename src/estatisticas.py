import numpy as np

def calcular_erro(y):
    if not y or len(y) == 0:
        return 0

    media = sum(y) / len(y)

    if media == 0:
        return 0

    erro = sum(abs(valor - media) for valor in y) / len(y)
    return erro


def desvio_padrao(y):
    if not y or len(y) == 0:
        return 0

    return float(np.std(y))
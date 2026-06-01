import numpy as np

def calcular_erro(y):
    
    media = np.mean(y)

    erro = [abs(valor - media) for valor in y]
    
    return np.mean (erro)
    
def desvio_padrao(y):

    return np.std(y)
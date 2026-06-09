import pandas as pd

def ler_csv(arquivo):
    dados = pd.read_csv(arquivo, skipinitialspace=True)

    x = dados.iloc[:, 0].astype(float).tolist()
    y = dados.iloc[:, 1].astype(float).tolist()

    return x, y
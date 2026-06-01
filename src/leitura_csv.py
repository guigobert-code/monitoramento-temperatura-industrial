import pandas as pd
def ler_csv(caminho):
    dados = pd.read_csv(caminho)

    x = dados.iloc[:, 0]. tolist()
    y = dados.iloc[:, 1]. tolist()

    return x, y

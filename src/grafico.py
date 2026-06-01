import os
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def gerar_grafico(x, y, valor_x, resultado):
    caminho = os.path.join("static", "grafico.png")

    plt.figure(figsize=(10, 5))

    plt.plot(x, y, marker="o", label="Dados reais")
    plt.scatter(valor_x, resultado, s=120, label="Valor interpolado")

    plt.title("Monitoramento de Temperatura Industrial")
    plt.xlabel("Tempo / Ponto de Medição")
    plt.ylabel("Temperatura")
    plt.grid(True)
    plt.legend()

    plt.savefig(caminho, bbox_inches="tight")
    plt.close()
   
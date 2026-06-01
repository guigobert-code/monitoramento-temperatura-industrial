from flask import Flask, render_template, request
from src.leitura_csv import ler_csv
from src.interpolacao import lagrange
from src.estatisticas import calcular_erro, desvio_padrao
from src.grafico import gerar_grafico

app = Flask(__name__)

arquivo = "dados/temperatura.csv"

x, y = ler_csv(arquivo)


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    desvio = None
    valor_x = None
    status = None

    try:
        erro = calcular_erro(y)
        desvio = desvio_padrao(y)

        if request.method == "POST":
            valor_x = float(request.form["valor_x"])
            resultado = lagrange(valor_x, x, y)

            if resultado < 50:
                status = "Normal"
            elif resultado < 80:
                status = "Alerta"
            else:
                status = "Crítico"

            gerar_grafico(x, y, valor_x, resultado)

    except Exception as e:
        print("Erro:", e)

    return render_template(
        "index.html",
        resultado=resultado,
        erro=erro,
        desvio=desvio,
        valor_x=valor_x,
        status=status
    )
    
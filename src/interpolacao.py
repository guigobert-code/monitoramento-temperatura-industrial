def lagrange(valor_x, xs, ys):
    n = len(xs)
    resultado = 0

    if len(xs) != len(ys):
        raise ValueError("As listas X e Y precisam ter o mesmo tamanho.")

    if len(set(xs)) != len(xs):
        raise ValueError("Existem valores repetidos na coluna X do CSV.")

    for i in range(n):
        termo = ys[i]

        for j in range(n):
            if i != j:
                denominador = xs[i] - xs[j]

                if denominador == 0:
                    raise ValueError("Erro: existem valores iguais na coluna X.")

                termo *= (valor_x - xs[j]) / denominador

        resultado += termo

    return resultado

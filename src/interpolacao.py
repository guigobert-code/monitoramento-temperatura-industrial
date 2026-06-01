def lagrange(valor_x, xs, ys):
    n = len(xs)
    resultado = 0

    for i in range(n):
        termo = ys[i]

        for j in range(n):
            if j != i:
                termo *= (valor_x - xs[j]) / (xs[i] - xs[j])

        resultado += termo

    return resultado


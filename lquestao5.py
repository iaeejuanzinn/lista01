def encontrar_combinacoes_para_oito():
    resultados = []
    for a in range(1,10):
        for b in range(1,10):
            for op1 in ['+', '-', '*', '/']:
                for op2 in ['+', '-', '*', '/']:
                    for op3 in ['+', '-', '*', '/']:
                     expressao = f"{a} {op1} {b} {op2} {a} {op3} {b}"
                     try:
                        resultado = eval(expressao)
                        if resultado == 8:
                            resultados.append(expressao)
                     except ZeroDivisionError:
                        pass
    return resultados

combinacoes_para_oito = encontrar_combinacoes_para_oito()
print("Combinações em que o resultado é 8:")
for combinacao in combinacoes_para_oito:
    print(combinacao)
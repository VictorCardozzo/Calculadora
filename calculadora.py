while True:
    expressao = input("Digite uma expressão matemática (ou 'sair' para encerrar): ")

    if expressao.lower() == "sair":
        print("Calculadora encerrada.")
        break

    try:
        resultado = eval(expressao)
        print("O resultado é:", resultado)
    except:
        print("Expressão inválida! Tente novamente.")
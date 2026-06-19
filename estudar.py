while True:
    A = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    B = float(input("Digite o segundo número: "))

    if operacao == "+":
        print("Resultado:", A + B)

    elif operacao == "-":
        print("Resultado:", A - B)

    elif operacao == "*":
        print("Resultado:", A * B)

    elif operacao == "/":
        if B != 0:
            print("Resultado:", A / B)
        else:
            print("Não é possível dividir por zero.")

    else:
        print("Operação inválida.")

    continuar = input("\nDeseja fazer outro cálculo? (s/n): ")

    if continuar.lower() != "s":
        print("Calculadora encerrada!")
        break
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def potencia(x, y):
    return x ** y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        print("Não é possível dividir por zero.")
        return None

while True:
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Potência")
    print("5. Divisão")
    print("6. Sair")

    operacao = int(input("Operação escolhida: "))

    if operacao == 6:
        break

    numero_x = float(input("Digite o valor de X: "))
    numero_y = float(input("Digite o valor de Y: "))

    if operacao == 1:
        resultado = soma(numero_x, numero_y)
        operacao_nome = "Soma"
    elif operacao == 2:
        resultado = subtracao(numero_x, numero_y)
        operacao_nome = "Subtração"
    elif operacao == 3:
        resultado = multiplicacao(numero_x, numero_y)
        operacao_nome = "Multiplicação"
    elif operacao == 4:
        resultado = potencia(numero_x, numero_y)
        operacao_nome = "Potência"
    elif operacao == 5:
        resultado = divisao(numero_x, numero_y)
        operacao_nome = "Divisão"
    else:
        print("Operação inválida")
        continue

    if resultado is not None:
        print(f"A operação escolhida foi {operacao_nome}")
        print(f"O resultado de {operacao_nome} entre {numero_x} e {numero_y} é igual a {resultado}")

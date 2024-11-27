

while(True):

    nmr1 = float(input("Digite o primeiro número: "))
    nmr2 = float(input("Digite o segundo número: "))
    opr =  str(input("Digite a operação: "))


    soma = nmr1 + nmr2
    subtracao = nmr1 - nmr2
    multiplicacao = nmr1 * nmr2
    divisao = nmr1 / nmr2

    if opr == '+' : print(soma)
    elif opr == '-' : print(subtracao)
    elif opr == '*' : print(multiplicacao)
    elif opr == '/' : print(divisao)


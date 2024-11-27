#LOGIN

senha_correta = "python 1244"
senha = ""
while senha != senha_correta:
    senha = input("Digite a senha: ")
    if senha != senha_correta:
        print("Senha incorreta, tente novamente.")
    else: 
        print("Senha correta! Acesso concedido.")

#ACUMULADOR PÓS LOGIN
soma = 0
numero = 1

while numero <= 100:
    soma +=  numero
    numero += 1 #incrementa o número que sera somado até o resultado final
    print("A soma dos números de 1 a 100 é: ", soma)


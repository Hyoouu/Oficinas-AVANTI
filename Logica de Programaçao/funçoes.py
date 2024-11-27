#FUNÇÕES

#FUNÇÃO ÁREA
def calcular_area(largura, altura):
    area = largura * altura
    return area


print(calcular_area(7, 5))

#FUNÇÃO NOME
def imprimir_nome(nome):
    print(f"Olá, {nome}!")
#expressar nome
imprimir_nome("Mohammed")

#FUNÇÃO NUMERO PAR
def eh_par(numero):
    return numero % 2 == 0

#CHAMANDO A FUNÇÃO
numero = 152

if eh_par(numero):
    print(f"O número {numero} é par.")
else : print(f"O  número {numero} é ímpar.")


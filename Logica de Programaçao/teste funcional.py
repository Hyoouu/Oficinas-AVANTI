#CALCULADORA DE MÉDIA

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(media)

if media < 6 : print("você foi reprovado")
else: print("você foi aprovado")
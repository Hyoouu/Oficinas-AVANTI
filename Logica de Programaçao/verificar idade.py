#VERIFICAR IDADE/PREÇO DO INGRESSO
print("Bem vindo ao cinema!")

idade = float(input("Digite sua idade para saber o preço do ingresso: "))

if idade < 10 : print("Ingresso Gratuito!")

elif idade == 10 : print("O valor do ingresso é R$10,00)")

elif idade <= 13 : print("O valor do ingresso é R$12,00")

elif idade <= 16 : print("O valor do ingresso é R$14,00")

elif idade < 18 : print("O valor do ingresso é R$16,00")

else : print("O valor do ingresso é R$32,00")
  


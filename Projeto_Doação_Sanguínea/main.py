#Luis Gustavo da Silva Vasconcelos - Turma N3
#MENU(DOAÇÃO)

#variáveis
idade = 0
peso = 0
tatuagem = ''
numero = 0

#Apresentação
print("Olá, seja bem vindo ao projeto DOE++.")
print("O programa tem por objetivo alcançar o máximo de possíveis doadores de sangue, para ajudar aqueles que necessitam de tal ajuda.")
print("O que deseja saber?")
print("""Digite:
      1 para saber quem pode doar,
      2 para saber os benefícios da doação,
      3 para entender os procedimentos,
      4 para descobrir locais e horários para doar, ou
      5 para saber se está apto a doar.
      Para cancelar digite qualquer outro numero.""")

#Estrutura de Repetição
while(True):
    numero = int(input("Número: "))

        #ESTRUTURA DE DECISÃO
    if numero == 1 : 
        print("Para se candidatar à doação de sangue, é preciso estar saudável, bem alimentado, pesar acima de 50 kg, ter entre 16 e 69 anos e apresentar um documento oficial com foto. Os menores de idade devem portar o Termo de Consentimento padrão assinado pelos pais ou responsável legal.")
    elif numero == 2 : 
        print("Doadores de sangue possuem direito a 1 dia de folga(o dia da doação), possuem menos risco de contrair qualquer tipo de câncer(pela troca sanguínea, forçando o sangue a se renovar), e ainda tem a capacidade de ajudar a salvar diversas vidas que necessitam desse recurso vital. ")
    elif numero == 3 : 
        print("1 - Não vá de jejum e alimente-se com alimentos leves, hidrate-se, evite alimentos gordurosos no dia da doação. \n2 - Cadastre-se na unidade de doação que estiver utlizando seu documento oficial com foto(RG, CNH, PASSAPORTE), e participe da triagem clínica. Para a faixa etária entre 16 e 18 anos incompletos é necessário acompanhante maior de idade com documento! \n3 - A coleta dura em torno de 15 a 20 minutos, e é feita completamente com material esterilizado e descartável, não apresenta riscos aos doadores. \n4 - Pós-doação, lembre-se de fazer um pequeno lanche e hidratar-se, evite esforço físico exagerado por pelo menos 12 horas, não furma por cerca de 2 horas, evitar bebidas alcóolicas por 12 horas e não dirigir veículos de grande porte. Exercícios e práticas esportivas também devem ser evitadas logo após a doação." )
    elif numero == 4 : 
        print("Hemoce(Av. José Bastos, 3390) - 07:00 a 16:00 \nFujisan(Av. Barão de Studart, 2626) - 07:30 a 13:00 \nHemoce(Av. Des. Moreira, Aldeota) - 07:00 a 16:00")
    elif numero == 5:
        #Questionário de Aptidão
        idade = float(input("Digite sua idade: ")) 
        peso = float(input("Digite seu peso em kg: ")) 
        tatuagem = str(input("Fez tatuagem nos últimos 6 meses (s/n): "))
        if idade < 18 and peso >= 50 and tatuagem == 'n'  : print("Apto somente com responsável")
        elif idade >= 18 and peso >= 50 and tatuagem == 'n' : print("Você está apto a doar!")
        elif idade >= 18 and peso >= 50 and tatuagem == 's' : print("Você não está apto pois possui tatuagem recente. Te aguardamos numa próxima!")
        elif idade >= 70 and peso >= 50 and tatuagem == 'n' : print("Você não está apto, idade avançada!")
        else : print("Talvez você tenha errado alguma coisa, tente novamente!")
        #Avisos Importantes
        print("Agradecemos seu interesse na doação de sangue, e esperamos que nos conceda a oportunidade de lhe ver outras vezes!")
        print("LEMBRE-SE:Mulheres podem doar sangue a cada intervalo de 90 dias, podendo fazer até 3 doações por ano. Homens podem fazer até 4 doações por ano, aguardando 60 dias de intervalo. ")
    else:
        break



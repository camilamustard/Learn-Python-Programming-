nome = input("Olá, qual é o seu nome?")
print("Prazer", nome)
print(
    "não se preocupe, tudo isso irá passar e tudo ficará bem. Seja bem-vindo a plataforma py da Camila."
)
Resposta = input("vamos testar seus conhecimentos, quem descobriu o Brasil?")
print("...")
print("analisando")
print("1,2,3...")
print("estou quase pronta,sou um robô que demora para se arrumar.")
print("Vamos parar de charme e analisar sua resposta;")

print(
    "Será que foi esse cara mesmo?", Resposta,
    "..., hm, será? eu sendo uma máquina sou livre para te questionar e te induzir ao erro, ."
)
Resposta2 = input("posso? por favorzinho..."
                  "sei que você é legal.me permite?")
print(
    Resposta2, nome,"saiba que viver é uma arte, A vida é uma arte,O mundo é um palco mas quem escreve e vive a história somos nós. Para existir o espetáculo três coisas são essenciais:Uma boa história,Um bom artista e Uma entusiasmada plateia."
)
print(
    "eu sei que sou um robô de humanas mas preciso aprender a ser uma calculadora nessa parte do projeto"
)
print(
    "A partir dessa linhga sou uma calculadora simpleso"
)
#Calculadora de python
######################
#Perguntar pro usuário qual o tipo de operação
#Perguntar o primeiro número
#perguntar o segundo número
#Calculo desses 2 números
#Imprime o resultado na tela

operacao= input("Qual operação (+,-,*,/) você quer fazer?")
num1= int (input("Digite o primeiro numero:"))
num2= int (input ("Digite o segundo numero:"))
if operacao == '+':
  total=num1+num2
  print(total)
elif operacao == "-":
  total=num1-num2
  print(total)
elif operacao == '*':
  total= num1*num2
  print('total')
elif operacao== '/':
  total=num1/num2
  print('total')
else:
  print("operacao invalida")
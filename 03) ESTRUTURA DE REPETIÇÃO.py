from time import sleep

#=========[ 1 ]CONTADOR GENÉRICO:================================
cont = 1
for c in range(0, 101, 1):
    print(f"⭐Contagem: {c}", end="\r")
    cont += 1
    sleep(0.1)
    
#=========[ 2 ]CONTAGEM PERSONALIZADA:====================================	
I = int(input("😎Digite o início da contagem:\n>>>"))
F = int(input("😎Digite o fim da contagem:\n>>>"))
print(f"🔔Contagem de {I} até {F}")
for c in range(I, F+1, 1):
    print(f"⭐VALOR [{c}/{F}]", end="\r")
    cont += 1
    sleep(1)

#=========[ 3 ]INTERROMPENDO LOOP:=============================================
while True:
    quarto = str(input("😬Já arrumou seu quarto?[S/N]:\n>>>")).strip().upper()[0]
    if quarto in "Nn":
        print("😠Você está de castigo!!!")
        for c in range(0, 11, 1):
            print(f"⭐Esperando [{c}/10]",end="\r")
            cont += 1
            sleep(1)
    elif quarto in "Ss":
        print("🔔Você está liberado!")
        break
    else:
        print("😬Não compreendo...")
        
#==========[ 4 ]VALIDAÇÃO DE SEXO:======================================
sexo = input("😎Informe o seu sexo[M/F]:\n>>>").strip().upper()[0]
while sexo not in "MmFf":
    sexo = input("😠Dados inválidos!!!\n😬Por favor, informe seu sexo[M/F]:\n>>>").strip().upper()[0]
    if sexo in "Mm":
       sexo = "HOMEM"
       break
    if sexo in "Ff":
       sexo = "MULHER"
       break
print(f"🌝Isso significa que você é {sexo}!!!")
sleep(3) 

#===========[ 5 ]JOGO DE ADIVINHAÇÃO 2.0:==================================
from random import randint

computador = randint(0,10)
print("😠Acabei de pensar em um número entre 0 e 10!")
sleep(2)

acertou = False
palpites = 0

while not acertou:
    jogador = int(input("😎Qual é o seu palpite:\n>>>"))
    palpites += 1
    if jogador == computador:
        acertou = True
        resultado = "👍ACERTOU com {} Tentativas!".format(palpites)
    else:
        if jogador < computador:
            print("👎ERRADO!!!➕VALOR É MAIOR QUÊ {}!!!".format(jogador))
        elif jogador > computador:
            print("👎ERRADO!!!➖VALOR É MENOR QUÊ {}!!!".format(jogador))
            
print("_" *35)
print("⭐Eu pensei no n°{}!\n⭐Você digitou:{}!\n⭐RESULTADO:{}".format(computador, jogador, resultado))
print("_" *35)

#==========[ 6 ]TABUADA (3.0):===============================
num = opr = c = 0
while True:
    num = int(input("😎Digite um número:\n🔔Envie float caso queira parar:\n>>>"))
    if num < 0:
        break
    opr = str(input("😎Digite o sinal aritmético[+×÷-]:\n>>>"))
    for c in range(1, 11):
        if opr == "×":
            print(f"{num} × {c:2} = {num*c}")
        elif opr == "+":
            print(f"{num} + {c:2} = {num+c}")
        elif opr == "-":
            print(f"{num} - {c:2} = {num-c}")
        elif opr == "÷":
            print(f"{num} ÷ {c:2} = {num/c}")
        else:
            print(f"😠Valor {opr} é inválido!!!")
print("⛔FIM!!")
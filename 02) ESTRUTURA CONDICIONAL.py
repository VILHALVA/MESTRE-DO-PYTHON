from time import sleep

#=========[ 1 ]ENTREVISTA CONPET:========================
nome = input("😎Qual é o seu nome?\n>>>").strip().upper()
if "SAMUEL" in nome or "DANIEL" in nome or "LUCAS" in nome or "MARIA" in nome or "ANA" in nome:
    print("😍Que nome lindo você tem!")
else: 
    print("😒Seu nome é tão comum!")
sleep(3) 
escola = input("😎Você tem o ensino médio completo?\n>>>").strip().upper()
if "SIM" in escola or "TENHO" in escola or "FIZ" in escola or "FACULDADE" in escola or "UNIVERSIDADE" in escola:
    print("👏PARABÉNS!!!")
elif "NÃO" in escola or "FUNDAMENTAL" in escola:
    print("😔Assim fica complicado️!") 
else:
    print("👏️Continue,que você consegue!!!️")
sleep(3)  

#==========[ 2 ]MÉDIA ARITMÉTICA:======================================
n1 = float(input("😎Digite sua 1ª nota:\n>>>"))
n2 = float(input("😎Digite sua 2ª nota:\n>>>"))
média = (n1 + n2) / 2
if média >= 7:
    situação = "👍APROVADO!"
else:
    if média < 7 and média >= 5:
        situação = "👎RECUPERAÇÃO!"
    else:
        situação = "😬REPROVADO!"

if média <= 10.00 and média > 9.00:
    classe = "A"
elif média <= 8.90 and média > 8.00:
    classe = "B"
elif média <= 7.90 and média > 7.00:
    classe = "C"
elif média <= 6.90 and média > 6.00:
    classe = "D"
elif média <= 5.90 and média > 5.00:
    classe = "E"
elif média < 5:
    classe = "F"
else:
    classe = "NENHUM"
    
print(f"⭐N1 é {n1}, N2 é {n2}!\n⭐Média é {média}\n⭐RESULTADO: {situação}\n⭐Classificação: {classe}")

#==========[ 3 ]ALISTAMENTO MILITAR:============================
import datetime

atual = datetime.date.today().year
sexo = str(input("😎Qual é o seu sexo?\n😎masculino ou feminino?\n>>>")).strip().upper()
if sexo == "MASCULINO":
    nasc = int(input("😎Digite o ano do seu nascimento:\n>>>"))
    idade = atual - nasc

    print("_" *35)
    if idade == 18:
        resultado = "⭐Tem que se alistar imediatamente!"
    elif idade < 18:
        saldo = 18 - idade 
        ano = atual + saldo
        resultado = "⭐Faltam {:.0f} anos para o alistamento!\n⭐Seu alistamento será em {:.0f}!".format(saldo, ano)
    elif idade > 18:
        saldo = idade - 18
        ano = atual - saldo
        resultado = "⭐Deveria ter se alistado há {:.0f} anos!\n⭐Seu alistamento foi em {:.0f}!".format(saldo, ano)
        
    print("⭐Para quem nasceu em {:.0f};\n⭐Tem {:.0f} anos em {:.0f};\n{}".format(nasc, idade, atual, resultado))
    print("_" *35)
elif sexo == "FEMININO":
    print("😔Sinto muito!!!; Em nosso país só é permitido homens!!!")
else:
    print("😡Não compreendo!!!")  
    
#==========[ 4 ]ANALISANDO TRIÂNGULOS:=========================
r1 = float(input("😎Digite o primeiro segmento:\n>>>"))
r2 = float(input("😎Digite o segundo segmento:\n>>>"))
r3 = float(input("😎Digite o terceiro segmento:\n>>>"))
print("⏳Processando...",end="\r")
sleep(3)

print("_" *35)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 == r3:
        triângulo = "👍SIM;\n⭐TIPO: EQUILÁTERO!"
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        triângulo = "👍SIM;\n⭐TIPO: ISÓSCELES!"
    elif r1 != r2 != r3 != r1:
        triângulo = "👍SIM;\n⭐TIPO: ESCALENO!"
else:
    triângulo = "👎NÃO!"

print("⭐SEGMENTOS: {}, {} e {}!\n⭐TRIÂNGULO?:{}".format(r1, r2, r3, triângulo))
print("_" *35)  

#==========[ 5 ]JOGO DE ADIVINHAÇÃO:==========================
from random import randint

print("-=-" *10)
print("😎Vou pensar em número entre 0 e 10. Tente adivinhar!!!")
print("-=-" *10)
computador = randint(0, 10) #>Faz o computador "PENSAR"

jogador = int(input("😎Em que número pensei?\n>>>")) #>Jogador tenta "ADVINHAR"
print("⏳Processando...",end="\r")
sleep(3)
if jogador == computador:
   print("😵PARABÉNS!!! Você acertou!!!")
else:
   print("😡VOCÊ PERDEU!!! O número é {}!!!".format(computador))
print("⛔GAME OVER.")
          
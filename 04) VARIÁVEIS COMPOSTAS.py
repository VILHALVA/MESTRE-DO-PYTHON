#==============[ 1 ]LISTA DE PREÇOS EM TUPLAS:================================
listagem = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.90,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livros", 34.90)
print("_" *30)
print(f"{'LISTAGEM DE PREÇOS:':^30}")
print("_" *30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<15}",end=" ")
    else:
        print(f"R${listagem[pos]:.>3.2f}")        
print("_" *30)

#==========[ 2 ]PARES E IMPARES NA LISTA:==========================
VALOR = [[], []]
cont = 1
while True:
    num = int(input(f"😎Digite o {cont}ª valor:\n>>>"))
    cont += 1
    if num % 2 == 0:
        VALOR[0].append(num)
    elif num % 2 == 1:
        VALOR[1].append(num)
    res = str(input(f"😠Voce quer digitar o {cont}ª valor?[S/N]:\n>>>")).strip().upper()[0]
    if res in "Ss":
        continue
    elif res in "Nn":
        break
    else:
        print("⛔Não compreendo...")

VALOR[0].sort()
VALOR[1].sort()
print(f"⭐Analisando {cont} valores:\n⚡PARES: {VALOR[0]}\n⚡IMPARES: {VALOR[1]}")

#============[ 3 ]MATRIZES 3 × 3 NA LISTA:=================================================
MATRIZ = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        MATRIZ[l][c] = int(input(f"😎Digite o [{c+1}/{l+1}] valor:\n>>>"))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{MATRIZ[l][c]}]",end="")
    print()

#==========[ 4 ]CADASTRO DO TRABALHADOR EM DICIONÁRIO:============================
from datetime import datetime

dados = dict()
dados["nome"] = str(input("😎Digite seu nome:\n>>>"))
nasc = int(input("😎Digite seu ano de nascimento:\n>>>"))
dados["idade"] = datetime.now().year - nasc
dados["ctps"] = int(input("😎Sua carteira de trabalho.\n😎Envie 0 se não tiver:\n>>>"))

if dados["ctps"] != 0:
    dados["contratação"] = int(input("😎Seu ano de contratação:\n>>>"))
    dados["salário"] = float(input("😎Qual é o seu salário[R$]?:\n>>>"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)
    
print("_" *35)
for k, v in dados.items():
    print("-" *20, f"\n★{k} é {v}!\n", "-" *20) 
print("_" *35)
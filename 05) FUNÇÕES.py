from time import sleep

#============[ 1 ]SENHA DE AUTENTICAÇÃO:========================================================================
cont = 1
def tempo(txt1, I, txt2):
     print(f"😠Foram {cont} tentativas!!!", end="\r")
     sleep(2)
     for c in range(I, 0, -1):
         print(f"{txt1}: {c} {txt2}", end="\r")
         sleep(1)
     senha = str(input("🔐Digite a senha para começar:\n>>>"))   
senha = str(input("🔐Digite a senha para começar:\n>>>"))
while senha not in "SAMUEL":
    cont += 1
    senha = str(input("🔒Senha inválida!!!Tente novamente:\n>>>"))
    if cont == 3:
        tempo("⌛Aguarde", 60, "segundos...")        
    elif cont == 6:
        tempo("⌛Aguarde", 300, "segundos...")
    elif cont > 10:
        tempo("⌛Aguarde", 9999999, "segundos...")                
print("=" *35, f"\n👏PARABÉNS!!!\n🔓VOCÊ ACERTOU!!!\n⭐Foram {cont} tentativas!!!\n", "=" *35)
sleep(2)

#==========[ 2 ]FORMATANDO MOEDAS:=========================
#-----------[ A ]FUNCÕES:----------------------------------
def aumentar(preço=0, formato=False):
    res = preço + (preço * preço / 100)
    return res if formato is False else moeda(res)
    
def diminuir(preço=0, formato=False):
    res = preço - (preço * preço / 100)
    return res if formato is False else moeda(res)

def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)
    
def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)
    
def moeda(preço=0, moeda="R$"): 
    return f"{moeda}{preço:>4.2f}".replace(".", ",")
    
#----------[ B ]PROGRAMA PRINCIPAL:-------------------------------
#from moeda import metade, dobro, aumentar, diminuir 

p = float(input("😎Digite o preço:\n>>>"))
print("_" *35, f"\n⭐O aumento de {moeda(p)} é {moeda(aumentar(p))}!\n⭐O diminuto de {moeda(p)} é {moeda(diminuir(p))}!\n⭐O dobro de {moeda(p)} é {moeda(dobro(p))}!\n⭐A metade de {moeda(p)} é {moeda(metade(p))}!\n", "_" *35)

#🔺Quando se usa a modularisação, para que aja a formação (R$), é necessário implementar o "True" em "{moeda(função(p, True))}".

#==========[ 3 ]MENU DE CADASTRO:===============================
#-----------[ A ]FUNCOES BÁSICAS(ex115.lib.interface):--------------------------
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31m😬ERRO! Digite um valor Inteiro!!!\033[m")
            continue
        except KeyboardInterrupt:
            print("🔺Houve erro! Usuário não digitou valor!")
            return n
        else:
            return n

def linha(tam=35):
    return "_" * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(28))
    print(linha())
    
def menu(lista):
    cabeçalho("😈MENU PRINCIPAL:")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[32m😎Digite o número da sua opção:\n>>>\033[m")
    return opc
    
#-----------[ B ]CRIAR/LER ARQUIVO(ex115.lib.arquivo):-----------------------------------------------
#import ex115.lib.interface import *
	
def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("🔻Falha ao criar arquivo!!!")
    else:
        print(f"👍Arquivo {nome} criado com sucesso!!!")

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("🔻Falha ao ler arquivo!!!")
    else:
        cabeçalho ("🎂PESSOAS CADASTRADAS:")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"👤{dado[0]:<15}{dado[1]:3>} anos")
    finally:
        a.close()
        
def cadastrar(arq, nome=0, idade=0):
    try:
        a = open(arq, "at")
    except:
        print("🔻Falha ao abrir arquivo!!!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("🔻Falha ao escrever os dados!!!")
        else:
            print(f"👍Novo registro de {nome} adicionado com sucesso!!!")
            a.close()
                   
#--------[ C ]PROGRAMA PRINCIPAL:-----------------------------------
#import ex115.lib.interface import *
#import ex115.lib.arquivo import *
from time import sleep

arq = "CURSO_EM_VIDEO.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)        
    
while True:
    resposta = menu(["PESSOAS CADRASTRADAS", "CADASTRAR NOVA PESSOA", "SAIR DO PROGRAMA"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("➕NOVO CADASTRO:")
        nome = str(input("👤NOME:\n>>>"))
        idade = leiaInt("👤IDADE:\n>>>")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("⛔FIM DO SISTEMA")
        break
    else:
        cabeçalho("\033[31m⛔ERRO! Digite uma opção válida!!!\033[m") 
    sleep(2)




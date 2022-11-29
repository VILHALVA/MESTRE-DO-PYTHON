#============[ 1 ]OPERAÇÃO COM STRING:===================
frase = "Curso em vídeo Python"

print(frase)
print("⭐1>",frase[3:13])
print("⭐2>",frase[5:10])
print("⭐3>",frase[:13])
print("⭐4>",frase[1:15:2])
print("⭐5>",frase[1::2])
print("⭐6>",frase[::2])
print("⭐7>",frase.count("o"))
print("⭐8>",frase.count("O"))
print("⭐9>",frase.count("a"))
print("⭐10>",frase.count("A"))
print("⭐11>",frase.upper())
print("⭐12>",frase.upper().count("o"))
print("⭐13>",len(frase))
print("⭐14>",len(frase.strip()))
print("⭐15>",frase.replace("Python", "Android"))

frase = frase.replace("Python", "Windows")
print("⭐16>",frase)
print("⭐17>","Curso" in frase)
print("⭐18>",frase.find("Vídeo"))
print("⭐19>",frase.lower().find("vídeo"))
print("⭐20>",frase.split())

dividido = frase.split()
print("⭐21>",dividido[0])
print("⭐22>",dividido[2][3])

#========[ 2 ]USO DA FORMATAÇÃO:=============================
nome = str(input("😎Digite seu nome:\n>>>")).strip().upper()
print(f"👤Seu nome é {nome}")
idade = int(input("😎Qual é sua idade?\n>>>"))
print(f"⭐Você tem {idade} anos")
altura = float(input("😎Qual é a sua altura?:\n>>>"))
print(f"🔔Você tem {altura} metros de altura")

#==============[ 3 ]CALCULO DA MÉDIA ARITMÉTICA:==========================================       
nota1 = float(input("😎Digite a sua 1° Nota da prova:\n>>>"))
nota2 = float(input("😎Digite a sua 2° Nota da prova:\n>>>"))
nota3 = float(input("😎Digite a sua 3° Nota da prova:\n>>>"))
nota4 = float(input("😎Digite a sua 4° Nota da prova:\n>>>"))      
média = (nota1 + nota2 + nota3 + nota4) / 4    
print(f"⚡Sua 1° Nota é: ({nota1:.1f});\n⚡Sua 2° Nota é: ({nota2:.1f});\n⚡Sua 3° Nota é: ({nota3:.1f});\n⚡Sua 4° Nota é: ({nota4:.1f});\n⭐A sua MÉDIA é: ({média:.1f})!")

#==============[ 4 ]CALCULAR DESCONTOS(%):==================================================================================  
print("😎Agora vamos calcular o seu desconto...")
preço = float(input("😎Digite o seu valor original(R$):\n>>>"))
desconto = float(input("😎Digite o seu desconto(%):\n>>>"))
pagar = preço - (preço * desconto / 100)   
print(f"⚡Preço de R${preço:.2f}!\n⚡Com um desconto de {desconto:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!")        

#===========[ 5 ]CALCULAR AUMENTOS(%):================================================
print("😎Agora vamos calcular o seu desconto...")
preço = float(input("😎Digite o seu valor original(R$):\n>>>"))
desconto = float(input("😎Digite o seu desconto(%):\n>>>"))
pagar = preço + (preço * desconto / 100)   
print(f"⚡Preço de R${preço:.2f}!\n⚡Com um desconto de {desconto:.0f}%!\n⭐Valor a pagar é de R${pagar:.2f}!")        
   
    
